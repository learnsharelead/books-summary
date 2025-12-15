"""
Discovery components - Ultra Compact
"""

import streamlit as st
import urllib.parse
from typing import Optional
from database.queries import get_random_book
from components.image_handler import load_image_safe


def render_random_book_button() -> None:
    """Render ultra-compact random book button."""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 10px; padding: 12px; text-align: center;">
    <div style="font-size: 24px; margin-bottom: 4px;">🎲</div>
    <h4 style="color: white; font-size: 12px; font-weight: 700; margin-bottom: 4px;">Feeling Adventurous?</h4>
    <p style="color: rgba(255,255,255,0.9); font-size: 9px;">Random book pick</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎲 Surprise Me!", key="random_book_btn", use_container_width=True):
        book = get_random_book()
        if book:
            st.session_state["random_book"] = book
            st.rerun()
    
    if "random_book" in st.session_state:
        book = st.session_state["random_book"]
        safe_image_url = load_image_safe(book.cover_image_url, "book")
        genre_name = book.genre.name if book.genre else "Unknown"
        
        st.markdown(f"""
        <div style="background: white; border-radius: 8px; padding: 10px; margin-top: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); display: flex; gap: 10px; align-items: center;">
        <img src="{safe_image_url}" style="width: 50px; height: 70px; object-fit: cover; border-radius: 4px;">
        <div>
        <h5 style="font-size: 10px; font-weight: 700; color: #1e293b; margin: 0; line-height: 1.2;">{book.title[:30]}{'...' if len(book.title) > 30 else ''}</h5>
        <p style="font-size: 8px; color: #64748b; margin: 2px 0;">{book.author}</p>
        <span style="font-size: 8px; background: #e2e8f0; padding: 1px 4px; border-radius: 6px; color: #475569;">📚 {genre_name}</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Read", f"/Book_Detail?slug={book.slug}", use_container_width=True)
        with col2:
            if st.button("🔄 Again", key="try_again_btn", use_container_width=True):
                del st.session_state["random_book"]
                st.rerun()


def render_compact_share_buttons(title: str, url: str) -> None:
    """Render ultra-compact share buttons."""
    encoded_title = urllib.parse.quote(title)
    encoded_url = urllib.parse.quote(url)
    
    twitter_url = f"https://twitter.com/intent/tweet?text={encoded_title}&url={encoded_url}"
    linkedin_url = f"https://www.linkedin.com/shareArticle?mini=true&url={encoded_url}&title={encoded_title}"
    whatsapp_url = f"https://wa.me/?text={encoded_title}%20{encoded_url}"
    
    st.markdown(f"""
    <div style="display: flex; gap: 6px; align-items: center;">
    <span style="font-size: 10px; color: #64748b;">Share:</span>
    <a href="{twitter_url}" target="_blank" style="display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; background: #1DA1F2; color: white; border-radius: 50%; text-decoration: none; font-size: 10px;">𝕏</a>
    <a href="{linkedin_url}" target="_blank" style="display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; background: #0A66C2; color: white; border-radius: 50%; text-decoration: none; font-size: 10px; font-weight: 700;">in</a>
    <a href="{whatsapp_url}" target="_blank" style="display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; background: #25D366; color: white; border-radius: 50%; text-decoration: none; font-size: 10px;">📱</a>
    </div>
    """, unsafe_allow_html=True)


def render_social_share_buttons(title: str, url: str, description: Optional[str] = None) -> None:
    """Alias for compact share buttons."""
    render_compact_share_buttons(title, url)


def add_bookmark(book_slug: str, title: str, author: str) -> None:
    """Add a book to session bookmarks."""
    if "bookmarks" not in st.session_state:
        st.session_state["bookmarks"] = []
    for b in st.session_state["bookmarks"]:
        if b["slug"] == book_slug:
            return
    st.session_state["bookmarks"].append({"slug": book_slug, "title": title, "author": author})


def remove_bookmark(book_slug: str) -> None:
    """Remove a book from session bookmarks."""
    if "bookmarks" not in st.session_state:
        return
    st.session_state["bookmarks"] = [b for b in st.session_state["bookmarks"] if b["slug"] != book_slug]


def is_bookmarked(book_slug: str) -> bool:
    """Check if a book is bookmarked."""
    if "bookmarks" not in st.session_state:
        return False
    return any(b["slug"] == book_slug for b in st.session_state["bookmarks"])


def render_bookmarks_sidebar() -> None:
    """Render bookmarks in sidebar."""
    if "bookmarks" not in st.session_state:
        st.session_state["bookmarks"] = []
    bookmarks = st.session_state["bookmarks"]
    st.sidebar.markdown("### 🔖 Bookmarks")
    if not bookmarks:
        st.sidebar.info("No bookmarks yet")
    else:
        for book in bookmarks[:5]:
            st.sidebar.markdown(f'<div style="font-size: 10px; padding: 4px 0;"><a href="/Book_Detail?slug={book["slug"]}" style="color: #1e293b;">{book["title"][:25]}</a></div>', unsafe_allow_html=True)
