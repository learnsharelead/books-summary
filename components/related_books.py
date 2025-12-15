"""
Related books component for BookWise.
Shows similar books based on genre and other factors.
"""

import streamlit as st
from typing import List, Optional
from database.queries import get_books_by_genre
from database.models import Book
from components.image_handler import load_image_safe


def get_related_books(
    current_book: Book,
    limit: int = 5
) -> List[Book]:
    """
    Get related books based on genre.
    
    Args:
        current_book: The current book being viewed
        limit: Maximum number of related books
    
    Returns:
        List[Book]: Related books (excluding current)
    """
    if not current_book.genre:
        return []
    
    # Get books from same genre
    genre_slug = current_book.genre.slug
    all_books = get_books_by_genre(genre_slug, limit=limit + 5)
    
    # Exclude current book
    related = [b for b in all_books if b.id != current_book.id]
    
    return related[:limit]


def render_related_books(
    current_book: Book,
    limit: int = 5
) -> None:
    """
    Render related books section.
    
    Args:
        current_book: The current book being viewed
        limit: Maximum number of related books
    """
    related = get_related_books(current_book, limit)
    
    if not related:
        return
    
    genre_name = current_book.genre.name if current_book.genre else "Similar"
    
    st.markdown(f"""
    <div style="margin-top: 40px; padding-top: 40px; border-top: 1px solid #e2e8f0;">
    <h3 style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 800; 
               color: #1e293b; margin-bottom: 24px;">
    📚 More in {genre_name}
    </h3>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(5, gap="medium")
    
    for idx, book in enumerate(related):
        with cols[idx % 5]:
            safe_image_url = load_image_safe(book.cover_image_url, "book")
            
            st.markdown(f"""
            <div class="hover-lift" style="background: white; border-radius: 12px; 
                        overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                        margin-bottom: 12px;">
            <div style="position: relative; padding-top: 150%; background: #f8fafc;">
            <img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; 
                 width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div style="padding: 12px;">
            <h4 style="font-size: 12px; font-weight: 700; color: #1e293b; margin-bottom: 4px;
                       line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2;
                       -webkit-box-orient: vertical; overflow: hidden;">
            {book.title}
            </h4>
            <p style="font-size: 10px; color: #64748b;">{book.author}</p>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.link_button("Read", f"/Book_Detail?slug={book.slug}", use_container_width=True)


def render_more_from_author(
    current_book: Book,
    all_books: Optional[List[Book]] = None,
    limit: int = 4
) -> None:
    """
    Render more books from the same author.
    
    Args:
        current_book: The current book
        all_books: Optional pre-fetched list of all books
        limit: Maximum number of books to show
    """
    # This would require fetching books by author
    # For now, skip if not implemented
    pass


def render_you_might_also_like(
    current_book: Book,
    limit: int = 4
) -> None:
    """
    Render "You might also like" section with diverse recommendations.
    
    Args:
        current_book: The current book
        limit: Maximum number of recommendations
    """
    from database.queries import get_featured_books
    
    # Get featured books from different genres
    featured = get_featured_books(limit=limit + 2)
    
    # Exclude current book and same genre
    recommendations = [
        b for b in featured 
        if b.id != current_book.id and 
           (not current_book.genre or b.genre_id != current_book.genre_id)
    ][:limit]
    
    if not recommendations:
        return
    
    st.markdown("""
    <div style="margin-top: 32px; padding-top: 32px; border-top: 1px solid #e2e8f0;">
    <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 16px;">
    ✨ You Might Also Like
    </h4>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4, gap="medium")
    
    for idx, book in enumerate(recommendations):
        with cols[idx]:
            safe_image_url = load_image_safe(book.cover_image_url, "book")
            genre_name = book.genre.name if book.genre else ""
            
            st.markdown(f"""
            <div style="display: flex; gap: 12px; align-items: center; padding: 12px; 
                        background: #f8fafc; border-radius: 12px; margin-bottom: 8px;">
            <img src="{safe_image_url}" style="width: 50px; height: 75px; object-fit: cover; border-radius: 6px;">
            <div>
            <h5 style="font-size: 12px; font-weight: 600; color: #1e293b; margin-bottom: 2px; 
                       line-height: 1.3;">{book.title[:30]}...</h5>
            <p style="font-size: 10px; color: #64748b; margin-bottom: 2px;">{book.author}</p>
            <span style="font-size: 9px; background: #e2e8f0; padding: 2px 6px; border-radius: 8px;">
            {genre_name}
            </span>
            </div>
            </div>
            """, unsafe_allow_html=True)
