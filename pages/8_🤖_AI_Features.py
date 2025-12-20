"""
AI Features Hub - Personalized Recommendations & Book Discovery
"""

import streamlit as st
from database.queries import get_all_books, get_top_rated_books, get_all_genres
from components.image_handler import load_image_safe
from components.navigation import render_navigation
from components.footer import render_footer

st.set_page_config(page_title="AI Features | BookWise", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
body {font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b;}
div.stButton > button {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 600; transition: all 0.2s ease;}
div.stButton > button:hover {transform: translateY(-1px);}
</style>
""", unsafe_allow_html=True)

render_navigation(active_page="AI Features")

# Hero Section
st.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%);">
<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px; text-align: center;">
    <div style="
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 8px 20px;
        border-radius: 20px;
        margin-bottom: 16px;
    ">
        <span style="font-size: 14px; font-weight: 600; color: white;">✨ AI-Powered Features</span>
    </div>
    <h1 style="font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 900; color: white; margin-bottom: 12px; line-height: 1.2;">
        Your Personal <span style="color: #a78bfa;">Reading Assistant</span>
    </h1>
    <p style="font-size: 16px; color: rgba(255, 255, 255, 0.8); max-width: 600px; margin: 0 auto;">
        Discover books tailored to your interests, listen to audio summaries, and have AI-powered conversations about any book.
    </p>
</div>
</div>
""", unsafe_allow_html=True)

