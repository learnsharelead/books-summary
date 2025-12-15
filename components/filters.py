"""
Filter components for BookWise.
Provides advanced filtering functionality for books.
"""

import streamlit as st
from typing import List, Optional, Tuple
from database.models import Book
from database.connection import get_db_session
from sqlalchemy.orm import joinedload


def get_filter_options() -> dict:
    """
    Get available filter options from the database.
    
    Returns:
        dict: Dictionary with filter options
    """
    with get_db_session() as session:
        # Get unique years
        years = session.query(Book.publication_year).distinct().order_by(Book.publication_year.desc()).all()
        years = [y[0] for y in years if y[0]]
        
        session.expunge_all()
        
        return {
            "years": years,
            "reading_times": [5, 10, 15, 20, 30],
            "difficulties": ["beginner", "intermediate", "advanced"],
        }


def render_filters() -> dict:
    """
    Render filter controls and return selected values.
    
    Returns:
        dict: Selected filter values
    """
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 12px; 
                box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 24px;">
    <h4 style="margin: 0 0 16px 0; color: #1e293b; font-size: 16px; font-weight: 600;">
    🎛️ Filter Books
    </h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    options = get_filter_options()
    
    with col1:
        # Year range filter
        year_options = ["All Years"] + [str(y) for y in options["years"][:20]]
        selected_year = st.selectbox("📅 Publication Year", year_options, key="filter_year")
    
    with col2:
        # Reading time filter
        time_options = ["Any Time", "< 10 min", "10-15 min", "15-20 min", "> 20 min"]
        selected_time = st.selectbox("⏱️ Reading Time", time_options, key="filter_time")
    
    with col3:
        # Sort by
        sort_options = ["Title (A-Z)", "Title (Z-A)", "Newest First", "Oldest First", "Rating"]
        selected_sort = st.selectbox("🔃 Sort By", sort_options, key="filter_sort")
    
    with col4:
        # Clear filters button
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Reset Filters", key="reset_filters"):
            st.session_state["filter_year"] = "All Years"
            st.session_state["filter_time"] = "Any Time"
            st.session_state["filter_sort"] = "Title (A-Z)"
            st.rerun()
    
    return {
        "year": None if selected_year == "All Years" else int(selected_year),
        "reading_time": selected_time,
        "sort": selected_sort
    }


def apply_filters(books: List[Book], filters: dict) -> List[Book]:
    """
    Apply filters to a list of books.
    
    Args:
        books: List of Book objects
        filters: Dictionary of filter values
    
    Returns:
        List[Book]: Filtered and sorted books
    """
    filtered = books.copy()
    
    # Filter by year
    if filters.get("year"):
        filtered = [b for b in filtered if b.publication_year == filters["year"]]
    
    # Filter by reading time (would need summary data)
    # This would require joining with Summary table in the query
    
    # Sort
    sort_option = filters.get("sort", "Title (A-Z)")
    
    if sort_option == "Title (A-Z)":
        filtered.sort(key=lambda b: b.title.lower())
    elif sort_option == "Title (Z-A)":
        filtered.sort(key=lambda b: b.title.lower(), reverse=True)
    elif sort_option == "Newest First":
        filtered.sort(key=lambda b: b.publication_year or 0, reverse=True)
    elif sort_option == "Oldest First":
        filtered.sort(key=lambda b: b.publication_year or 9999)
    
    return filtered


def render_filter_pills(filters: dict) -> None:
    """
    Render active filter pills.
    
    Args:
        filters: Dictionary of active filter values
    """
    active_filters = []
    
    if filters.get("year"):
        active_filters.append(f"📅 {filters['year']}")
    
    if filters.get("reading_time") and filters["reading_time"] != "Any Time":
        active_filters.append(f"⏱️ {filters['reading_time']}")
    
    if active_filters:
        pills_html = " ".join([
            f'<span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); '
            f'color: white; padding: 6px 12px; border-radius: 20px; font-size: 12px; '
            f'font-weight: 500; margin-right: 8px;">{pill}</span>'
            for pill in active_filters
        ])
        
        st.markdown(f"""
        <div style="margin-bottom: 16px;">
        <span style="color: #64748b; font-size: 13px; margin-right: 8px;">Active filters:</span>
        {pills_html}
        </div>
        """, unsafe_allow_html=True)


def render_compact_sort() -> str:
    """
    Render a compact sort dropdown.
    
    Returns:
        str: Selected sort option
    """
    sort_options = ["Relevance", "Title (A-Z)", "Newest", "Popular"]
    
    st.markdown("""
    <style>
    .compact-sort select {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 13px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    return st.selectbox("Sort", sort_options, key="compact_sort", label_visibility="collapsed")
