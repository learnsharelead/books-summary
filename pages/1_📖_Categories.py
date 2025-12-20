"""
Categories Page - With Pagination and Theme Support
"""

import streamlit as st
from database.queries import get_all_genres, get_genre_by_slug, get_books_by_genre
from components.image_handler import load_image_safe
from components.navigation import render_navigation, render_breadcrumb
from components.footer import render_footer
from components.theme import render_global_styles, get_theme_colors, get_genre_color, COLORS
from components.pagination import paginate_items, render_pagination, PaginationConfig

@st.cache_data(ttl=300)
def get_genre_book_counts():
    genres = get_all_genres()
    return {g.slug: len(get_books_by_genre(g.slug)) for g in genres}

st.set_page_config(page_title="Categories | BookWise", page_icon="📖", layout="wide", initial_sidebar_state="collapsed")

# Apply global styles from theme
render_global_styles()

# Get theme colors
c = get_theme_colors()

render_navigation(active_page="Categories")
genre_slug = st.query_params.get("name", None)

if genre_slug:
    genre = get_genre_by_slug(genre_slug)
    if genre:
        render_breadcrumb([
            {"label": "Home", "url": "/"},
            {"label": "Categories", "url": "/Categories"},
            {"label": genre.name, "url": f"/Categories?name={genre.slug}"}
        ])
        
        # Hero for genre
        genre_color = get_genre_color(genre_slug)
        st.markdown(f'''
        <div style="background: linear-gradient(135deg, {genre_color} 0%, {genre_color}dd 100%);">
        <div style="max-width: 1200px; margin: 0 auto; padding: 20px; text-align: center;">
        <div style="font-size: 36px; margin-bottom: 8px;">{genre.icon}</div>
        <h1 style="font-size: 24px; font-weight: 900; color: white; margin-bottom: 6px;">{genre.name}</h1>
        <p style="font-size: 13px; color: rgba(255, 255, 255, 0.9);">{genre.description}</p>
        </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Get all books for this genre
        all_books = get_books_by_genre(genre_slug)
        
        if all_books:
            # Pagination config
            pagination_key = f"genre_{genre_slug}"
            config = PaginationConfig(items_per_page=12, show_page_size_selector=True)
            
            # Paginate books
            paginated_books, current_page, total_pages = paginate_items(
                all_books, pagination_key, config
            )
            
            # Header with count
            st.markdown(f'''
            <div style="max-width: 1200px; margin: 0 auto; padding: 16px 20px 8px 20px;">
            <h3 style="font-size: 16px; font-weight: 800; color: {c['text_primary']};">
            📚 {len(all_books)} Books
            </h3>
            </div>
            ''', unsafe_allow_html=True)
            
            # Book grid
            cols = st.columns(6, gap="small")
            for idx, book in enumerate(paginated_books):
                with cols[idx % 6]:
                    safe_image_url = load_image_safe(book.cover_image_url, "book")
                    st.markdown(f'''
                    <div class="hover-lift" style="
                        background: {c['surface']};
                        border-radius: 8px;
                        overflow: hidden;
                        box-shadow: 0 2px 6px {c['shadow']};
                        margin-bottom: 10px;
                    ">
                    <div style="position: relative; padding-top: 140%; background: {c['background']};">
                    <img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div style="padding: 10px;">
                    <h4 style="font-size: 13px; font-weight: 700; color: {c['text_primary']}; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; margin: 0;">{book.title}</h4>
                    <p style="font-size: 11px; color: {c['text_secondary']}; margin: 4px 0 0 0;">{book.author}</p>
                    </div>
                    </div>
                    ''', unsafe_allow_html=True)
                    st.link_button("Read", f"/Book_Detail?slug={book.slug}", use_container_width=True)
            
            # Render pagination controls
            render_pagination(
                key=pagination_key,
                total_items=len(all_books),
                config=config,
                show_info=True
            )
        
        st.markdown(f'<div style="max-width: 1200px; margin: 0 auto; padding: 12px 20px 20px 20px;">', unsafe_allow_html=True)
        if st.button("← Back to Categories", use_container_width=False):
            st.query_params.clear()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # All categories view
    st.markdown(f'''
    <div style="background: {COLORS['primary_gradient']};">
    <div style="max-width: 1200px; margin: 0 auto; padding: 28px 20px; text-align: center;">
    <h1 style="font-size: 26px; font-weight: 900; color: white; margin-bottom: 6px;">Explore by Category</h1>
    <p style="font-size: 14px; color: rgba(255, 255, 255, 0.9);">Browse expert summaries across all genres</p>
    </div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div style="max-width: 1200px; margin: 20px auto; padding: 0 20px;">', unsafe_allow_html=True)
    
    genres = get_all_genres()
    book_counts = get_genre_book_counts()
    
    if genres:
        # First row of genres
        cols1 = st.columns(5, gap="small")
        for idx in range(min(5, len(genres))):
            genre = genres[idx]
            color = get_genre_color(genre.slug)
            book_count = book_counts.get(genre.slug, 0)
            with cols1[idx]:
                st.markdown(f'''
                <div class="hover-lift" style="
                    background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
                    border-radius: 10px;
                    padding: 18px 12px;
                    text-align: center;
                    color: white;
                    min-height: 110px;
                    margin-bottom: 10px;
                ">
                <div style="font-size: 30px; margin-bottom: 8px;">{genre.icon}</div>
                <div style="font-size: 14px; font-weight: 700;">{genre.name}</div>
                <div style="font-size: 11px; opacity: 0.9;">{book_count} books</div>
                </div>
                ''', unsafe_allow_html=True)
                st.link_button("Explore →", f"/Categories?name={genre.slug}", use_container_width=True)
        
        # Second row of genres
        if len(genres) > 5:
            cols2 = st.columns(5, gap="small")
            for idx in range(5, min(10, len(genres))):
                genre = genres[idx]
                color = get_genre_color(genre.slug)
                book_count = book_counts.get(genre.slug, 0)
                with cols2[idx - 5]:
                    st.markdown(f'''
                    <div class="hover-lift" style="
                        background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
                        border-radius: 10px;
                        padding: 18px 12px;
                        text-align: center;
                        color: white;
                        min-height: 110px;
                        margin-bottom: 10px;
                    ">
                    <div style="font-size: 30px; margin-bottom: 8px;">{genre.icon}</div>
                    <div style="font-size: 14px; font-weight: 700;">{genre.name}</div>
                    <div style="font-size: 11px; opacity: 0.9;">{book_count} books</div>
                    </div>
                    ''', unsafe_allow_html=True)
                    st.link_button("Explore →", f"/Categories?name={genre.slug}", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()
