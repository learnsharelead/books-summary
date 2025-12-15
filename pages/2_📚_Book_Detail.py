"""
Book Detail Page - Compact with readable fonts
"""

import streamlit as st
import json
from database.queries import get_book_by_slug, get_summary_for_book, get_books_by_genre
from components.image_handler import load_image_safe

st.set_page_config(page_title="Book Summary", page_icon="📖", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 1rem 1.5rem !important; max-width: 1100px !important; margin: 0 auto;}
body {font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b;}
div.stButton > button {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

book_slug = st.query_params.get("slug", None)
if not book_slug:
    st.warning("Select a book from the library")
    st.link_button("← Home", "/")
    st.stop()

book = get_book_by_slug(book_slug)
if not book:
    st.error("Book not found")
    st.stop()

summary = get_summary_for_book(book.id)
if not summary:
    st.error("Summary not found")
    st.link_button("← Home", "/")
    st.stop()

def safe_json(val):
    try: return json.loads(val or "[]")
    except: return []

takeaways = safe_json(summary.key_takeaways)
analogies = safe_json(summary.analogies)
quotes = safe_json(summary.quotes)
actions = safe_json(summary.action_steps)

# Header
col1, col2 = st.columns([1, 4], gap="medium")
with col1:
    if book.cover_image_url:
        st.image(load_image_safe(book.cover_image_url), use_container_width=True)

with col2:
    st.markdown(f"### {book.title}")
    st.markdown(f"**by {book.author}**")
    
    st.markdown(f'''<div style="display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0;">
        <span style="background: #E8F4FD; padding: 4px 10px; border-radius: 10px; font-size: 12px; color: #1E40AF;">📚 {book.genre.name}</span>
        <span style="background: #FFF4E6; padding: 4px 10px; border-radius: 10px; font-size: 12px; color: #92400E;">⏱️ {summary.reading_time} min</span>
        <span style="background: #F3F4F6; padding: 4px 10px; border-radius: 10px; font-size: 12px; color: #374151;">📅 {book.publication_year}</span>
        <span style="background: #FFF8DC; padding: 4px 10px; border-radius: 10px; font-size: 12px; color: #78350F;">⭐ {summary.rating}/5</span>
    </div>''', unsafe_allow_html=True)
    
    if summary.quote_of_the_book:
        st.markdown(f'<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 12px 14px; border-radius: 8px; color: white; margin: 10px 0; font-size: 13px; font-style: italic; border-left: 3px solid #FFD700;">"{summary.quote_of_the_book[:120]}{"..." if len(summary.quote_of_the_book) > 120 else ""}"</div>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📖 Summary", "💡 Concepts", "🚀 Actions", "💬 Quotes"])

with tab1:
    st.markdown(f'<div style="background: white; padding: 14px; border-radius: 8px; border-left: 3px solid #6366F1; font-size: 14px; line-height: 1.6;">{summary.executive_summary}</div>', unsafe_allow_html=True)
    if summary.who_should_read:
        st.markdown(f'<div style="background: #E8F8F5; padding: 12px; border-radius: 8px; margin-top: 10px; border-left: 3px solid #10B981;"><span style="font-size: 13px; font-weight: 600; color: #065F46;">👥 Perfect For:</span> <span style="font-size: 13px; color: #047857;">{summary.who_should_read}</span></div>', unsafe_allow_html=True)

with tab2:
    if takeaways:
        for idx, t in enumerate(takeaways[:5], 1):
            with st.expander(f"{idx}. {t.get('title', 'Concept')}", expanded=(idx==1)):
                st.markdown(f'<div style="font-size: 13px; line-height: 1.5; color: #475569;">{t.get("text", "")}</div>', unsafe_allow_html=True)
    if analogies:
        st.markdown('<div style="font-size: 14px; font-weight: 600; margin-top: 12px;">🧩 Mental Models</div>', unsafe_allow_html=True)
        for a in analogies[:3]:
            st.markdown(f'<div style="background: white; padding: 10px; border-radius: 6px; margin: 6px 0; border-left: 3px solid #F59E0B;"><div style="font-size: 13px;"><b>{a.get("concept")}</b>: {a.get("analogy")}</div><div style="font-size: 12px; color: #64748b; margin-top: 4px;">{a.get("explanation", "")[:100]}</div></div>', unsafe_allow_html=True)

with tab3:
    if actions:
        for idx, action in enumerate(actions[:6], 1):
            st.markdown(f'<div style="background: white; padding: 10px 12px; border-radius: 6px; border-left: 3px solid #10B981; margin: 6px 0;"><span style="color: #64748B; font-size: 12px; font-weight: 600;">{idx}.</span> <span style="font-size: 13px;">{action}</span></div>', unsafe_allow_html=True)

with tab4:
    if quotes:
        for idx, q in enumerate(quotes[:4], 1):
            st.markdown(f'<div style="background: white; padding: 14px; border-radius: 8px; margin: 8px 0; border-left: 3px solid #6366F1;"><div style="font-size: 14px; font-style: italic; color: #1E293B; line-height: 1.5;">"{q}"</div><div style="text-align: right; font-size: 12px; color: #64748B; margin-top: 6px;">— {book.author}</div></div>', unsafe_allow_html=True)

# Related Books
st.markdown(f'<div style="margin-top: 16px; font-size: 14px; font-weight: 600;">🔗 More in {book.genre.name}</div>', unsafe_allow_html=True)
related = get_books_by_genre(book.genre.slug, limit=4)
cols = st.columns(4, gap="small")
for idx, rb in enumerate(related):
    if rb.id != book.id:
        with cols[idx % 4]:
            st.image(load_image_safe(rb.cover_image_url), use_container_width=True)
            st.caption(rb.title[:25] + "..." if len(rb.title) > 25 else rb.title)
            st.link_button("Read", f"/Book_Detail?slug={rb.slug}", use_container_width=True)

# Footer
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.link_button("← Categories", "/Categories", use_container_width=True)
with col2:
    st.link_button("🏠 Home", "/", use_container_width=True)
