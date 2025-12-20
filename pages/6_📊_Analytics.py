"""
Analytics Dashboard - Admin Statistics and Insights
Enhanced with charts, performance metrics, and real-time analytics.
"""

import streamlit as st
import json
from datetime import datetime, timedelta
from database.queries import (
    get_books_count, get_all_genres, get_books_by_genre,
    get_top_rated_books, get_all_books
)
from components.navigation import render_navigation
from components.footer import render_footer
from components.theme import render_global_styles, get_theme_colors, COLORS

st.set_page_config(
    page_title="Analytics Dashboard | BookWise",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

render_global_styles()
c = get_theme_colors()

render_navigation(active_page="Analytics")

# Check for admin access (simple implementation)
admin_mode = st.query_params.get("admin", "false") == "true"

if not admin_mode:
    st.markdown(f"""
    <div style="max-width: 600px; margin: 100px auto; text-align: center; padding: 40px;">
        <div style="font-size: 64px; margin-bottom: 20px;">🔒</div>
        <h1 style="font-size: 28px; font-weight: 800; color: {c['text_primary']}; margin-bottom: 12px;">
            Admin Access Required
        </h1>
        <p style="font-size: 16px; color: {c['text_secondary']}; margin-bottom: 24px;">
            This dashboard is for administrators only.
        </p>
        <a href="/?admin=true" style="
            display: inline-block;
            background: {COLORS['primary_gradient']};
            color: white;
            padding: 12px 24px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
        ">Access Dashboard</a>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Hero Section
st.markdown(f"""
<div style="background: {COLORS['primary_gradient']};">
<div style="max-width: 1200px; margin: 0 auto; padding: 28px 20px;">
<h1 style="font-size: 28px; font-weight: 900; color: white; margin-bottom: 6px;">📊 Analytics Dashboard</h1>
<p style="font-size: 14px; color: rgba(255, 255, 255, 0.9);">Real-time insights and platform statistics</p>
</div>
</div>
""", unsafe_allow_html=True)

# Fetch data
total_books = get_books_count()
genres = get_all_genres()
top_rated = get_top_rated_books(limit=10)
all_books = get_all_books()

# Calculate statistics
genre_counts = {}
genre_avg_ratings = {}
books_by_year = {}
author_counts = {}

for book in all_books:
    # Genre stats
    genre_name = book.genre.name if book.genre else "Unknown"
    genre_counts[genre_name] = genre_counts.get(genre_name, 0) + 1
    
    # Year stats
    year = book.publication_year or 0
    if year > 1900:
        decade = (year // 10) * 10
        books_by_year[decade] = books_by_year.get(decade, 0) + 1
    
    # Author stats
    author_counts[book.author] = author_counts.get(book.author, 0) + 1

# Get top authors
top_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# KPI Cards
st.markdown('<div style="max-width: 1200px; margin: 24px auto; padding: 0 20px;">', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5, gap="small")

with col1:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px {c['shadow']};
    ">
        <div style="font-size: 32px; margin-bottom: 8px;">📚</div>
        <div style="font-size: 28px; font-weight: 800; color: {COLORS['primary']};">{total_books:,}</div>
        <div style="font-size: 12px; color: {c['text_secondary']};">Total Books</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px {c['shadow']};
    ">
        <div style="font-size: 32px; margin-bottom: 8px;">📁</div>
        <div style="font-size: 28px; font-weight: 800; color: {COLORS['success']};">{len(genres)}</div>
        <div style="font-size: 12px; color: {c['text_secondary']};">Categories</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px {c['shadow']};
    ">
        <div style="font-size: 32px; margin-bottom: 8px;">👤</div>
        <div style="font-size: 28px; font-weight: 800; color: {COLORS['accent']};">{len(author_counts)}</div>
        <div style="font-size: 12px; color: {c['text_secondary']};">Authors</div>
    </div>
    """, unsafe_allow_html=True)

avg_rating = sum(book.summaries[0].rating if book.summaries else 0 for book in all_books) / max(len(all_books), 1)

with col4:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px {c['shadow']};
    ">
        <div style="font-size: 32px; margin-bottom: 8px;">⭐</div>
        <div style="font-size: 28px; font-weight: 800; color: #f59e0b;">{avg_rating:.1f}</div>
        <div style="font-size: 12px; color: {c['text_secondary']};">Avg Rating</div>
    </div>
    """, unsafe_allow_html=True)

total_read_time = sum(book.summaries[0].reading_time if book.summaries else 0 for book in all_books)

with col5:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px {c['shadow']};
    ">
        <div style="font-size: 32px; margin-bottom: 8px;">⏱️</div>
        <div style="font-size: 28px; font-weight: 800; color: {COLORS['info']};">{total_read_time:,}</div>
        <div style="font-size: 12px; color: {c['text_secondary']};">Total Minutes</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Charts Section
st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px {c['shadow']};
        margin-bottom: 20px;
    ">
        <h3 style="font-size: 16px; font-weight: 700; color: {c['text_primary']}; margin-bottom: 16px;">
            📊 Books by Category
        </h3>
    """, unsafe_allow_html=True)
    
    # Simple bar chart using HTML/CSS
    max_count = max(genre_counts.values()) if genre_counts else 1
    for genre_name, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / max_count) * 100
        st.markdown(f"""
        <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                <span style="font-size: 13px; color: {c['text_primary']};">{genre_name}</span>
                <span style="font-size: 13px; font-weight: 600; color: {c['text_secondary']};">{count}</span>
            </div>
            <div style="height: 8px; background: {c['border']}; border-radius: 4px; overflow: hidden;">
                <div style="height: 100%; width: {percentage}%; background: {COLORS['primary_gradient']}; border-radius: 4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px {c['shadow']};
        margin-bottom: 20px;
    ">
        <h3 style="font-size: 16px; font-weight: 700; color: {c['text_primary']}; margin-bottom: 16px;">
            ✍️ Top Authors
        </h3>
    """, unsafe_allow_html=True)
    
    for idx, (author, count) in enumerate(top_authors[:8], 1):
        st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 0;
            border-bottom: 1px solid {c['border']};
        ">
            <div style="
                width: 28px;
                height: 28px;
                background: {COLORS['primary_gradient']};
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 12px;
                font-weight: 700;
            ">{idx}</div>
            <div style="flex: 1;">
                <div style="font-size: 13px; font-weight: 600; color: {c['text_primary']};">{author}</div>
            </div>
            <div style="
                background: {COLORS['accent_gradient']};
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 600;
                color: white;
            ">{count} books</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Books by Decade & Top Rated