# Feature Cards
st.markdown('<div style="max-width: 1200px; margin: -30px auto 0 auto; padding: 0 20px; position: relative; z-index: 10;">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div style="
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        height: 100%;
    ">
        <div style="
            width: 56px; height: 56px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
        ">🎧</div>
        <h3 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 8px;">
            Audio Summaries
        </h3>
        <p style="font-size: 14px; color: #64748b; line-height: 1.6; margin-bottom: 16px;">
            Listen to book summaries on the go. Perfect for commutes, workouts, or relaxing. 
            Works offline using your browser's text-to-speech.
        </p>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Offline Ready</span>
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Speed Control</span>
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Progress Tracking</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        height: 100%;
    ">
        <div style="
            width: 56px; height: 56px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
        ">🤖</div>
        <h3 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 8px;">
            AI Book Chat
        </h3>
        <p style="font-size: 14px; color: #64748b; line-height: 1.6; margin-bottom: 16px;">
            Have a conversation with any book! Ask questions, get explanations, 
            and explore concepts deeper with our Gemini-powered AI assistant.
        </p>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">RAG Powered</span>
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Context Aware</span>
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Quiz Mode</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        height: 100%;
    ">
        <div style="
            width: 56px; height: 56px;
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
        ">🎯</div>
        <h3 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 8px;">
            Smart Recommendations
        </h3>
        <p style="font-size: 14px; color: #64748b; line-height: 1.6; margin-bottom: 16px;">
            Get personalized book suggestions based on themes, concepts, and your reading history. 
            Never run out of great books to read.
        </p>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Content-Based</span>
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Match Score</span>
            <span style="background: #f3f4f6; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #475569;">Personalized</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Personalized Recommendations Section
st.markdown("""
<div style="max-width: 1200px; margin: 40px auto 0 auto; padding: 0 20px;">
    <h2 style="font-size: 24px; font-weight: 800; color: #1e293b; margin-bottom: 8px;">
        🎯 Recommended For You
    </h2>
    <p style="font-size: 14px; color: #64748b; margin-bottom: 20px;">
        Based on popular books and top ratings
    </p>
</div>
""", unsafe_allow_html=True)

# Get top rated books for recommendations
top_books = get_top_rated_books(limit=6)

if top_books:
    st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">', unsafe_allow_html=True)
    cols = st.columns(6, gap="small")
    for idx, book in enumerate(top_books):
        with cols[idx]:
            safe_image = load_image_safe(book.cover_image_url, "book")
            st.markdown(f'''
            <div style="
                background: white;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                transition: all 0.2s;
            " onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.12)'"
               onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 8px rgba(0,0,0,0.08)'">
                <div style="position: relative; padding-top: 140%; background: #f8fafc;">
                    <img src="{safe_image}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
                    <div style="
                        position: absolute;
                        top: 8px; left: 8px;
                        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                        color: white;
                        font-size: 10px;
                        padding: 3px 8px;
                        border-radius: 10px;
                        font-weight: 600;
                    ">⭐ Top Rated</div>
                </div>
                <div style="padding: 12px;">
                    <h4 style="
                        font-size: 13px;
                        font-weight: 700;
                        color: #1e293b;
                        line-height: 1.3;
                        display: -webkit-box;
                        -webkit-line-clamp: 2;
                        -webkit-box-orient: vertical;
                        overflow: hidden;
                        margin: 0;
                    ">{book.title}</h4>
                    <p style="font-size: 11px; color: #64748b; margin: 4px 0 0 0;">
                        {book.author}
                    </p>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            st.link_button("▶️ Try AI Features", f"/Book_Detail?slug={book.slug}", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# How It Works Section
st.markdown("""
<div style="background: #f8fafc; padding: 40px 20px; margin-top: 40px;">
<div style="max-width: 1200px; margin: 0 auto;">
    <h2 style="font-size: 24px; font-weight: 800; color: #1e293b; margin-bottom: 24px; text-align: center;">
        How It Works
    </h2>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;">
        <div style="text-align: center;">
            <div style="
                width: 48px; height: 48px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                color: white;
                font-weight: 700;
                margin: 0 auto 12px auto;
            ">1</div>
            <h4 style="font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 4px;">Choose a Book</h4>
            <p style="font-size: 12px; color: #64748b;">Browse our library of 290+ summaries</p>
        </div>
        <div style="text-align: center;">
            <div style="
                width: 48px; height: 48px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                color: white;
                font-weight: 700;
                margin: 0 auto 12px auto;
            ">2</div>
            <h4 style="font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 4px;">Pick Your Mode</h4>
            <p style="font-size: 12px; color: #64748b;">Read, Listen, or Chat with AI</p>
        </div>
        <div style="text-align: center;">
            <div style="
                width: 48px; height: 48px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                color: white;
                font-weight: 700;
                margin: 0 auto 12px auto;
            ">3</div>
            <h4 style="font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 4px;">Learn Deeply</h4>
            <p style="font-size: 12px; color: #64748b;">Ask questions, get insights</p>
        </div>
        <div style="text-align: center;">
            <div style="
                width: 48px; height: 48px;
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                color: white;
                font-weight: 700;
                margin: 0 auto 12px auto;
            ">4</div>
            <h4 style="font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 4px;">Get Recommendations</h4>
            <p style="font-size: 12px; color: #64748b;">Discover your next great read</p>
        </div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# API Key Setup Section
st.markdown("""
<div style="max-width: 1200px; margin: 40px auto; padding: 0 20px;">
    <div style="
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-radius: 16px;
        padding: 24px;
        border-left: 4px solid #f59e0b;
    ">
        <h3 style="font-size: 16px; font-weight: 700; color: #92400e; margin-bottom: 8px;">
            🔑 Setup Instructions for AI Chat
        </h3>
        <p style="font-size: 14px; color: #78350f; line-height: 1.6; margin-bottom: 12px;">
            The Audio Summary and Smart Recommendations work out of the box! 
            For AI Chat, you'll need a free Gemini API key.
        </p>
        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
            <a href="https://aistudio.google.com/app/apikey" target="_blank" style="
                background: #f59e0b;
                color: white;
                padding: 8px 16px;
                border-radius: 8px;
                text-decoration: none;
                font-size: 13px;
                font-weight: 600;
                display: inline-flex;
                align-items: center;
                gap: 6px;
            ">🔗 Get Free API Key</a>
            <span style="
                background: white;
                color: #78350f;
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 12px;
                font-family: monospace;
            ">Add to .streamlit/secrets.toml: GEMINI_API_KEY = "your_key"</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div style="max-width: 1200px; margin: 40px auto; padding: 0 20px; text-align: center;">
    <h2 style="font-size: 28px; font-weight: 800; color: #1e293b; margin-bottom: 12px;">
        Ready to Experience AI-Powered Reading?
    </h2>
    <p style="font-size: 16px; color: #64748b; margin-bottom: 24px;">
        Pick any book and explore all three AI features.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.link_button("📚 Browse Library", "/Categories", use_container_width=True)

render_footer()
