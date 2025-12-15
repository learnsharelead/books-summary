"""
Privacy Policy - Compact with readable fonts
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer

st.set_page_config(page_title="Privacy | BookWise", page_icon="🔒", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
body {font-family: 'Inter', sans-serif; background: #f8fafc;}
</style>
""", unsafe_allow_html=True)

render_navigation()

st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 32px 20px; text-align: center;"><div style="font-size: 36px; margin-bottom: 8px;">🔒</div><h1 style="font-size: 24px; font-weight: 900; color: white;">Privacy Policy</h1></div>', unsafe_allow_html=True)

st.markdown("""
<div style="max-width: 700px; margin: 24px auto; padding: 0 20px;">
<div style="background: white; padding: 24px; border-radius: 12px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04); font-size: 14px; line-height: 1.7; color: #475569;">

<h4 style="font-size: 16px; color: #1e293b; margin-bottom: 8px;">Information We Collect</h4>
<p style="margin-bottom: 16px;">Usage data, device info, and cookies to improve your experience.</p>

<h4 style="font-size: 16px; color: #1e293b; margin-bottom: 8px;">How We Use It</h4>
<p style="margin-bottom: 16px;">To improve summaries, personalize recommendations, and analyze patterns.</p>

<h4 style="font-size: 16px; color: #1e293b; margin-bottom: 8px;">Data Security</h4>
<p style="margin-bottom: 16px;">HTTPS encryption, secure servers, regular audits.</p>

<h4 style="font-size: 16px; color: #1e293b; margin-bottom: 8px;">Your Rights</h4>
<p style="margin-bottom: 16px;">Access, delete, or opt-out anytime.</p>

<p style="font-size: 12px; color: #94a3b8;"><em>Contact: privacy@bookwise.app • Updated Dec 2024</em></p>

</div></div>
""", unsafe_allow_html=True)

render_footer()
