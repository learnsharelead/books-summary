"""
BookWise - Compact Homepage with Readable Fonts
"""

import streamlit as st
from database.queries import get_featured_books, get_all_genres, search_books, get_top_rated_books, get_books_by_genre
from components.image_handler import load_image_safe
from components.navigation import render_navigation
from components.footer import render_footer
from components.reading_lists import READING_LISTS
from components.book_of_day import render_book_of_the_day
from components.testimonials import render_stats_with_social_proof

@st.cache_data(ttl=300)
def get_genre_book_counts():
    genres = get_all_genres()
    return {g.slug: len(get_books_by_genre(g.slug)) for g in genres}

st.set_page_config(page_title="BookWise", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
body {font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b;}
div.stButton > button {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 600; transition: all 0.2s ease;}
div.stButton > button:hover {transform: translateY(-1px);}
input[type="text"] {border: 1px solid #e2e8f0 !important; border-radius: 8px !important; padding: 8px 12px !important; font-size: 14px !important;}
.hover-lift {transition: all 0.2s ease;}
.hover-lift:hover {transform: translateY(-3px); box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);}
</style>
""", unsafe_allow_html=True)

render_navigation(active_page="Home")

# Compact Hero with readable fonts
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
<div style="max-width: 1200px; margin: 0 auto; padding: 28px 20px; text-align: center;">
<h1 style="font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 900; color: white; margin-bottom: 8px; line-height: 1.2;">
Transform Your Life, <span style="color: #e0e7ff;">One Book at a Time</span>
</h1>
<p style="font-size: 14px; color: rgba(255, 255, 255, 0.9);">Master influential books in 15 minutes • Expert summaries • Actionable insights</p>
</div>
</div>
""", unsafe_allow_html=True)

# Search
st.markdown('<div style="max-width: 900px; margin: -16px auto 16px auto; padding: 0 20px; position: relative; z-index: 10;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<div style="background: white; padding: 6px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">', unsafe_allow_html=True)
    search_query = st.text_input("Search", placeholder="🔍 Search books...", label_visibility="collapsed", key="home_search")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if search_query and len(search_query) >= 2:
    results = search_books(search_query, limit=12)
    if results:
        st.markdown(f'<div style="max-width: 1200px; margin: 0 auto; padding: 12px 20px;"><h3 style="font-size: 18px; font-weight: 700; color: #1e293b;">🔍 "{search_query}" ({len(results)} found)</h3></div>', unsafe_allow_html=True)
        cols = st.columns(6, gap="small")
        for idx, book in enumerate(results):
            with cols[idx % 6]:
                safe_image_url = load_image_safe(book.cover_image_url, "book")
                st.markdown(f'<div class="hover-lift" style="background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08); margin-bottom: 10px;"><div style="position: relative; padding-top: 140%; background: #f8fafc;"><img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;"></div><div style="padding: 10px;"><h4 style="font-size: 13px; font-weight: 700; color: #1e293b; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; margin: 0;">{book.title}</h4><p style="font-size: 11px; color: #64748b; margin: 4px 0 0 0;">{book.author}</p></div></div>', unsafe_allow_html=True)
                st.link_button("Read", f"Book_Detail?slug={book.slug}", use_container_width=True)
    else:
        st.info(f'No books found for "{search_query}"')
else:
    # Featured Books
    st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;"><h3 style="font-size: 20px; font-weight: 800; color: #1e293b; margin-bottom: 12px;">✨ Featured</h3>', unsafe_allow_html=True)
    featured = get_featured_books(limit=6)
    cols = st.columns(6, gap="small")
    for idx, book in enumerate(featured):
        with cols[idx]:
            safe_image_url = load_image_safe(book.cover_image_url, "book")
            st.markdown(f'<div class="hover-lift" style="background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);"><div style="position: relative; padding-top: 140%; background: #f8fafc;"><img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;"></div><div style="padding: 10px;"><h4 style="font-size: 13px; font-weight: 700; color: #1e293b; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; margin: 0;">{book.title}</h4><p style="font-size: 11px; color: #64748b; margin: 4px 0 0 0;">{book.author}</p></div></div>', unsafe_allow_html=True)
            st.link_button("Read", f"Book_Detail?slug={book.slug}", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Categories - Compact Grid
    st.markdown('<div style="background: #f8fafc; padding: 20px 0; margin-top: 16px;"><div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;"><h3 style="font-size: 20px; font-weight: 800; color: #1e293b; margin-bottom: 16px; text-align: center;">🎯 Categories</h3>', unsafe_allow_html=True)
    
    genres = get_all_genres()
    colors = {"self-help": "#667eea", "business": "#f093fb", "psychology": "#4facfe", "finance": "#43e97b", "productivity": "#fa709a", "philosophy": "#30cfd0", "history": "#a8edea", "science": "#ff9a9e", "biography": "#ffecd2", "technology": "#ff6e7f"}
    book_counts = get_genre_book_counts()
    
    cols = st.columns(5, gap="small")
    for idx, genre in enumerate(genres[:5]):
        color = colors.get(genre.slug, "#667eea")
        book_count = book_counts.get(genre.slug, 0)
        with cols[idx]:
            st.markdown(f'<div class="hover-lift" style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%); border-radius: 10px; padding: 16px 10px; text-align: center; color: white; min-height: 100px;"><div style="font-size: 28px; margin-bottom: 6px;">{genre.icon}</div><div style="font-size: 13px; font-weight: 700;">{genre.name}</div><div style="font-size: 11px; opacity: 0.9;">{book_count} books</div></div>', unsafe_allow_html=True)
            st.link_button("Explore", f"/Categories?name={genre.slug}", use_container_width=True)
    
    if len(genres) > 5:
        cols2 = st.columns(5, gap="small")
        for idx, genre in enumerate(genres[5:10]):
            color = colors.get(genre.slug, "#667eea")
            book_count = book_counts.get(genre.slug, 0)
            with cols2[idx]:
                st.markdown(f'<div class="hover-lift" style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%); border-radius: 10px; padding: 16px 10px; text-align: center; color: white; min-height: 100px;"><div style="font-size: 28px; margin-bottom: 6px;">{genre.icon}</div><div style="font-size: 13px; font-weight: 700;">{genre.name}</div><div style="font-size: 11px; opacity: 0.9;">{book_count} books</div></div>', unsafe_allow_html=True)
                st.link_button("Explore", f"/Categories?name={genre.slug}", use_container_width=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

    # Reading Lists Preview
    st.markdown('<div style="max-width: 1200px; margin: 16px auto; padding: 0 20px;"><h3 style="font-size: 20px; font-weight: 800; color: #1e293b; margin-bottom: 12px;">📋 Reading Lists</h3>', unsafe_allow_html=True)
    list_keys = list(READING_LISTS.keys())[:3]
    cols_lists = st.columns(3, gap="small")
    for idx, list_id in enumerate(list_keys):
        rl = READING_LISTS[list_id]
        with cols_lists[idx]:
            st.markdown(f'<div class="hover-lift" style="background: {rl["color"]}; border-radius: 10px; padding: 16px; text-align: center; min-height: 100px;"><div style="font-size: 32px; margin-bottom: 6px;">{rl["icon"]}</div><div style="font-size: 14px; font-weight: 700; color: white;">{rl["title"]}</div><div style="font-size: 11px; color: rgba(255,255,255,0.8);">{len(rl["books"])} books</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Book of the Day & Stats
st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    render_book_of_the_day()
st.markdown('</div>', unsafe_allow_html=True)

render_stats_with_social_proof()
render_footer()
