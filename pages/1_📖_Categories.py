"""
Categories Page - Compact Awesome Design
"""

import streamlit as st
from database.queries import get_all_genres, get_genre_by_slug, get_books_by_genre
from components.image_handler import load_image_safe

st.set_page_config(
    page_title="Categories | BookWise",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Compact CSS
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');

#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}

* {margin: 0; padding: 0; box-sizing: border-box;}
body {font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b;}

div.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white; border: none; border-radius: 8px; padding: 8px 16px; font-size: 13px;
    font-weight: 600; transition: all 0.3s ease;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px -2px rgba(102, 126, 234, 0.4);
}

.hover-lift {transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);}
.hover-lift:hover {transform: translateY(-4px); box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.15);}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ==================== COMPACT NAVIGATION ====================
nav = """
<div style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 1000;">
<div style="max-width: 1400px; margin: 0 auto; padding: 0 24px; height: 60px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 24px;">📚</span>
<span style="font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 800; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">BookWise</span>
</div>
<div style="display: flex; gap: 32px; align-items: center;">
<a href="/" style="font-size: 14px; font-weight: 500; color: #64748b; text-decoration: none;">Home</a>
<a href="/Categories" style="font-size: 14px; font-weight: 600; color: #667eea; text-decoration: none; border-bottom: 2px solid #667eea; padding-bottom: 2px;">Categories</a>
<a href="/Book_Detail" style="font-size: 14px; font-weight: 500; color: #64748b; text-decoration: none;">Library</a>
<a href="/About" style="font-size: 14px; font-weight: 500; color: #64748b; text-decoration: none;">About</a>
</div>
<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 6px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; color: #92400e;">✨ 1,000+</div>
</div>
</div>
"""
st.markdown(nav, unsafe_allow_html=True)

genre_slug = st.query_params.get("name", None)

