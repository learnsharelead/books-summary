"""
Shared navigation - Compact with dark mode toggle
"""

import streamlit as st
from database.queries import get_books_count
from components.theme import get_theme, toggle_theme, get_theme_colors, COLORS


def render_navigation(active_page: str = "Home", compact: bool = True, show_theme_toggle: bool = True) -> None:
    """Render compact navigation with readable fonts and dark mode toggle."""
    book_count = get_books_count()
    theme = get_theme()
    c = get_theme_colors()
    
    def get_link_style(page: str) -> str:
        if page == active_page:
            return f"font-weight: 600; color: {COLORS['primary']};"
        return f"font-weight: 500; color: {c['text_secondary']};"
    
    # Theme toggle icon
    theme_icon = "🌙" if theme == "light" else "☀️"
    theme_label = "Dark" if theme == "light" else "Light"
    
    nav_html = f"""
    <div style="background: {c['surface']}; border-bottom: 1px solid {c['border']}; position: sticky; top: 0; z-index: 1000;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; height: 50px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 22px;">📚</span>
    <a href="/" style="font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 800; background: {COLORS['primary_gradient']}; -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none;">BookWise</a>
    </div>
    <div style="display: flex; gap: 24px; align-items: center;">
    <a href="/" style="font-size: 14px; {get_link_style('Home')} text-decoration: none;">Home</a>
    <a href="/Categories" style="font-size: 14px; {get_link_style('Categories')} text-decoration: none;">Categories</a>
    <a href="/AI_Features" style="font-size: 14px; {get_link_style('AI Features')} text-decoration: none; display: flex; align-items: center; gap: 4px;">🤖 AI<span style="background: {COLORS['success_gradient']}; color: white; font-size: 9px; padding: 2px 6px; border-radius: 8px; font-weight: 600;">NEW</span></a>
    <a href="/About" style="font-size: 14px; {get_link_style('About')} text-decoration: none;">About</a>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
    <div style="background: {COLORS['accent_gradient']}; padding: 4px 10px; border-radius: 14px; font-size: 11px; font-weight: 700; color: white;">
    ✨ {book_count:,}+ Books
    </div>
    </div>
    </div>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)
    
    # Theme toggle button (Streamlit native for interactivity)
    if show_theme_toggle:
        # Position in top right using columns hack
        _, col_toggle = st.columns([20, 1])
        with col_toggle:
            if st.button(theme_icon, key="nav_theme_toggle", help=f"Switch to {theme_label} mode"):
                toggle_theme()
                st.rerun()


def render_breadcrumb(items: list) -> None:
    """Render breadcrumb navigation."""
    c = get_theme_colors()
    crumbs = []
    for i, item in enumerate(items):
        if i < len(items) - 1:
            crumbs.append(f'<a href="{item["url"]}" style="color: {c["text_secondary"]}; text-decoration: none; font-size: 13px;">{item["label"]}</a>')
        else:
            crumbs.append(f'<span style="color: {c["text_primary"]}; font-weight: 600; font-size: 13px;">{item["label"]}</span>')
    
    st.markdown(f'<div style="max-width: 1200px; margin: 0 auto; padding: 10px 20px;"><div style="color: {c["text_secondary"]};">{" › ".join(crumbs)}</div></div>', unsafe_allow_html=True)
