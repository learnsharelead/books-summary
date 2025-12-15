"""
About Page - Compact with readable fonts
"""

import streamlit as st
from database.queries import get_books_count, get_genres_count
from components.navigation import render_navigation
from components.footer import render_footer

st.set_page_config(page_title="About | BookWise", page_icon="ℹ️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
body {font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b;}
div.stButton > button {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 6px; padding: 8px 16px; font-size: 13px; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

render_navigation(active_page="About")
book_count = get_books_count()
genre_count = get_genres_count()

# Hero
st.markdown(f'<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"><div style="max-width: 1200px; margin: 0 auto; padding: 32px 20px; text-align: center;"><div style="font-size: 42px; margin-bottom: 10px;">ℹ️</div><h1 style="font-size: 28px; font-weight: 900; color: white; margin-bottom: 8px;">About BookWise</h1><p style="font-size: 14px; color: rgba(255, 255, 255, 0.9);">Making book knowledge accessible through curated summaries</p></div></div>', unsafe_allow_html=True)

# Stats
st.markdown('<div style="max-width: 1200px; margin: -20px auto 0 auto; padding: 0 20px; position: relative; z-index: 10;">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4, gap="small")
with col1:
    st.markdown(f'<div style="background: white; padding: 16px; border-radius: 10px; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);"><div style="font-size: 24px;">📖</div><div style="font-size: 24px; font-weight: 800; color: #667eea;">{book_count:,}+</div><div style="font-size: 12px; color: #64748b;">Books</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div style="background: white; padding: 16px; border-radius: 10px; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);"><div style="font-size: 24px;">📚</div><div style="font-size: 24px; font-weight: 800; color: #f093fb;">{genre_count}</div><div style="font-size: 12px; color: #64748b;">Genres</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div style="background: white; padding: 16px; border-radius: 10px; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);"><div style="font-size: 24px;">⏱️</div><div style="font-size: 24px; font-weight: 800; color: #43e97b;">{book_count * 5:,}+</div><div style="font-size: 12px; color: #64748b;">Hours Saved</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div style="background: white; padding: 16px; border-radius: 10px; text-align: center; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);"><div style="font-size: 24px;">✍️</div><div style="font-size: 24px; font-weight: 800; color: #fa709a;">100%</div><div style="font-size: 12px; color: #64748b;">Expert Written</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Mission
st.markdown('<div style="max-width: 800px; margin: 24px auto; padding: 0 20px;"><div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);"><h3 style="font-size: 18px; font-weight: 800; color: #1e293b; margin-bottom: 10px;">🎯 Our Mission</h3><p style="font-size: 14px; line-height: 1.7; color: #475569;">We believe knowledge should be accessible to everyone. BookWise provides expert-curated summaries of influential books, distilling hours of reading into 15-minute insights you can apply immediately.</p></div></div>', unsafe_allow_html=True)

# Features
st.markdown('<div style="max-width: 1200px; margin: 20px auto; padding: 0 20px;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 12px; color: white; text-align: center; min-height: 120px;"><div style="font-size: 32px; margin-bottom: 8px;">🎓</div><div style="font-size: 15px; font-weight: 700; margin-bottom: 6px;">Expert Curation</div><p style="font-size: 12px; opacity: 0.9;">Crafted by subject matter experts</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 12px; color: white; text-align: center; min-height: 120px;"><div style="font-size: 32px; margin-bottom: 8px;">🚀</div><div style="font-size: 15px; font-weight: 700; margin-bottom: 6px;">Action-Focused</div><p style="font-size: 12px; opacity: 0.9;">Frameworks to apply immediately</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); padding: 20px; border-radius: 12px; color: white; text-align: center; min-height: 120px;"><div style="font-size: 32px; margin-bottom: 8px;">📊</div><div style="font-size: 15px; font-weight: 700; margin-bottom: 6px;">Visual Learning</div><p style="font-size: 12px; opacity: 0.9;">Diagrams for key concepts</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# CTA
st.markdown('<div style="max-width: 1200px; margin: 20px auto; padding: 0 20px;"><div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 28px; border-radius: 14px; text-align: center;"><h3 style="font-size: 22px; font-weight: 800; color: white; margin-bottom: 8px;">Ready to Start?</h3><p style="font-size: 14px; color: rgba(255, 255, 255, 0.9);">Explore our library today.</p></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.link_button("📚 Browse Books", "/Categories", use_container_width=True)

st.markdown('<div style="text-align: center; padding: 16px;"><p style="font-size: 13px; color: #64748b;">Questions? hello@bookwise.app</p></div>', unsafe_allow_html=True)

render_footer()
