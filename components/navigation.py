"""
Shared navigation - Compact with readable fonts
"""

import streamlit as st
from database.queries import get_books_count


def render_navigation(active_page: str = "Home", compact: bool = True, show_theme_toggle: bool = False) -> None:
    """Render compact navigation with readable fonts."""
    book_count = get_books_count()
    
    def get_link_style(page: str) -> str:
        if page == active_page:
            return "font-weight: 600; color: #667eea;"
        return "font-weight: 500; color: #64748b;"
    
    nav_html = f"""
    <div style="background: rgba(255, 255, 255, 0.98); border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 1000;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; height: 50px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 22px;">📚</span>
    <a href="/" style="font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 800; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none;">BookWise</a>
    </div>
    <div style="display: flex; gap: 24px; align-items: center;">
    <a href="/" style="font-size: 14px; {get_link_style('Home')} text-decoration: none;">Home</a>
    <a href="/Categories" style="font-size: 14px; {get_link_style('Categories')} text-decoration: none;">Categories</a>
    <a href="/About" style="font-size: 14px; {get_link_style('About')} text-decoration: none;">About</a>
    </div>
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 4px 10px; border-radius: 14px; font-size: 11px; font-weight: 700; color: #92400e;">
    ✨ {book_count:,}+ Books
    </div>
    </div>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)


def render_breadcrumb(items: list) -> None:
    """Render breadcrumb navigation."""
    crumbs = []
    for i, item in enumerate(items):
        if i < len(items) - 1:
            crumbs.append(f'<a href="{item["url"]}" style="color: #64748b; text-decoration: none; font-size: 13px;">{item["label"]}</a>')
        else:
            crumbs.append(f'<span style="color: #1e293b; font-weight: 600; font-size: 13px;">{item["label"]}</span>')
    
    st.markdown(f'<div style="max-width: 1200px; margin: 0 auto; padding: 10px 20px;"><div style="color: #64748b;">{" › ".join(crumbs)}</div></div>', unsafe_allow_html=True)
