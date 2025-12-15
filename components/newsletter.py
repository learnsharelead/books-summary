"""
Newsletter - Ultra Compact
"""

import streamlit as st
from datetime import datetime


def render_newsletter_signup(compact: bool = True) -> None:
    """Render ultra-compact newsletter signup."""
    st.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; padding: 12px 16px; margin: 12px 0;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
    <div>
    <h4 style="font-size: 13px; font-weight: 700; color: white; margin: 0;">📬 Weekly Insights</h4>
    <p style="font-size: 10px; color: rgba(255,255,255,0.8); margin: 2px 0 0 0;">Get summaries in your inbox</p>
    </div>
    </div>
    </div>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Email", placeholder="your@email.com", label_visibility="collapsed", key="newsletter_email")
    with col2:
        if st.button("Subscribe", key="subscribe_btn", use_container_width=True):
            if email and "@" in email:
                st.toast("🎉 Subscribed!")
            else:
                st.error("Invalid email")


def get_subscriber_count() -> int:
    return len(st.session_state.get("subscribers", []))
