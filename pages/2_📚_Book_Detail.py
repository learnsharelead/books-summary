"""
Book Detail Page - Premium Beautiful Design
"""

import streamlit as st
import json
from pathlib import Path
from database.queries import get_book_by_slug, get_summary_for_book, get_books_by_genre
from components.image_handler import load_image_safe

st.set_page_config(page_title="Book Summary", page_icon="📖", layout="wide")

# Load CSS
css_path = Path(__file__).parent.parent / "assets" / "css" / "styles.css"
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Get book
book_slug = st.query_params.get("slug", None)
if not book_slug:
    st.warning("Select a book from the library")
    st.link_button("← Go to Home", "/")
    st.stop()

book = get_book_by_slug(book_slug)
if not book:
    st.error("Book not found")
    st.stop()

summary = get_summary_for_book(book.id)

# Parse JSON fields
def safe_json(val):
    try: return json.loads(val or "[]")
    except: return []

takeaways = safe_json(summary.key_takeaways)
analogies = safe_json(summary.analogies)
quotes = safe_json(summary.quotes)
actions = safe_json(summary.action_steps)

# ===== HEADER =====
col1, col2 = st.columns([1.2, 4], gap="large")

with col1:
    if book.cover_image_url:
        st.image(load_image_safe(book.cover_image_url), use_container_width=True)

with col2:
    st.markdown(f"# {book.title}")
    st.markdown(f"### by {book.author}")
    
    # Metadata pills
    pill_html = f"""
    <div style="display: flex; gap: 10px; flex-wrap: wrap; margin: 20px 0;">
        <span style="background: linear-gradient(135deg, #E8F4FD, #D4E7FF); padding: 8px 16px; 
                     border-radius: 20px; font-size: 14px; font-weight: 500; color: #1E40AF;">
            📚 {book.genre.name}
        </span>
        <span style="background: linear-gradient(135deg, #FFF4E6, #FFE8CC); padding: 8px 16px; 
                     border-radius: 20px; font-size: 14px; font-weight: 500; color: #92400E;">
            ⏱️ {summary.reading_time} min read
        </span>
        <span style="background: linear-gradient(135deg, #F3F4F6, #E5E7EB); padding: 8px 16px; 
                     border-radius: 20px; font-size: 14px; font-weight: 500; color: #374151;">
            📅 {book.publication_year}
        </span>
        <span style="background: linear-gradient(135deg, #FFF8DC, #FFEAA7); padding: 8px 16px; 
                     border-radius: 20px; font-size: 14px; font-weight: 500; color: #78350F;">
            ⭐ {summary.rating}/5.0
        </span>
    </div>
    """
    st.markdown(pill_html, unsafe_allow_html=True)
    
    if summary.quote_of_the_book:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 24px 28px; border-radius: 12px; color: white; margin: 24px 0;
                    border-left: 4px solid #FFD700; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);">
            <div style="font-size: 18px; font-style: italic; line-height: 1.6; font-weight: 300;">
                "{summary.quote_of_the_book}"
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== TABS =====
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Executive Summary", 
    "💡 Key Concepts", 
    "🔄 Visual Framework", 
    "🚀 Action Steps",
    "💬 Quotes"
])

# TAB 1: EXECUTIVE SUMMARY
with tab1:
    st.markdown(f"""
    <div style="background: white; padding: 28px; border-radius: 12px; 
                border-left: 4px solid #6366F1; line-height: 1.8; font-size: 16px; 
                margin: 16px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
        {summary.executive_summary}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #E8F8F5, #D1F2EB); 
                padding: 20px; border-radius: 12px; margin: 20px 0;
                border-left: 4px solid #10B981;">
        <div style="font-weight: 600; color: #065F46; margin-bottom: 10px; font-size: 16px;">
            👥 Perfect For
        </div>
        <div style="font-size: 15px; line-height: 1.7; color: #047857;">
            {}
        </div>
    </div>
    """.format(summary.who_should_read), unsafe_allow_html=True)

