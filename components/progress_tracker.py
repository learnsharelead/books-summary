"""
Reading Progress Tracker for BookWise.
Tracks user's reading progress per book.
"""

import streamlit as st
from typing import Dict, Optional
from datetime import datetime


def get_reading_progress(book_slug: str) -> Dict:
    """
    Get reading progress for a book.
    
    Args:
        book_slug: The book's slug
    
    Returns:
        Dict: Progress data including sections read and percentage
    """
    if "reading_progress" not in st.session_state:
        st.session_state["reading_progress"] = {}
    
    return st.session_state["reading_progress"].get(book_slug, {
        "sections_read": [],
        "started_at": None,
        "completed_at": None,
        "percentage": 0
    })


def update_reading_progress(
    book_slug: str,
    section: str,
    total_sections: int = 5
) -> None:
    """
    Update reading progress when a section is read.
    
    Args:
        book_slug: The book's slug
        section: Section name that was read
        total_sections: Total number of sections
    """
    if "reading_progress" not in st.session_state:
        st.session_state["reading_progress"] = {}
    
    if book_slug not in st.session_state["reading_progress"]:
        st.session_state["reading_progress"][book_slug] = {
            "sections_read": [],
            "started_at": datetime.now().isoformat(),
            "completed_at": None,
            "percentage": 0
        }
    
    progress = st.session_state["reading_progress"][book_slug]
    
    if section not in progress["sections_read"]:
        progress["sections_read"].append(section)
        progress["percentage"] = int(len(progress["sections_read"]) / total_sections * 100)
        
        if progress["percentage"] >= 100:
            progress["completed_at"] = datetime.now().isoformat()


def render_progress_bar(book_slug: str, total_sections: int = 5) -> None:
    """
    Render progress bar for a book.
    
    Args:
        book_slug: The book's slug
        total_sections: Total number of sections
    """
    progress = get_reading_progress(book_slug)
    percentage = progress["percentage"]
    sections_read = len(progress["sections_read"])
    
    # Determine color based on progress
    if percentage >= 100:
        color = "#22c55e"  # Green
        status = "✅ Completed"
    elif percentage > 0:
        color = "#667eea"  # Purple
        status = "📖 In Progress"
    else:
        color = "#e2e8f0"  # Gray
        status = "📚 Not Started"
    
    st.markdown(f"""
    <div style="background: white; padding: 16px; border-radius: 12px; 
                box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <span style="font-size: 13px; font-weight: 600; color: #1e293b;">{status}</span>
    <span style="font-size: 13px; color: #64748b;">{sections_read}/{total_sections} sections</span>
    </div>
    <div style="background: #e2e8f0; border-radius: 8px; height: 8px; overflow: hidden;">
    <div style="background: {color}; width: {percentage}%; height: 100%; border-radius: 8px;
                transition: width 0.3s ease;"></div>
    </div>
    <div style="text-align: right; margin-top: 4px;">
    <span style="font-size: 12px; color: #64748b; font-weight: 600;">{percentage}%</span>
    </div>
    </div>
    """, unsafe_allow_html=True)


def render_section_checkboxes(
    book_slug: str,
    sections: list = None
) -> None:
    """
    Render checkboxes for tracking section completion.
    
    Args:
        book_slug: The book's slug
        sections: List of section names
    """
    if sections is None:
        sections = [
            "Executive Summary",
            "Key Concepts",
            "Visual Framework",
            "Action Steps",
            "Quotes"
        ]
    
    progress = get_reading_progress(book_slug)
    
    st.markdown("""
    <div style="background: #f8fafc; padding: 16px; border-radius: 12px; margin-bottom: 16px;">
    <h4 style="font-size: 14px; font-weight: 600; color: #1e293b; margin-bottom: 12px;">
    📋 Track Your Progress
    </h4>
    </div>
    """, unsafe_allow_html=True)
    
    for section in sections:
        is_read = section in progress["sections_read"]
        
        if st.checkbox(
            f"{'✅' if is_read else '⬜'} {section}",
            value=is_read,
            key=f"section_{book_slug}_{section}"
        ):
            if not is_read:
                update_reading_progress(book_slug, section, len(sections))
                st.rerun()


def render_reading_stats() -> None:
    """Render overall reading statistics."""
    if "reading_progress" not in st.session_state:
        st.session_state["reading_progress"] = {}
    
    progress_data = st.session_state["reading_progress"]
    
    total_books = len(progress_data)
    completed = sum(1 for p in progress_data.values() if p.get("completed_at"))
    in_progress = sum(1 for p in progress_data.values() 
                      if p.get("percentage", 0) > 0 and not p.get("completed_at"))
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 24px; border-radius: 16px; color: white;">
    <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 16px;">📊 Your Reading Stats</h3>
    <div style="display: flex; gap: 24px;">
    <div>
    <div style="font-size: 28px; font-weight: 800;">{total_books}</div>
    <div style="font-size: 12px; opacity: 0.9;">Books Started</div>
    </div>
    <div>
    <div style="font-size: 28px; font-weight: 800;">{in_progress}</div>
    <div style="font-size: 12px; opacity: 0.9;">In Progress</div>
    </div>
    <div>
    <div style="font-size: 28px; font-weight: 800;">{completed}</div>
    <div style="font-size: 12px; opacity: 0.9;">Completed</div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)


def mark_section_complete(book_slug: str, section: str) -> None:
    """Quick function to mark a section as complete."""
    update_reading_progress(book_slug, section)


def get_books_in_progress() -> list:
    """Get list of books currently in progress."""
    if "reading_progress" not in st.session_state:
        return []
    
    return [
        slug for slug, progress in st.session_state["reading_progress"].items()
        if progress.get("percentage", 0) > 0 and not progress.get("completed_at")
    ]


def get_completed_books() -> list:
    """Get list of completed books."""
    if "reading_progress" not in st.session_state:
        return []
    
    return [
        slug for slug, progress in st.session_state["reading_progress"].items()
        if progress.get("completed_at")
    ]
