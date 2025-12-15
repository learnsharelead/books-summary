"""
Book of the Day - Compact with readable fonts
"""

import streamlit as st
from datetime import datetime
from database.queries import get_all_books
from components.image_handler import load_image_safe


def get_book_of_the_day():
    """Get the book of the day based on current date."""
    books = get_all_books()
    if not books:
        return None
    today = datetime.now()
    day_seed = today.year * 1000 + today.timetuple().tm_yday
    return books[day_seed % len(books)]


def render_book_of_the_day() -> None:
    """Render compact Book of the Day with readable fonts."""
    book = get_book_of_the_day()
    if not book:
        return
    
    safe_image_url = load_image_safe(book.cover_image_url, "book")
    genre_name = book.genre.name if book.genre else "Unknown"
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 20px; margin: 16px 0; display: flex; gap: 20px; align-items: center;">
    <div style="flex-shrink: 0; position: relative;">
    <img src="{safe_image_url}" style="width: 80px; height: 120px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <div style="position: absolute; top: -8px; right: -8px; background: #fef3c7; padding: 3px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; color: #92400e;">⭐ Today</div>
    </div>
    <div style="flex-grow: 1; color: white;">
    <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.8; margin-bottom: 6px;">📅 {datetime.now().strftime("%B %d")}</div>
    <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 6px; line-height: 1.2; color: white;">{book.title[:50]}{'...' if len(book.title) > 50 else ''}</h3>
    <p style="font-size: 13px; opacity: 0.9; margin-bottom: 10px; color: white;">by {book.author}</p>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
    <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 12px; font-size: 11px;">{genre_name}</span>
    <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 12px; font-size: 11px;">⏱️ 15 min</span>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("📖 Read Today's Pick", f"/Book_Detail?slug={book.slug}", use_container_width=True)


def render_compact_book_of_day() -> None:
    """Alias for compatibility."""
    render_book_of_the_day()
