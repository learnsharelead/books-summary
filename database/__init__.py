"""
Database package for BookWise.
Provides SQLAlchemy models, connection management, and query utilities.
"""

from database.models import Genre, Book, Summary, SummaryImage
from database.connection import get_db_session, init_db
from database.queries import (
    get_all_genres,
    get_genre_by_slug,
    get_books_by_genre,
    get_book_by_slug,
    get_summary_for_book,
    get_images_for_summary,
    get_featured_books,
    search_books,
    get_all_books,
)

__all__ = [
    "Genre",
    "Book",
    "Summary",
    "SummaryImage",
    "get_db_session",
    "init_db",
    "get_all_genres",
    "get_genre_by_slug",
    "get_books_by_genre",
    "get_book_by_slug",
    "get_summary_for_book",
    "get_images_for_summary",
    "get_featured_books",
    "search_books",
    "get_all_books",
]
