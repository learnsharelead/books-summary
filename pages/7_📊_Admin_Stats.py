"""
Admin Stats - Compact with readable fonts
"""

import streamlit as st
from datetime import datetime
from database.queries import get_books_count, get_genres_count, get_summaries_count, get_all_genres, get_all_books
from components.navigation import render_navigation
from components.footer import render_footer

st.set_page_config(page_title="Admin | BookWise", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
body {font-family: 'Inter', sans-serif; background: #f8fafc;}
</style>
""", unsafe_allow_html=True)

render_navigation()

st.markdown('<div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%);"><div style="max-width: 1200px; margin: 0 auto; padding: 24px 20px; text-align: center;"><div style="font-size: 32px; margin-bottom: 6px;">📊</div><h1 style="font-size: 22px; font-weight: 900; color: white;">Admin Dashboard</h1></div></div>', unsafe_allow_html=True)

book_count = get_books_count()
genre_count = get_genres_count()
summary_count = get_summaries_count()
genres = get_all_genres()
books = get_all_books()

# Metrics
st.markdown('<div style="max-width: 1200px; margin: -16px auto 0 auto; padding: 0 20px; position: relative; z-index: 10;">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4, gap="small")
with col1:
    st.markdown(f'<div style="background: white; padding: 14px; border-radius: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);"><div style="font-size: 28px; font-weight: 800; color: #667eea;">{book_count:,}</div><div style="font-size: 12px; color: #64748b;">Books</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div style="background: white; padding: 14px; border-radius: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);"><div style="font-size: 28px; font-weight: 800; color: #f093fb;">{genre_count}</div><div style="font-size: 12px; color: #64748b;">Genres</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div style="background: white; padding: 14px; border-radius: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);"><div style="font-size: 28px; font-weight: 800; color: #43e97b;">{summary_count:,}</div><div style="font-size: 12px; color: #64748b;">Summaries</div></div>', unsafe_allow_html=True)
with col4:
    avg = book_count // genre_count if genre_count > 0 else 0
    st.markdown(f'<div style="background: white; padding: 14px; border-radius: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);"><div style="font-size: 28px; font-weight: 800; color: #fa709a;">{avg}</div><div style="font-size: 12px; color: #64748b;">Avg/Genre</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Genre Distribution
st.markdown('<div style="max-width: 1200px; margin: 20px auto; padding: 0 20px;"><h3 style="font-size: 16px; font-weight: 800; color: #1e293b; margin-bottom: 12px;">📊 Genre Distribution</h3>', unsafe_allow_html=True)

genre_stats = sorted([{"name": g.name, "icon": g.icon, "count": len([b for b in books if b.genre_id == g.id]), "pct": (len([b for b in books if b.genre_id == g.id]) / book_count * 100) if book_count > 0 else 0} for g in genres], key=lambda x: x["count"], reverse=True)

for g in genre_stats[:5]:
    st.markdown(f'<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;"><span style="font-size: 18px;">{g["icon"]}</span><span style="font-size: 13px; font-weight: 600; width: 90px;">{g["name"]}</span><div style="flex-grow: 1; background: #e2e8f0; border-radius: 6px; height: 18px; overflow: hidden;"><div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: {g["pct"]}%; height: 100%;"></div></div><span style="font-size: 12px; color: #64748b; width: 40px;">{g["count"]}</span></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# System Info
st.markdown(f'<div style="max-width: 1200px; margin: 16px auto; padding: 0 20px;"><div style="background: white; padding: 16px; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); font-size: 13px;"><div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #f1f5f9;"><span style="color: #64748b;">Last Updated</span><span>{datetime.now().strftime("%Y-%m-%d %H:%M")}</span></div><div style="display: flex; justify-content: space-between; padding: 6px 0;"><span style="color: #64748b;">Sitemap URLs</span><span>{5 + genre_count + book_count}</span></div></div></div>', unsafe_allow_html=True)

render_footer()
