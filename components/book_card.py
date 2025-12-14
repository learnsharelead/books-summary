"""
Book card components for BookWise.
Renders book cards and grids with cover images.
"""

import streamlit as st
from typing import List, Any


def render_book_card(book: Any, show_genre: bool = False) -> None:
    """
    Render a single book card with cover image.
    
    Args:
        book: Book model instance
        show_genre: Whether to show genre badge
    """
    cover_url = book.cover_image_url or "https://via.placeholder.com/300x450?text=No+Cover"
    
    card_html = f"""
    <div class="book-card" onclick="window.location.href='/Book_Detail?slug={book.slug}';" style="cursor:pointer;">
        <img src="{cover_url}" alt="{book.title} cover" class="book-cover" 
             onerror="this.src='https://via.placeholder.com/300x450?text=No+Cover'">
        <h3 class="book-title">{book.title}</h3>
        <p class="book-author">by {book.author}</p>
        {"<span class='badge badge-primary'>" + book.genre.name + "</span>" if show_genre and hasattr(book, 'genre') and book.genre else ""}
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Add navigation button
    if st.button("Read Summary", key=f"btn_{book.slug}", use_container_width=True):
        st.query_params["slug"] = book.slug
        st.switch_page("pages/2_📚_Book_Detail.py")


def render_book_grid(books: List[Any], columns: int = 4, show_genre: bool = False) -> None:
    """
    Render a grid of book cards.
    
    Args:
        books: List of Book model instances
        columns: Number of columns in the grid
        show_genre: Whether to show genre badges
    """
    if not books:
        st.info("No books found in this category.")
        return
    
    cols = st.columns(columns)
    for idx, book in enumerate(books):
        with cols[idx % columns]:
            render_book_card_simple(book, show_genre)


def render_book_card_simple(book: Any, show_genre: bool = False) -> None:
    """Render a simplified book card."""
    cover_url = book.cover_image_url or "https://via.placeholder.com/300x450?text=No+Cover"
    
    with st.container():
        st.image(cover_url, use_container_width=True)
        st.markdown(f"**{book.title}**")
        st.caption(f"by {book.author}")
        if show_genre and hasattr(book, 'genre') and book.genre:
            st.caption(f"📚 {book.genre.name}")
        if st.button("Read Summary", key=f"read_{book.slug}"):
            st.query_params["slug"] = book.slug
            st.switch_page("pages/2_📚_Book_Detail.py")
        st.markdown("---")
