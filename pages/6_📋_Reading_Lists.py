"""
Reading Lists - Compact with readable fonts
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer
from components.reading_lists import render_reading_lists_section

st.set_page_config(page_title="Reading Lists | BookWise", page_icon="📋", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
body {font-family: 'Inter', sans-serif; background: #f8fafc;}
div.stButton > button {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

render_navigation()

if "selected_list" not in st.session_state:
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"><div style="max-width: 1200px; margin: 0 auto; padding: 28px 20px; text-align: center;"><div style="font-size: 40px; margin-bottom: 8px;">📋</div><h1 style="font-size: 24px; font-weight: 900; color: white;">Reading Lists</h1><p style="font-size: 14px; color: rgba(255, 255, 255, 0.9);">Expert-curated collections to accelerate your growth</p></div></div>', unsafe_allow_html=True)

render_reading_lists_section()
render_footer()
