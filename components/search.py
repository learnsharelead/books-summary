"""
Search component for BookWise.
Provides search functionality across books.
"""

import streamlit as st
from typing import Optional, List
from database.queries import search_books, get_all_books
from components.image_handler import load_image_safe


def render_search_bar(placeholder: str = "🔍  Search book summaries...") -> Optional[str]:
    """
    Render the search bar with premium styling.
    
    Args:
        placeholder: Placeholder text for search input
        
    Returns:
        str: Search query if entered, None otherwise
    """
    st.markdown('''
    <div style="max-width: 1400px; margin: -30px auto 40px auto; padding: 0 32px; position: relative; z-index: 10;">
    ''', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('''
        <div style="background: white; padding: 8px; border-radius: 16px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
        ''', unsafe_allow_html=True)
        search_query = st.text_input(
            "Search",
            placeholder=placeholder,
            label_visibility="collapsed",
            key="main_search"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return search_query if search_query else None


def render_search_results(query: str, max_results: int = 12) -> None:
    """
    Render search results in a grid.
    
    Args:
        query: Search query string
        max_results: Maximum results to display
    """
    if not query or len(query) < 2:
        return
    
    results = search_books(query, limit=max_results)
    
    if not results:
        st.markdown(f"""
        <div style="max-width: 1400px; margin: 0 auto; padding: 40px 32px; text-align: center;">
        <div style="font-size: 48px; margin-bottom: 16px;">📚</div>
        <h3 style="font-size: 24px; color: #1e293b; margin-bottom: 8px;">No books found for "{query}"</h3>
        <p style="color: #64748b;">Try adjusting your search terms or browse our categories</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Search results header
    st.markdown(f"""
    <div style="max-width: 1400px; margin: 0 auto; padding: 20px 32px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
    <div>
    <h2 style="font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 800; color: #1e293b; margin-bottom: 4px;">
    🔍 Search Results for "{query}"
    </h2>
    <p style="font-size: 14px; color: #64748b;">{len(results)} book(s) found</p>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Results grid
    cols = st.columns(6, gap="medium")
    
    for idx, book in enumerate(results):
        with cols[idx % 6]:
            safe_image_url = load_image_safe(book.cover_image_url, "book")
            genre_name = book.genre.name if book.genre else "Unknown"
            
            st.markdown(f"""
            <div class="hover-lift" style="background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border: 1px solid #f1f5f9; margin-bottom: 16px;">
            <div style="position: relative; padding-top: 150%; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);">
            <img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div style="padding: 16px;">
            <h3 style="font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 4px; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{book.title}</h3>
            <p style="font-size: 12px; color: #64748b; margin-bottom: 4px;">{book.author}</p>
            <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px;">
            <span style="font-size: 11px; color: #94a3b8;">📚 {genre_name}</span>
            </div>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.link_button("Read Summary", f"/Book_Detail?slug={book.slug}", use_container_width=True)


def handle_search() -> bool:
    """
    Handle search logic. Returns True if search is active.
    
    Returns:
        bool: True if search query exists and results should be shown
    """
    query = st.session_state.get("main_search", "")
    if query and len(query) >= 2:
        render_search_results(query)
        return True
    return False