# TAB 2: KEY CONCEPTS
with tab2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px 24px; border-radius: 12px; margin: 16px 0;
                box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);">
        <div style="color: white; font-weight: 600; font-size: 18px; margin-bottom: 4px;">
            💡 Core Concepts & Frameworks
        </div>
        <div style="color: rgba(255,255,255,0.9); font-size: 14px;">
            Expand each concept to explore in detail
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not takeaways:
        st.info("📚 Key concepts are being curated for this book.")
    else:
        for idx, t in enumerate(takeaways, 1):
            with st.expander(f"**{idx}. {t.get('title', 'Key Concept')}**", expanded=(idx==1)):
                st.markdown(f"""
                <div style="background: #FAFBFC; padding: 20px; border-radius: 8px; 
                            line-height: 1.7; font-size: 15px; color: #1E293B;">
                    {t.get('text', '')}
                </div>
                """, unsafe_allow_html=True)
    
    if analogies:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF8DC, #FFEAA7); 
                    padding: 16px 20px; border-radius: 12px; margin: 20px 0;">
            <div style="color: #92400E; font-weight: 600; font-size: 17px; margin-bottom: 4px;">
                🧩 Mental Models & Analogies
            </div>
            <div style="color: #78350F; font-size: 13px;">
                Real-world examples to crystallize understanding
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        for a in analogies:
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 10px; 
                        margin: 12px 0; border-left: 4px solid #F59E0B;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
                <div style="font-weight: 600; color: #1E293B; margin-bottom: 10px; font-size: 16px;">
                    {a.get('concept')} — <em style="color: #64748B; font-weight: 400;">{a.get('analogy')}</em>
                </div>
                <div style="color: #475569; line-height: 1.7; font-size: 15px;">
                    {a.get('explanation', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)

# TAB 3: VISUAL MAP
with tab3:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                padding: 20px 24px; border-radius: 12px; margin: 16px 0;
                box-shadow: 0 4px 12px rgba(240, 147, 251, 0.3);">
        <div style="color: white; font-weight: 600; font-size: 18px; margin-bottom: 4px;">
            📊 Visual Framework Map
        </div>
        <div style="color: rgba(255,255,255,0.9); font-size: 14px;">
            A diagram of the book's core model and how concepts interconnect
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if summary.workflow_data:
        st.markdown("<div style='background: white; padding: 24px; border-radius: 12px; margin: 20px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.06);'>", unsafe_allow_html=True)
        st.graphviz_chart(summary.workflow_data, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.info("💡 **Tip**: This diagram visualizes the book's unique framework and how key ideas connect")
    else:
        st.warning("📌 Visual diagram is being created for this book")

# TAB 4: ACTION GUIDE
with tab4:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                padding: 20px 24px; border-radius: 12px; margin: 16px 0;
                box-shadow: 0 4px 12px rgba(250, 112, 154, 0.3);">
        <div style="color: white; font-weight: 600; font-size: 18px; margin-bottom: 4px;">
            🚀 Actionable Steps
        </div>
        <div style="color: rgba(255,255,255,0.95); font-size: 14px;">
            Practical strategies to implement what you've learned
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not actions:
        st.info("📋 Action steps are being curated for this book.")
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        for idx, action in enumerate(actions, 1):
            col_check, col_text = st.columns([0.5, 9.5])
            with col_check:
                st.checkbox("", key=f"action_{idx}", label_visibility="collapsed")
            with col_text:
                st.markdown(f"""
                <div style="background: white; padding: 14px 18px; border-radius: 8px; 
                            border-left: 4px solid #10B981; margin-bottom: 10px;
                            box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
                    <span style="color: #64748B; font-weight: 600; margin-right: 10px; font-size: 14px;">
                        {idx}.
                    </span>
                    <span style="color: #1E293B; font-size: 15px; line-height: 1.6;">
                        {action}
                    </span>
                </div>
                """, unsafe_allow_html=True)

# TAB 5: QUOTES
with tab5:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                padding: 20px 24px; border-radius: 12px; margin: 16px 0;
                box-shadow: 0 4px 12px rgba(79, 172, 254, 0.3);">
        <div style="color: white; font-weight: 600; font-size: 18px; margin-bottom: 4px;">
            💬 Memorable Quotes
        </div>
        <div style="color: rgba(255,255,255,0.95); font-size: 14px;">
            Key insights worth remembering and sharing
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not quotes:
        st.info("💭 Quotes are being curated for this book.")
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        for idx, q in enumerate(quotes, 1):
            st.markdown(f"""
            <div style="background: white; padding: 28px; border-radius: 12px; 
                        margin: 20px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                        border-left: 5px solid #6366F1;">
                <div style="font-size: 11px; color: #94A3B8; margin-bottom: 12px; 
                            font-weight: 600; letter-spacing: 1px;">
                    QUOTE #{idx}
                </div>
                <div style="font-size: 19px; font-style: italic; color: #1E293B; 
                            line-height: 1.7; font-family: Georgia, serif; margin-bottom: 16px;">
                    "{q}"
                </div>
                <div style="text-align: right; color: #64748B; font-size: 14px; font-weight: 500;">
                    — {book.author}
                </div>
            </div>
            """, unsafe_allow_html=True)

# ===== RELATED BOOKS =====
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="background: white; padding: 18px 24px; border-radius: 12px; margin: 24px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
    <div style="color: #1E293B; font-weight: 600; font-size: 20px;">
        🔗 More Books in {}
    </div>
</div>
""".format(book.genre.name), unsafe_allow_html=True)

related_books = get_books_by_genre(book.genre.slug, limit=4)
cols = st.columns(4)

for idx, rb in enumerate(related_books):
    if rb.id != book.id:
        with cols[idx % 4]:
            st.image(load_image_safe(rb.cover_image_url), use_container_width=True)
            st.markdown(f"**{rb.title}**")
            st.caption(f"by {rb.author}")
            st.link_button("Read Summary →", f"/Book_Detail?slug={rb.slug}", use_container_width=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
col_back, col_home = st.columns([1, 1])
with col_back:
    st.link_button("← Browse All Categories", "/Categories", use_container_width=True)
with col_home:
    st.link_button("🏠 Back to Home", "/", use_container_width=True)
