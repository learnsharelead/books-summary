"""
Reading Lists and Collections for BookWise.
Provides curated book lists for different user personas.
"""

import streamlit as st
from typing import List, Dict
from database.queries import get_book_by_slug, search_books
from components.image_handler import load_image_safe


# Curated reading lists
READING_LISTS = {
    "startup-essentials": {
        "title": "🚀 Startup Essentials",
        "description": "Must-read books for entrepreneurs and startup founders",
        "icon": "🚀",
        "color": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "books": [
            "the-lean-startup",
            "zero-to-one",
            "the-hard-thing-about-hard-things",
            "the-innovators-dilemma",
            "good-to-great",
            "start-with-why",
        ]
    },
    "productivity-masters": {
        "title": "⚡ Productivity Masters",
        "description": "Transform your output with these time-tested strategies",
        "icon": "⚡",
        "color": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
        "books": [
            "atomic-habits",
            "deep-work",
            "getting-things-done",
            "the-4-hour-workweek",
            "essentialism",
            "make-time",
        ]
    },
    "wealth-building": {
        "title": "💰 Wealth Building",
        "description": "Master your finances and build lasting wealth",
        "icon": "💰",
        "color": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
        "books": [
            "the-psychology-of-money",
            "rich-dad-poor-dad",
            "think-and-grow-rich",
            "the-intelligent-investor",
            "the-millionaire-next-door",
            "your-money-or-your-life",
        ]
    },
    "mindset-shift": {
        "title": "🧠 Mindset Shift",
        "description": "Rewire your thinking for success and happiness",
        "icon": "🧠",
        "color": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "books": [
            "mindset",
            "thinking-fast-and-slow",
            "the-power-of-now",
            "mans-search-for-meaning",
            "the-subtle-art-of-not-giving-a-fck",
            "grit",
        ]
    },
    "leadership-excellence": {
        "title": "👔 Leadership Excellence",
        "description": "Develop the skills to lead teams and organizations",
        "icon": "👔",
        "color": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "books": [
            "the-7-habits-of-highly-effective-people",
            "how-to-win-friends-and-influence-people",
            "extreme-ownership",
            "leaders-eat-last",
            "the-five-dysfunctions-of-a-team",
            "primal-leadership",
        ]
    },
    "stoic-wisdom": {
        "title": "🏛️ Stoic Wisdom",
        "description": "Ancient philosophy for modern challenges",
        "icon": "🏛️",
        "color": "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
        "books": [
            "meditations",
            "the-daily-stoic",
            "letters-from-a-stoic",
            "the-obstacle-is-the-way",
            "ego-is-the-enemy",
            "mans-search-for-meaning",
        ]
    },
}


def get_reading_lists() -> Dict[str, dict]:
    """Get all available reading lists."""
    return READING_LISTS


def get_reading_list(list_id: str) -> dict:
    """Get a specific reading list by ID."""
    return READING_LISTS.get(list_id, {})


def render_reading_lists_grid() -> None:
    """Render a grid of all reading lists."""
    st.markdown("""
    <div style="max-width: 1400px; margin: 40px auto; padding: 0 32px;">
    <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 800; 
               color: #1e293b; margin-bottom: 8px;">📚 Curated Reading Lists</h2>
    <p style="font-size: 16px; color: #64748b; margin-bottom: 32px;">
    Expert-curated collections to accelerate your learning
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3, gap="large")
    
    for idx, (list_id, reading_list) in enumerate(READING_LISTS.items()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="hover-lift" style="background: {reading_list['color']}; 
                        border-radius: 16px; padding: 28px; margin-bottom: 24px;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <div style="font-size: 48px; margin-bottom: 12px;">{reading_list['icon']}</div>
            <h3 style="font-size: 20px; font-weight: 700; color: white; margin-bottom: 8px;">
            {reading_list['title']}
            </h3>
            <p style="font-size: 14px; color: rgba(255,255,255,0.9); margin-bottom: 12px;">
            {reading_list['description']}
            </p>
            <div style="background: rgba(255,255,255,0.2); padding: 6px 12px; 
                        border-radius: 20px; font-size: 12px; color: white; display: inline-block;">
            {len(reading_list['books'])} Books
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Explore →", key=f"list_{list_id}", use_container_width=True):
                st.session_state["selected_list"] = list_id
                st.rerun()


def render_reading_list_detail(list_id: str) -> None:
    """Render a single reading list with its books."""
    reading_list = get_reading_list(list_id)
    
    if not reading_list:
        st.error("Reading list not found")
        return
    
    # Header
    st.markdown(f"""
    <div style="background: {reading_list['color']}; padding: 40px 32px; border-radius: 16px; 
                margin-bottom: 32px; text-align: center;">
    <div style="font-size: 64px; margin-bottom: 16px;">{reading_list['icon']}</div>
    <h1 style="font-size: 36px; font-weight: 800; color: white; margin-bottom: 8px;">
    {reading_list['title']}
    </h1>
    <p style="font-size: 18px; color: rgba(255,255,255,0.9);">
    {reading_list['description']}
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Reading Lists"):
        del st.session_state["selected_list"]
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Books grid
    cols = st.columns(6, gap="medium")
    
    for idx, book_slug in enumerate(reading_list["books"]):
        book = get_book_by_slug(book_slug)
        
        if book:
            with cols[idx % 6]:
                safe_image_url = load_image_safe(book.cover_image_url, "book")
                
                st.markdown(f"""
                <div class="hover-lift" style="background: white; border-radius: 12px; 
                            overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                            margin-bottom: 16px;">
                <div style="position: relative; padding-top: 150%; background: #f8fafc;">
                <img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; 
                     width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div style="padding: 12px;">
                <h4 style="font-size: 13px; font-weight: 700; color: #1e293b; margin-bottom: 4px;
                           line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2;
                           -webkit-box-orient: vertical; overflow: hidden;">
                {book.title}
                </h4>
                <p style="font-size: 11px; color: #64748b;">{book.author}</p>
                </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.link_button("Read", f"/Book_Detail?slug={book.slug}", use_container_width=True)


def render_reading_lists_section() -> None:
    """Main entry point for reading lists - handles both list view and detail view."""
    if "selected_list" in st.session_state:
        render_reading_list_detail(st.session_state["selected_list"])
    else:
        render_reading_lists_grid()
