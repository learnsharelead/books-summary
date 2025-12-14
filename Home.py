"""
BookWise - Awesome Modern Homepage
"""

import streamlit as st
from database.queries import get_featured_books, get_all_genres
from components.image_handler import load_image_safe

st.set_page_config(
    page_title="BookWise - Transform Your Life",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern CSS with animations and professional styling
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}

/* Global Styles */
* {margin: 0; padding: 0; box-sizing: border-box;}
body {font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b;}

/* Smooth Scrolling */
html {scroll-behavior: smooth;}

/* Button Styling */
div.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px -1px rgba(102, 126, 234, 0.3);
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(102, 126, 234, 0.4);
}

/* Input Styling */
input[type="text"] {
    border: 2px solid #e2e8f0 !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    transition: all 0.3s ease !important;
}

input[type="text"]:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in-up {
    animation: fadeInUp 0.6s ease-out;
}

/* Card Hover Effect */
.hover-lift {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hover-lift:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ==================== NAVIGATION ====================
nav = """
<div style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);">
<div style="max-width: 1400px; margin: 0 auto; padding: 0 32px; height: 70px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="font-size: 32px;">📚</span>
<span style="font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 800; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">BookWise</span>
</div>
<div style="display: flex; gap: 40px; align-items: center;">
<a href="/" style="font-size: 15px; font-weight: 600; color: #667eea; text-decoration: none; padding-bottom: 2px; border-bottom: 2px solid #667eea;">Home</a>
<a href="/Categories" style="font-size: 15px; font-weight: 500; color: #64748b; text-decoration: none; transition: color 0.2s;">Categories</a>
<a href="/Book_Detail" style="font-size: 15px; font-weight: 500; color: #64748b; text-decoration: none; transition: color 0.2s;">Library</a>
<a href="/About" style="font-size: 15px; font-weight: 500; color: #64748b; text-decoration: none; transition: color 0.2s;">About</a>
</div>
<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 8px 16px; border-radius: 20px; font-size: 12px; font-weight: 700; color: #92400e;">
✨ 1,000+ Premium Summaries
</div>
</div>
</div>
"""
st.markdown(nav, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero = """
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; overflow: hidden;">
<div style="max-width: 1400px; margin: 0 auto; padding: 80px 32px; text-align: center; position: relative; z-index: 1;">
<div class="fade-in-up" style="max-width: 900px; margin: 0 auto;">
<h1 style="font-family: 'Playfair Display', serif; font-size: 56px; font-weight: 900; color: white; margin-bottom: 24px; line-height: 1.1; letter-spacing: -1px;">
Transform Your Life,<br/>
<span style="color: #e0e7ff;">One Book at a Time</span>
</h1>
<p style="font-size: 20px; color: rgba(255, 255, 255, 0.9); margin-bottom: 40px; line-height: 1.6;">
Master the world's most influential books in just 15 minutes.<br/>
Expert summaries • Key frameworks • Actionable insights
</p>
</div>
</div>
<div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.1; background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 40px 40px;"></div>
</div>
"""
st.markdown(hero, unsafe_allow_html=True)

# ==================== SEARCH BAR ====================
st.markdown('<div style="max-width: 1400px; margin: -30px auto 60px auto; padding: 0 32px; position: relative; z-index: 10;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div style="background: white; padding: 8px; border-radius: 16px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">', unsafe_allow_html=True)
    search = st.text_input("Search", placeholder="🔍  Search 1,000+ book summaries...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================== FEATURED BOOKS ====================
st.markdown("""
<div style="max-width: 1400px; margin: 0 auto; padding: 0 32px 60px 32px;">
<div style="margin-bottom: 40px;">
<h2 style="font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 800; color: #1e293b; margin-bottom: 8px;">✨ Featured Masterpieces</h2>
<p style="font-size: 16px; color: #64748b;">Handpicked summaries to accelerate your growth</p>
</div>
""", unsafe_allow_html=True)

featured = get_featured_books(limit=6)
cols = st.columns(6, gap="medium")

for idx, book in enumerate(featured):
    with cols[idx]:
        # Use safe image handler to prevent broken images
        safe_image_url = load_image_safe(book.cover_image_url, "book")
        
        st.markdown(f"""
        <div class="hover-lift" style="background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border: 1px solid #f1f5f9;">
        <div style="position: relative; padding-top: 150%; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);">
        <img src="{safe_image_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div style="padding: 16px;">
        <h3 style="font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 4px; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{book.title}</h3>
        <p style="font-size: 12px; color: #64748b; margin-bottom: 4px;">{book.author}</p>
        <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px;">
        <span style="font-size: 11px; color: #94a3b8;">📖 {book.publication_year}</span>
        <span style="font-size: 11px; color: #94a3b8;">• 15 min</span>
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("Read Summary", f"Book_Detail?slug={book.slug}", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==================== CATEGORIES ====================
st.markdown("""
<div style="background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); padding: 80px 0; border-top: 1px solid #e2e8f0;">
<div style="max-width: 1400px; margin: 0 auto; padding: 0 32px;">
<div style="text-align: center; margin-bottom: 50px;">
<h2 style="font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 800; color: #1e293b; margin-bottom: 8px;">🎯 Explore by Category</h2>
<p style="font-size: 16px; color: #64748b;">Dive deep into topics that matter to you</p>
</div>
""", unsafe_allow_html=True)

genres = get_all_genres()
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

cols1 = st.columns(5, gap="large")
for idx in range(min(5, len(genres))):
    genre = genres[idx]
    gradient = colors.get(genre.slug, "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")
    
    with cols1[idx]:
        st.markdown(f"""
        <div class="hover-lift" style="background: {gradient}; border-radius: 20px; padding: 32px; text-align: center; color: white; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); min-height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div style="font-size: 48px; margin-bottom: 16px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));">{genre.icon}</div>
        <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">{genre.name}</h3>
        <p style="font-size: 14px; opacity: 0.9;">100 Premium Summaries</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Explore →", key=f"cat_{genre.slug}", use_container_width=True):
            st.switch_page("pages/1_📖_Categories.py")

if len(genres) > 5:
    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
    cols2 = st.columns(5, gap="large")
    for idx in range(5, min(10, len(genres))):
        genre = genres[idx]
        gradient = colors.get(genre.slug, "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")
        
        with cols2[idx - 5]:
            st.markdown(f"""
            <div class="hover-lift" style="background: {gradient}; border-radius: 20px; padding: 32px; text-align: center; color: white; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); min-height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="font-size: 48px; margin-bottom: 16px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));">{genre.icon}</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">{genre.name}</h3>
            <p style="font-size: 14px; opacity: 0.9;">100 Premium Summaries</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Explore →", key=f"cat2_{genre.slug}", use_container_width=True):
                st.switch_page("pages/1_📖_Categories.py")

st.markdown("</div></div>", unsafe_allow_html=True)

# ==================== FOOTER ====================
footer = """
<div style="background: #1e293b; color: white; padding: 60px 0 30px 0; margin-top: 80px;">
<div style="max-width: 1400px; margin: 0 auto; padding: 0 32px;">
<div style="display: flex; justify-content: space-between; margin-bottom: 40px;">
<div style="max-width: 400px;">
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
<span style="font-size: 32px;">📚</span>
<span style="font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 800;">BookWise</span>
</div>
<p style="color: #94a3b8; line-height: 1.6;">Transform your life with expert book summaries. Learn faster, grow smarter.</p>
</div>
<div style="display: flex; gap: 60px;">
<div>
<h4 style="font-weight: 700; margin-bottom: 16px;">Platform</h4>
<div style="display: flex; flex-direction: column; gap: 12px; color: #94a3b8; font-size: 14px;">
<a href="/" style="color: #94a3b8; text-decoration: none;">Home</a>
<a href="/Categories" style="color: #94a3b8; text-decoration: none;">Categories</a>
<a href="/Book_Detail" style="color: #94a3b8; text-decoration: none;">Library</a>
</div>
</div>
<div>
<h4 style="font-weight: 700; margin-bottom: 16px;">Company</h4>
<div style="display: flex; flex-direction: column; gap: 12px; color: #94a3b8; font-size: 14px;">
<a href="/About" style="color: #94a3b8; text-decoration: none;">About</a>
<a href="#" style="color: #94a3b8; text-decoration: none;">Contact</a>
<a href="#" style="color: #94a3b8; text-decoration: none;">Privacy</a>
</div>
</div>
</div>
</div>
<div style="border-top: 1px solid #334155; padding-top: 30px; text-align: center; color: #64748b; font-size: 14px;">
© 2024 BookWise. All rights reserved. Built with ❤️ for learners worldwide.
</div>
</div>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
