"""
Database query functions for BookWise.
Provides cached data access methods for all models.
"""

from typing import List, Optional
import json
import streamlit as st

from sqlalchemy.orm import Session, joinedload

from database.models import Genre, Book, Summary, SummaryImage
from database.connection import get_db_session


# Cache TTL in seconds (5 minutes for genre/count data)
CACHE_TTL = 300


@st.cache_data(ttl=CACHE_TTL)
def get_all_genres() -> List[Genre]:
    """
    Get all genres ordered by name. (Cached)
    
    Returns:
        List[Genre]: All genres in alphabetical order
    """
    with get_db_session() as session:
        genres = session.query(Genre).order_by(Genre.name).all()
        # Detach from session for caching
        session.expunge_all()
        return genres


def get_genre_by_slug(slug: str) -> Optional[Genre]:
    """
    Get a genre by its URL slug.
    
    Args:
        slug: URL-friendly genre identifier
    
    Returns:
        Optional[Genre]: The genre if found, None otherwise
    """
    with get_db_session() as session:
        genre = session.query(Genre).filter(Genre.slug == slug).first()
        if genre:
            session.expunge(genre)
        return genre


def get_books_by_genre(genre_slug: str, limit: Optional[int] = None) -> List[Book]:
    """
    Get all books in a specific genre.
    
    Args:
        genre_slug: URL-friendly genre identifier
        limit: Maximum number of books to return
    
    Returns:
        List[Book]: Books in the specified genre
    """
    with get_db_session() as session:
        query = (
            session.query(Book)
            .join(Genre)
            .filter(Genre.slug == genre_slug)
            .order_by(Book.title)
        )
        if limit:
            query = query.limit(limit)
        books = query.all()
        session.expunge_all()
        return books


def get_book_by_slug(slug: str) -> Optional[Book]:
    """
    Get a book by its URL slug with related data.
    
    Args:
        slug: URL-friendly book identifier
    
    Returns:
        Optional[Book]: The book with genre loaded, None if not found
    """
    with get_db_session() as session:
        book = (
            session.query(Book)
            .options(joinedload(Book.genre))
            .filter(Book.slug == slug)
            .first()
        )
        if book:
            # Access related objects before expunge
            _ = book.genre
            session.expunge_all()
        return book


def get_summary_for_book(book_id: int) -> Optional[Summary]:
    """
    Get the summary for a specific book.
    
    Args:
        book_id: Book database ID
    
    Returns:
        Optional[Summary]: The book's summary if exists
    """
    with get_db_session() as session:
        summary = (
            session.query(Summary)
            .filter(Summary.book_id == book_id)
            .first()
        )
        if summary:
            session.expunge(summary)
        return summary


def get_images_for_summary(summary_id: int) -> List[SummaryImage]:
    """
    Get all images for a specific summary.
    
    Args:
        summary_id: Summary database ID
    
    Returns:
        List[SummaryImage]: Images ordered by their display order
    """
    with get_db_session() as session:
        images = (
            session.query(SummaryImage)
            .filter(SummaryImage.summary_id == summary_id)
            .order_by(SummaryImage.order)
            .all()
        )
        session.expunge_all()
        return images


@st.cache_data(ttl=CACHE_TTL)
def get_featured_books(limit: int = 8) -> List[Book]:
    """
    Get featured books for the homepage. (Cached)
    
    Args:
        limit: Maximum number of books to return
    
    Returns:
        List[Book]: Featured books with genres loaded
    """
    with get_db_session() as session:
        books = (
            session.query(Book)
            .options(joinedload(Book.genre))
            .filter(Book.is_featured == True)
            .order_by(Book.title)
            .limit(limit)
            .all()
        )
        # Access related objects before expunge
        for book in books:
            _ = book.genre
        session.expunge_all()
        return books


def search_books(query: str, limit: int = 20) -> List[Book]:
    """
    Search books by title or author.
    
    Args:
        query: Search term
        limit: Maximum number of results
    
    Returns:
        List[Book]: Matching books with genres loaded
    """
    with get_db_session() as session:
        search_term = f"%{query}%"
        books = (
            session.query(Book)
            .options(joinedload(Book.genre))
            .filter(
                (Book.title.ilike(search_term)) | 
                (Book.author.ilike(search_term))
            )
            .order_by(Book.title)
            .limit(limit)
            .all()
        )
        for book in books:
            _ = book.genre
        session.expunge_all()
        return books


def get_all_books(limit: Optional[int] = None) -> List[Book]:
    """
    Get all books with their genres.
    
    Args:
        limit: Maximum number of books to return
    
    Returns:
        List[Book]: All books ordered by title
    """
    with get_db_session() as session:
        query = (
            session.query(Book)
            .options(joinedload(Book.genre))
            .order_by(Book.title)
        )
        if limit:
            query = query.limit(limit)
        books = query.all()
        for book in books:
            _ = book.genre
        session.expunge_all()
        return books


@st.cache_data(ttl=CACHE_TTL)
def get_books_count() -> int:
    """
    Get total number of books. (Cached)
    
    Returns:
        int: Total book count
    """
    with get_db_session() as session:
        return session.query(Book).count()


@st.cache_data(ttl=CACHE_TTL)
def get_genres_count() -> int:
    """
    Get total number of genres. (Cached)
    
    Returns:
        int: Total genre count
    """
    with get_db_session() as session:
        return session.query(Genre).count()


@st.cache_data(ttl=CACHE_TTL)
def get_summaries_count() -> int:
    """
    Get total number of summaries. (Cached)
    
    Returns:
        int: Total summary count
    """
    with get_db_session() as session:
        return session.query(Summary).count()


def get_random_book() -> Optional[Book]:
    """
    Get a random book from the database.
    
    Returns:
        Optional[Book]: A random book with genre loaded
    """
    import random
    with get_db_session() as session:
        # Get total count
        count = session.query(Book).count()
        if count == 0:
            return None
        # Get random offset
        random_offset = random.randint(0, count - 1)
        book = (
            session.query(Book)
            .options(joinedload(Book.genre))
            .offset(random_offset)
            .limit(1)
            .first()
        )
        if book:
            _ = book.genre  # Access before expunge
            session.expunge_all()
        return book


def get_top_rated_books(limit: int = 6) -> List[Book]:
    """
    Get top-rated books based on summary rating.
    
    Args:
        limit: Maximum number of books to return
    
    Returns:
        List[Book]: Top-rated books with genres loaded
    """
    with get_db_session() as session:
        books = (
            session.query(Book)
            .join(Summary)
            .options(joinedload(Book.genre))
            .order_by(Summary.rating.desc(), Book.title)
            .limit(limit)
            .all()
        )
        for book in books:
            _ = book.genre
        session.expunge_all()
        return books


def get_recent_books(limit: int = 6) -> List[Book]:
    """
    Get most recently added books.
    
    Args:
        limit: Maximum number of books to return
    
    Returns:
        List[Book]: Recent books with genres loaded
    """
    with get_db_session() as session:
        books = (
            session.query(Book)
            .options(joinedload(Book.genre))
            .order_by(Book.created_at.desc())
            .limit(limit)
            .all()
        )
        for book in books:
            _ = book.genre
        session.expunge_all()
        return books

