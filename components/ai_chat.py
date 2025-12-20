"""
AI Chat Component for BookWise.
Provides conversational interface to chat with book content.
"""

import streamlit as st
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChatMessage:
    """Chat message data structure."""
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: str = None
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().strftime("%H:%M")


def get_chat_history(book_slug: str) -> List[ChatMessage]:
    """Get chat history for a specific book."""
    if 'book_chats' not in st.session_state:
        st.session_state.book_chats = {}
    
    if book_slug not in st.session_state.book_chats:
        st.session_state.book_chats[book_slug] = []
    
    return st.session_state.book_chats[book_slug]


def add_message(book_slug: str, role: str, content: str) -> None:
    """Add a message to chat history."""
    history = get_chat_history(book_slug)
    history.append(ChatMessage(role=role, content=content))


def clear_chat(book_slug: str) -> None:
    """Clear chat history for a book."""
    if 'book_chats' in st.session_state:
        st.session_state.book_chats[book_slug] = []


def render_ai_chat(
    book_data: Dict[str, Any],
    book_slug: str,
    expanded: bool = False
) -> None:
    """
    Render the AI chat interface for a book.
    
    Args:
        book_data: Dictionary with book and summary information
        book_slug: Book slug for session management
        expanded: Whether to show expanded by default
    """
    from services.ai_service import get_ai_service, ChatMessage as AIMessage
    
    # Initialize AI service
    ai_service = get_ai_service()
    
    # Check for API key
    has_api_key = bool(ai_service.api_key)
    
    # Chat container
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border-radius: 16px;
        padding: 20px;
        margin: 20px 0;
    ">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
            <div style="
                width: 40px; height: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
            ">🤖</div>
            <div>
                <div style="font-size: 16px; font-weight: 700; color: white;">
                    Chat with this Book
                </div>
                <div style="font-size: 12px; color: #94a3b8;">
                    Ask questions about concepts, get explanations, and explore ideas
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not has_api_key:
        st.warning("🔑 To use AI Chat, please set your **GEMINI_API_KEY** in environment variables or Streamlit secrets.")
        
        with st.expander("How to set up API key"):
            st.markdown("""
            **Option 1: Environment Variable**
            ```bash
            export GEMINI_API_KEY=your_api_key_here
            ```
            
            **Option 2: Streamlit Secrets**
            Create `.streamlit/secrets.toml`:
            ```toml
            GEMINI_API_KEY = "your_api_key_here"
            ```
            
            **Get your API key:**
            Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
            """)
        
        # Still show the interface but disabled
        st.text_input(
            "Ask a question...",
            placeholder="Configure API key to start chatting",
            disabled=True,
            key="chat_disabled"
        )
        return
    
    # Get chat history
    history = get_chat_history(book_slug)
    
    # Display chat history
    chat_container = st.container()
    
    with chat_container:
        if not history:
            # Welcome message
            st.markdown("""
            <div style="
                background: rgba(102, 126, 234, 0.1);
                border-radius: 12px;
                padding: 16px;
                margin-bottom: 12px;
                border-left: 4px solid #667eea;
            ">
                <div style="font-size: 14px; color: #475569; line-height: 1.6;">
                    👋 <strong>Welcome!</strong> I'm your AI reading companion. Ask me anything about 
                    <strong>"{book_data.get('title', 'this book')}"</strong>:
                    <ul style="margin: 8px 0 0 0; padding-left: 20px;">
                        <li>Explain key concepts in simple terms</li>
                        <li>How can I apply these ideas?</li>
                        <li>What's the main argument?</li>
                        <li>Create a quiz to test my understanding</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Display messages
            for msg in history:
                if msg.role == 'user':
                    st.markdown(f"""
                    <div style="
                        display: flex;
                        justify-content: flex-end;
                        margin-bottom: 12px;
                    ">
                        <div style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            padding: 12px 16px;
                            border-radius: 16px 16px 4px 16px;
                            max-width: 80%;
                            font-size: 14px;
                            line-height: 1.5;
                        ">
                            {msg.content}
                            <div style="font-size: 10px; opacity: 0.7; text-align: right; margin-top: 4px;">
                                {msg.timestamp}
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="
                        display: flex;
                        justify-content: flex-start;
                        margin-bottom: 12px;
                    ">
                        <div style="
                            background: #f1f5f9;
                            color: #1e293b;
                            padding: 12px 16px;
                            border-radius: 16px 16px 16px 4px;
                            max-width: 85%;
                            font-size: 14px;
                            line-height: 1.6;
                        ">
                            <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 8px;">
                                <span style="font-size: 16px;">🤖</span>
                                <span style="font-weight: 600; color: #667eea;">BookWise AI</span>
                            </div>
                            {msg.content}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Input section
    col1, col2 = st.columns([6, 1])
    
    with col1:
        user_input = st.text_input(
            "Ask a question",
            placeholder=f"Ask anything about '{book_data.get('title', 'this book')}'...",
            label_visibility="collapsed",
            key=f"chat_input_{book_slug}"
        )
    
    with col2:
        send_clicked = st.button("Send", use_container_width=True, key=f"send_{book_slug}")
    
    # Quick question buttons
    st.markdown("<div style='margin-top: 8px;'>", unsafe_allow_html=True)
    quick_cols = st.columns(4)
    quick_questions = [
        "📚 Summarize in 3 points",
        "🎯 Key takeaways",
        "💡 How to apply this?",
        "🧠 Quiz me!"
    ]
    
    quick_question = None
    for idx, q in enumerate(quick_questions):
        with quick_cols[idx]:
            if st.button(q, key=f"quick_{idx}_{book_slug}", use_container_width=True):
                quick_question = q.split(' ', 1)[1]  # Remove emoji
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Handle send
    question = user_input if send_clicked and user_input else quick_question
    
    if question:
        # Add user message
        add_message(book_slug, 'user', question)
        
        # Convert history to AI format
        ai_history = [
            AIMessage(role=m.role, content=m.content)
            for m in history
        ]
        
        # Get AI response
        with st.spinner("Thinking..."):
            response = ai_service.chat_with_book(
                user_message=question,
                book_data=book_data,
                chat_history=ai_history
            )
        
        # Add assistant response
        add_message(book_slug, 'assistant', response)
        
        # Rerun to show new messages
        st.rerun()
    
    # Clear chat button
    if history:
        if st.button("🗑️ Clear Chat", key=f"clear_{book_slug}"):
            clear_chat(book_slug)
            st.rerun()


def render_compact_chat_button(book_slug: str, book_title: str) -> None:
    """Render a compact chat button that opens the full chat."""
    st.markdown(f"""
    <a href="?slug={book_slug}&chat=open" style="text-decoration: none;">
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.2s;
            cursor: pointer;
        " onmouseover="this.style.transform='translateY(-2px)'" 
           onmouseout="this.style.transform='translateY(0)'">
            <span style="font-size: 24px;">🤖</span>
            <div>
                <div style="font-size: 14px; font-weight: 600; color: white;">
                    Chat with AI
                </div>
                <div style="font-size: 11px; color: rgba(255,255,255,0.8);">
                    Ask questions about {book_title[:30]}...
                </div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)
