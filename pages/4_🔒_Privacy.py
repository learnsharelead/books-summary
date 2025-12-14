"""
Privacy Policy Page.
"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Privacy Policy | BookWise",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

css_path = Path(__file__).parent.parent / "assets" / "css" / "styles.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.seo_content import SEO_CONTENT

seo = SEO_CONTENT["privacy"]
st.markdown(f"""
<title>{seo['title']}</title>
<meta name="description" content="{seo['description']}">
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🔒 Privacy Policy</h1>
    <p class="hero-subtitle">
        Your privacy matters to us. Here's how we handle your data.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(seo["content"])

st.markdown("---")
st.caption("📚 BookWise - Curated Book Summaries")
