"""
Genre card components for BookWise.
Renders genre cards and grids.
"""

import streamlit as st
from typing import List, Any


def render_genre_card(genre: Any) -> None:
    """
    Render a single genre card.
    
    Args:
        genre: Genre model instance
    """
    book_count = genre.book_count if hasattr(genre, 'book_count') else 0
    
    with st.container():
        st.markdown(f"### {genre.icon} {genre.name}")
        st.caption(genre.description[:100] + "..." if len(genre.description) > 100 else genre.description)
        st.caption(f"📖 {book_count} books")
        if st.button("Explore", key=f"genre_{genre.slug}"):
            st.query_params["name"] = genre.slug
            st.switch_page("pages/1_📖_Categories.py")


def render_genre_grid(genres: List[Any], columns: int = 3) -> None:
    """
    Render a grid of genre cards.
    
    Args:
        genres: List of Genre model instances
        columns: Number of columns in the grid
    """
    if not genres:
        st.info("No genres found.")
        return
    
    cols = st.columns(columns)
    for idx, genre in enumerate(genres):
        with cols[idx % columns]:
            render_genre_card(genre)


def render_genre_hero(genre: Any) -> None:
    """Render a hero section for a genre page."""
    st.markdown(f"""
    <div class="hero-section">
        <div class="genre-icon" style="font-size:4rem;">{genre.icon}</div>
        <h1 class="hero-title">{genre.name}</h1>
        <p class="hero-subtitle">{genre.description}</p>
    </div>
    """, unsafe_allow_html=True)
