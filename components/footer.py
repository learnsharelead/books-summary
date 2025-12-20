"""
Shared footer - Theme-aware with dark mode support
"""

import streamlit as st
from datetime import datetime
from components.theme import get_theme, get_theme_colors, COLORS


def render_footer(compact: bool = True) -> None:
    """Render theme-aware footer."""
    current_year = datetime.now().year
    theme = get_theme()
    c = get_theme_colors()
    
    # Footer uses inverted colors for visual separation
    if theme == "light":
        bg_color = "#1e293b"
        text_color = "white"
        link_color = "#94a3b8"
        muted_color = "#64748b"
    else:
        bg_color = c['surface']
        text_color = c['text_primary']
        link_color = c['text_secondary']
        muted_color = c['text_muted']
    
    footer_html = f"""
    <div style="background: {bg_color}; color: {text_color}; padding: 20px 0; margin-top: 24px; border-top: 1px solid {c['border']};">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
    <div style="display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 20px;">📚</span>
    <span style="font-size: 16px; font-weight: 700;"">BookWise</span>
    </div>
    <div style="display: flex; gap: 20px; font-size: 13px;">
    <a href="/" style="color: {link_color}; text-decoration: none;">Home</a>
    <a href="/Categories" style="color: {link_color}; text-decoration: none;">Categories</a>
    <a href="/AI_Features" style="color: {link_color}; text-decoration: none;">🤖 AI</a>
    <a href="/About" style="color: {link_color}; text-decoration: none;">About</a>
    <a href="/Privacy" style="color: {link_color}; text-decoration: none;">Privacy</a>
    <a href="/Terms" style="color: {link_color}; text-decoration: none;">Terms</a>
    </div>
    <div style="color: {muted_color}; font-size: 12px;">© {current_year} BookWise</div>
    </div>
    </div>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)
