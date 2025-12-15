"""
Shared footer - Compact with readable fonts
"""

import streamlit as st
from datetime import datetime


def render_footer(compact: bool = True) -> None:
    """Render compact footer with readable fonts."""
    current_year = datetime.now().year
    
    footer_html = f"""
    <div style="background: #1e293b; color: white; padding: 20px 0; margin-top: 24px;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
    <div style="display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 20px;">📚</span>
    <span style="font-size: 16px; font-weight: 700;">BookWise</span>
    </div>
    <div style="display: flex; gap: 20px; font-size: 13px; color: #94a3b8;">
    <a href="/" style="color: #94a3b8; text-decoration: none;">Home</a>
    <a href="/Categories" style="color: #94a3b8; text-decoration: none;">Categories</a>
    <a href="/About" style="color: #94a3b8; text-decoration: none;">About</a>
    <a href="/Privacy" style="color: #94a3b8; text-decoration: none;">Privacy</a>
    <a href="/Terms" style="color: #94a3b8; text-decoration: none;">Terms</a>
    </div>
    <div style="color: #64748b; font-size: 12px;">© {current_year} BookWise</div>
    </div>
    </div>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)