if genre_slug:
    # ==================== SINGLE GENRE VIEW (COMPACT) ====================
    genre = get_genre_by_slug(genre_slug)
    
    if genre:
        # Compact Breadcrumb
        st.markdown("""
        <div style="max-width: 1400px; margin: 0 auto; padding: 12px 24px;">
        <div style="font-size: 13px; color: #64748b;">
        <a href="/" style="color: #64748b; text-decoration: none;">Home</a> › 
        <a href="/Categories" style="color: #64748b; text-decoration: none;">Categories</a> › 
        <span style="color: #1e293b; font-weight: 600;">""" + genre.name + """</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Compact Genre Hero
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; overflow: hidden;">
        <div style="max-width: 1400px; margin: 0 auto; padding: 40px 24px; text-align: center;">
        <div style="font-size: 48px; margin-bottom: 12px;">{genre.icon}</div>
        <h1 style="font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 900; color: white; margin-bottom: 8px;">{genre.name}</h1>
        <p style="font-size: 15px; color: rgba(255, 255, 255, 0.9); max-width: 600px; margin: 0 auto;">{genre.description}</p>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Compact Books Grid
        books = get_books_by_genre(genre_slug)
        
        if books:
            st.markdown(f"""
            <div style="max-width: 1400px; margin: 0 auto; padding: 30px 24px 20px 24px;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 800; color: #1e293b; margin-bottom: 4px;">📚 All Books</h2>
            <p style="font-size: 14px; color: #64748b; margin-bottom: 20px;">{len(books)} summaries available</p>
            </div>
            """, unsafe_allow_html=True)
            
            cols = st.columns(6, gap="medium")
            for idx, book in enumerate(books):
                with cols[idx % 6]:
                    # Use safe image handler
                    safe_image_url = load_image_safe(book.cover_image_url, "book")
                    
                    st.markdown(f"""
                    <div class="hover-lift" style="background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); border: 1px solid #f1f5f9; margin-bottom: 16px;">
                    <div style="position: relative; padding-top: 150%; background: #f8fafc;">
                    <img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div style="padding: 12px;">
                    <h3 style="font-size: 13px; font-weight: 700; color: #1e293b; margin-bottom: 4px; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{book.title}</h3>
                    <p style="font-size: 11px; color: #64748b; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{book.author}</p>
                    </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.link_button("Read", f"/Book_Detail?slug={book.slug}", use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Back button
        st.markdown('<div style="max-width: 1400px; margin: 0 auto; padding: 0 24px 40px 24px;">', unsafe_allow_html=True)
        if st.button("← Back", use_container_width=False):
            st.query_params.clear()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # ==================== ALL GENRES VIEW (COMPACT) ====================
    
    # Compact Hero
    hero = """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; overflow: hidden;">
    <div style="max-width: 1400px; margin: 0 auto; padding: 50px 24px; text-align: center;">
    <h1 style="font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 900; color: white; margin-bottom: 12px; letter-spacing: -0.5px;">Explore by Category</h1>
    <p style="font-size: 16px; color: rgba(255, 255, 255, 0.9); margin: 0;">Browse 1,000+ expert summaries across 10 genres</p>
    </div>
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.1; background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 30px 30px;"></div>
    </div>
    """
    st.markdown(hero, unsafe_allow_html=True)
    
    # Compact Categories Grid
    st.markdown('<div style="max-width: 1400px; margin: 40px auto; padding: 0 24px;">', unsafe_allow_html=True)
    
    genres = get_all_genres()
    
    if genres:
        colors = {
            "self-help": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "business": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
            "psychology": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            "finance": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
            "productivity": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
            "philosophy": "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
            "history": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
            "science": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
            "biography": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
            "technology": "linear-gradient(135deg, #ff6e7f 0%, #bfe9ff 100%)"
        }
        
        # First row - 5 categories
        cols1 = st.columns(5, gap="medium")
        for idx in range(min(5, len(genres))):
            genre = genres[idx]
            gradient = colors.get(genre.slug, "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")
            
            with cols1[idx]:
                st.markdown(f"""
                <div class="hover-lift" style="background: {gradient}; border-radius: 16px; padding: 28px 20px; text-align: center; color: white; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); min-height: 180px; display: flex; flex-direction: column; justify-content: center; margin-bottom: 16px;">
                <div style="font-size: 40px; margin-bottom: 12px;">{genre.icon}</div>
                <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 8px;">{genre.name}</h3>
                <p style="font-size: 12px; opacity: 0.9; line-height: 1.4; margin-bottom: 12px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{genre.description}</p>
                <div style="background: rgba(255, 255, 255, 0.2); padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block;">100 Books</div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Explore →", key=f"genre_{genre.slug}", use_container_width=True):
                    st.query_params["name"] = genre.slug
                    st.rerun()
        
        # Second row - remaining categories
        if len(genres) > 5:
            cols2 = st.columns(5, gap="medium")
            for idx in range(5, min(10, len(genres))):
                genre = genres[idx]
                gradient = colors.get(genre.slug, "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")
                
                with cols2[idx - 5]:
                    st.markdown(f"""
                    <div class="hover-lift" style="background: {gradient}; border-radius: 16px; padding: 28px 20px; text-align: center; color: white; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); min-height: 180px; display: flex; flex-direction: column; justify-content: center; margin-bottom: 16px;">
                    <div style="font-size: 40px; margin-bottom: 12px;">{genre.icon}</div>
                    <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 8px;">{genre.name}</h3>
                    <p style="font-size: 12px; opacity: 0.9; line-height: 1.4; margin-bottom: 12px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{genre.description}</p>
                    <div style="background: rgba(255, 255, 255, 0.2); padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; display: inline-block;">100 Books</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"Explore →", key=f"genre2_{genre.slug}", use_container_width=True):
                        st.query_params["name"] = genre.slug
                        st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# ==================== COMPACT FOOTER ====================
footer = """
<div style="background: #1e293b; color: white; padding: 40px 0 20px 0; margin-top: 40px;">
<div style="max-width: 1400px; margin: 0 auto; padding: 0 24px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 24px;">📚</span>
<span style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 800;">BookWise</span>
</div>
<div style="display: flex; gap: 24px; font-size: 13px; color: #94a3b8;">
<a href="/" style="color: #94a3b8; text-decoration: none;">Home</a>
<a href="/Categories" style="color: #94a3b8; text-decoration: none;">Categories</a>
<a href="/About" style="color: #94a3b8; text-decoration: none;">About</a>
</div>
<div style=" color: #64748b; font-size: 12px;">© 2024 BookWise</div>
</div>
</div>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
