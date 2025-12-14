"""
About Page - Information about BookWise.
"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="About BookWise",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

css_path = Path(__file__).parent.parent / "assets" / "css" / "styles.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.seo_content import SEO_CONTENT

seo = SEO_CONTENT["about"]
st.markdown(f"""
<title>{seo['title']}</title>
<meta name="description" content="{seo['description']}">
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">ℹ️ About BookWise</h1>
    <p class="hero-subtitle">
        Making book knowledge accessible to everyone through curated summaries.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(seo["content"])

# Stats
st.markdown("---")
st.markdown("## 📊 By the Numbers")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📖 Books", "50+")
with col2:
    st.metric("📚 Genres", "11")
with col3:
    st.metric("⏱️ Hours Saved", "100+")
with col4:
    st.metric("✍️ Expert Written", "100%")

# Team
st.markdown("---")
st.markdown("""
## 👥 Our Team

BookWise is built by a passionate team of readers and lifelong learners 
who believe in the power of books to transform lives.

---

*Questions? Reach out at hello@bookwise.app*
""")

st.markdown("---")
st.caption("📚 BookWise - Curated Book Summaries")
