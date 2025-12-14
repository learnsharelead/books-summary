"""
Helper utilities for BookWise.
"""

import streamlit as st
from pathlib import Path


def load_css() -> None:
    """Load custom CSS styles."""
    css_path = Path(__file__).parent.parent / "assets" / "css" / "styles.css"
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    return (
        text.lower()
        .replace(" ", "-")
        .replace(":", "")
        .replace("'", "")
        .replace(",", "")
        .replace(".", "")
        .replace("&", "and")
    )


def format_reading_time(minutes: int) -> str:
    """Format reading time for display."""
    if minutes < 1:
        return "< 1 min read"
    elif minutes == 1:
        return "1 min read"
    else:
        return f"{minutes} min read"


def render_footer() -> None:
    """Render page footer."""
    st.markdown("---")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**BookWise**")
        st.caption("AI-Powered Book Summaries")
    with cols[1]:
        st.markdown("[About](/About) | [Privacy](/Privacy) | [Terms](/Terms)")
    with cols[2]:
        st.caption("© 2024 BookWise. All rights reserved.")


def init_page_config(
    title: str = "BookWise",
    icon: str = "📚",
    layout: str = "wide"
) -> None:
    """Initialize Streamlit page configuration."""
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout=layout,
        initial_sidebar_state="collapsed",
        menu_items={
            "Get help": None,
            "Report a Bug": None,
            "About": "BookWise - AI-Powered Book Summary Platform"
        }
    )
    load_css()
