"""
Stats bar component showing key metrics.
"""

import streamlit as st
from database.queries import get_books_count, get_genres_count


def render_stats_bar() -> None:
    """Render a horizontal stats bar with key platform metrics."""
    book_count = get_books_count()
    genre_count = get_genres_count()
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
                padding: 16px 32px; margin: 0;">
    <div style="max-width: 1400px; margin: 0 auto; display: flex; justify-content: center; 
                gap: 60px; align-items: center;">
    <div style="text-align: center;">
    <span style="font-size: 24px; font-weight: 800; color: white;">{book_count:,}+</span>
    <span style="font-size: 13px; color: rgba(255,255,255,0.7); margin-left: 8px;">Book Summaries</span>
    </div>
    <div style="width: 1px; height: 30px; background: rgba(255,255,255,0.2);"></div>
    <div style="text-align: center;">
    <span style="font-size: 24px; font-weight: 800; color: white;">{genre_count}</span>
    <span style="font-size: 13px; color: rgba(255,255,255,0.7); margin-left: 8px;">Genres</span>
    </div>
    <div style="width: 1px; height: 30px; background: rgba(255,255,255,0.2);"></div>
    <div style="text-align: center;">
    <span style="font-size: 24px; font-weight: 800; color: white;">15 min</span>
    <span style="font-size: 13px; color: rgba(255,255,255,0.7); margin-left: 8px;">Avg Read Time</span>
    </div>
    <div style="width: 1px; height: 30px; background: rgba(255,255,255,0.2);"></div>
    <div style="text-align: center;">
    <span style="font-size: 24px; font-weight: 800; color: white;">100%</span>
    <span style="font-size: 13px; color: rgba(255,255,255,0.7); margin-left: 8px;">Free Access</span>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)


def render_compact_stats() -> None:
    """Render compact stats pills."""
    book_count = get_books_count()
    genre_count = get_genres_count()
    
    st.markdown(f"""
    <div style="display: flex; gap: 12px; flex-wrap: wrap; margin: 16px 0;">
    <span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                 color: white; padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 600;">
    📖 {book_count:,}+ Books
    </span>
    <span style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                 color: white; padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 600;">
    📚 {genre_count} Genres
    </span>
    <span style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); 
                 color: white; padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 600;">
    ⏱️ 15 min reads
    </span>
    </div>
    """, unsafe_allow_html=True)
