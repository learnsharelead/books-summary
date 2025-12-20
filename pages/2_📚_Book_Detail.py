"""
Book Detail Page - With AI Features
Includes: Audio Summaries (TTS), AI Chat (RAG), Smart Recommendations
"""

import streamlit as st
import json
from database.queries import get_book_by_slug, get_summary_for_book, get_books_by_genre, get_all_books
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
.stTabs [data-baseweb="tab-list"] {gap: 8px;}
.stTabs [data-baseweb="tab"] {background: white; border-radius: 8px; padding: 8px 16px; font-weight: 600;}
.stTabs [aria-selected="true"] {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white !important;}
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

# Build book_data dict for AI services
book_data = {
    'title': book.title,
    'author': book.author,
    'genre': book.genre.name if book.genre else 'Unknown',
    'year': book.publication_year,
    'executive_summary': summary.executive_summary,
    'main_content': summary.main_content,
    'overview': summary.overview_text,
    'takeaways': summary.key_takeaways,
    'analogies': summary.analogies,
    'quotes': summary.quotes,
    'action_steps': summary.action_steps,
    'who_should_read': summary.who_should_read
}

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

# AI Features Section - NEW!
st.markdown("---")
st.markdown("""
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
    <span style="font-size: 20px;">✨</span>
    <span style="font-size: 18px; font-weight: 800; color: #1e293b;">AI-Powered Features</span>
    <span style="
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-size: 10px;
        padding: 2px 10px;
        border-radius: 10px;
        font-weight: 600;
    ">NEW</span>
</div>
""", unsafe_allow_html=True)

# Three AI feature tabs
ai_tab1, ai_tab2, ai_tab3 = st.tabs(["🎧 Audio Summary", "🤖 AI Chat", "🎯 Smart Picks"])

with ai_tab1:
    # Audio Summary (TTS)
    from services.tts_service import TTSService
    
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <p style="font-size: 14px; color: #475569; line-height: 1.6;">
            Listen to the executive summary while commuting, exercising, or relaxing. 
            Uses your browser's text-to-speech for offline playback.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Prepare audio text
    audio_text = summary.executive_summary or summary.overview_text or summary.main_content
    
    # Clean up the text for audio (remove markdown)
    import re
    audio_text_clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', audio_text)  # Remove bold
    audio_text_clean = re.sub(r'\*([^*]+)\*', r'\1', audio_text_clean)  # Remove italics
    audio_text_clean = re.sub(r'#{1,6}\s*', '', audio_text_clean)  # Remove headers
    audio_text_clean = re.sub(r'\n{3,}', '\n\n', audio_text_clean)  # Reduce line breaks
    
    TTSService.render_audio_player(
        text=audio_text_clean,
        title=f"📖 {book.title} - Audio Summary",
        show_controls=True
    )
    
    # Additional audio options
    with st.expander("📝 View Text Being Read"):
        st.markdown(f'<div style="background: white; padding: 16px; border-radius: 8px; font-size: 14px; line-height: 1.7; max-height: 300px; overflow-y: auto;">{audio_text_clean[:2000]}...</div>', unsafe_allow_html=True)

with ai_tab2:
    # AI Chat (RAG)
    from components.ai_chat import render_ai_chat
    
    render_ai_chat(
        book_data=book_data,
        book_slug=book_slug,
        expanded=True
    )

with ai_tab3:
    # Smart Recommendations
    from services.recommendations import RecommendationEngine, render_smart_recommendations
    
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <p style="font-size: 14px; color: #475569; line-height: 1.6;">
            Based on the themes, concepts, and style of this book, here are personalized recommendations:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    render_smart_recommendations(
        current_book=book,
        current_summary=summary,
        show_reasons=True
    )

# Tabs for content
st.markdown("---")
st.markdown("""
<div style="margin: 16px 0;">
    <span style="font-size: 18px; font-weight: 800; color: #1e293b;">📖 Book Content</span>
</div>
""", unsafe_allow_html=True)

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
                # Add mini TTS button for each concept
                TTSService.render_mini_player(t.get("text", ""), f"Listen to Concept {idx}")
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
            # Share quote button
            TTSService.render_mini_player(q, "Listen")

# Related Books (non-AI based, genre match)
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