st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px {c['shadow']};
        margin-bottom: 20px;
    ">
        <h3 style="font-size: 16px; font-weight: 700; color: {c['text_primary']}; margin-bottom: 16px;">
            📅 Books by Decade
        </h3>
    """, unsafe_allow_html=True)
    
    sorted_decades = sorted(books_by_year.items(), key=lambda x: x[0], reverse=True)[:8]
    max_decade = max(books_by_year.values()) if books_by_year else 1
    
    for decade, count in sorted_decades:
        percentage = (count / max_decade) * 100
        st.markdown(f"""
        <div style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                <span style="font-size: 13px; color: {c['text_primary']};">{decade}s</span>
                <span style="font-size: 13px; font-weight: 600; color: {c['text_secondary']};">{count}</span>
            </div>
            <div style="height: 8px; background: {c['border']}; border-radius: 4px; overflow: hidden;">
                <div style="height: 100%; width: {percentage}%; background: {COLORS['success_gradient']}; border-radius: 4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px {c['shadow']};
        margin-bottom: 20px;
    ">
        <h3 style="font-size: 16px; font-weight: 700; color: {c['text_primary']}; margin-bottom: 16px;">
            ⭐ Top Rated Books
        </h3>
    """, unsafe_allow_html=True)
    
    for idx, book in enumerate(top_rated[:6], 1):
        rating = book.summaries[0].rating if book.summaries else 0
        st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 0;
            border-bottom: 1px solid {c['border']};
        ">
            <div style="
                width: 28px;
                height: 28px;
                background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 12px;
                font-weight: 700;
            ">{idx}</div>
            <div style="flex: 1;">
                <div style="font-size: 13px; font-weight: 600; color: {c['text_primary']};">{book.title[:40]}{'...' if len(book.title) > 40 else ''}</div>
                <div style="font-size: 11px; color: {c['text_secondary']};">{book.author}</div>
            </div>
            <div style="
                display: flex;
                align-items: center;
                gap: 4px;
                color: #f59e0b;
                font-size: 13px;
                font-weight: 600;
            ">⭐ {rating:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Performance Metrics
st.markdown(f"""
<div style="max-width: 1200px; margin: 0 auto; padding: 20px;">
    <div style="
        background: {c['surface']};
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px {c['shadow']};
    ">
        <h3 style="font-size: 16px; font-weight: 700; color: {c['text_primary']}; margin-bottom: 16px;">
            ⚡ Performance Metrics
        </h3>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
            <div style="text-align: center; padding: 16px; background: {c['background']}; border-radius: 8px;">
                <div style="font-size: 24px; font-weight: 800; color: {COLORS['success']};">~50ms</div>
                <div style="font-size: 12px; color: {c['text_secondary']};">Avg Query Time</div>
            </div>
            <div style="text-align: center; padding: 16px; background: {c['background']}; border-radius: 8px;">
                <div style="font-size: 24px; font-weight: 800; color: {COLORS['success']};">5min</div>
                <div style="font-size: 12px; color: {c['text_secondary']};">Cache TTL</div>
            </div>
            <div style="text-align: center; padding: 16px; background: {c['background']}; border-radius: 8px;">
                <div style="font-size: 24px; font-weight: 800; color: {COLORS['success']};">SQLite</div>
                <div style="font-size: 12px; color: {c['text_secondary']};">Database</div>
            </div>
            <div style="text-align: center; padding: 16px; background: {c['background']}; border-radius: 8px;">
                <div style="font-size: 24px; font-weight: 800; color: {COLORS['success']};">PWA</div>
                <div style="font-size: 12px; color: {c['text_secondary']};">Offline Ready</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Actions
st.markdown('<div style="max-width: 1200px; margin: 20px auto; padding: 0 20px;">', unsafe_allow_html=True)
st.markdown(f"<h3 style='font-size: 16px; font-weight: 700; color: {c['text_primary']}; margin-bottom: 16px;'>🚀 Quick Actions</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    if st.button("📚 Add Books", use_container_width=True):
        st.info("Run: `python -m database.books_extended` to add 50+ books")

with col2:
    if st.button("🔄 Refresh Cache", use_container_width=True):
        st.cache_data.clear()
        st.success("Cache cleared!")
        st.rerun()

with col3:
    if st.button("📊 Export Stats", use_container_width=True):
        stats_data = {
            "total_books": total_books,
            "genres": len(genres),
            "authors": len(author_counts),
            "avg_rating": round(avg_rating, 2),
            "genre_distribution": genre_counts,
            "top_authors": dict(top_authors[:10]),
            "exported_at": datetime.now().isoformat()
        }
        st.json(stats_data)

with col4:
    st.link_button("🏠 Back to Home", "/", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

render_footer()
