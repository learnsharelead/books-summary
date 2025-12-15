"""
Testimonials - Compact with readable fonts
"""

import streamlit as st

TESTIMONIALS = [
    {"name": "Sarah J.", "role": "Founder", "image": "👩‍💼", "quote": "50+ summaries read in time it takes to read 3 books!", "rating": 5},
    {"name": "Michael C.", "role": "Engineer", "image": "👨‍💻", "quote": "Action steps are game-changers. Immediate application.", "rating": 5},
    {"name": "Emily R.", "role": "Director", "image": "👩‍🎨", "quote": "Best summary platform I've tried. Exceptional quality.", "rating": 5},
]


def render_testimonials(count: int = 3) -> None:
    """Render compact testimonials with readable fonts."""
    st.markdown('<div style="max-width: 1200px; margin: 16px auto; padding: 0 20px;"><h3 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 12px; text-align: center;">💬 What Readers Say</h3>', unsafe_allow_html=True)
    
    cols = st.columns(count, gap="small")
    for idx, t in enumerate(TESTIMONIALS[:count]):
        with cols[idx]:
            st.markdown(f'''<div style="background: white; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border: 1px solid #f1f5f9; height: 100%;">
            <div style="font-size: 12px; margin-bottom: 8px;">{"⭐" * t["rating"]}</div>
            <p style="font-size: 13px; color: #475569; line-height: 1.5; font-style: italic; margin-bottom: 12px;">"{t["quote"]}"</p>
            <div style="display: flex; align-items: center; gap: 8px;">
            <div style="font-size: 24px;">{t["image"]}</div>
            <div><div style="font-size: 13px; font-weight: 600; color: #1e293b;">{t["name"]}</div><div style="font-size: 11px; color: #64748b;">{t["role"]}</div></div>
            </div></div>''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_stats_with_social_proof() -> None:
    """Render compact stats bar with readable fonts."""
    st.markdown('''
    <div style="background: #1e293b; padding: 16px 20px; margin: 16px 0;">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
    <div style="text-align: center;"><div style="font-size: 24px; font-weight: 800; color: #667eea;">10K+</div><div style="font-size: 12px; color: #94a3b8;">Readers</div></div>
    <div style="text-align: center;"><div style="font-size: 24px; font-weight: 800; color: #f093fb;">4.9</div><div style="font-size: 12px; color: #94a3b8;">Rating</div></div>
    <div style="text-align: center;"><div style="font-size: 24px; font-weight: 800; color: #43e97b;">50K+</div><div style="font-size: 12px; color: #94a3b8;">Hours Saved</div></div>
    <div style="text-align: center;"><div style="font-size: 24px; font-weight: 800; color: #fa709a;">98%</div><div style="font-size: 12px; color: #94a3b8;">Satisfaction</div></div>
    </div>
    </div>
    ''', unsafe_allow_html=True)


def render_testimonials_carousel() -> None:
    """Render single featured quote."""
    t = TESTIMONIALS[0]
    st.markdown(f'''<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 20px; text-align: center; margin: 16px 0;">
    <p style="font-size: 14px; color: white; font-style: italic; margin-bottom: 10px;">"{t["quote"]}"</p>
    <div style="font-size: 12px; color: rgba(255,255,255,0.8);">— {t["name"]}, {t["role"]}</div>
    </div>''', unsafe_allow_html=True)


def get_testimonials():
    return TESTIMONIALS
