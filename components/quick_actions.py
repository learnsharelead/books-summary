"""
Quick Actions component for BookWise.
Floating action buttons for common actions.
"""

import streamlit as st


def render_quick_actions() -> None:
    """
    Render floating quick action buttons.
    Appears in the bottom-right corner.
    """
    st.markdown("""
    <style>
    .quick-actions {
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 9999;
        display: flex;
        flex-direction: column;
        gap: 12px;
        align-items: flex-end;
    }
    
    .quick-action-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 24px;
        text-decoration: none;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .quick-action-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5);
    }
    
    .quick-action-btn.secondary {
        width: 48px;
        height: 48px;
        font-size: 20px;
        background: white;
        color: #667eea;
        box-shadow: 0 2px 12px rgba(0,0,0,0.15);
    }
    
    .quick-action-btn.secondary:hover {
        background: #f8fafc;
    }
    
    /* Hide on mobile */
    @media (max-width: 640px) {
        .quick-actions {
            bottom: 16px;
            right: 16px;
        }
        
        .quick-action-btn {
            width: 48px;
            height: 48px;
            font-size: 20px;
        }
        
        .quick-action-btn.secondary {
            width: 40px;
            height: 40px;
            font-size: 16px;
        }
    }
    </style>
    
    <div class="quick-actions">
        <a href="#top" class="quick-action-btn secondary" title="Back to Top">
            ⬆️
        </a>
        <a href="/Categories" class="quick-action-btn secondary" title="Browse Categories">
            📚
        </a>
        <a href="/" class="quick-action-btn" title="Home">
            🏠
        </a>
    </div>
    """, unsafe_allow_html=True)


def render_scroll_to_top() -> None:
    """Render a scroll-to-top button only."""
    st.markdown("""
    <style>
    .scroll-top-btn {
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 9999;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        opacity: 0.9;
    }
    
    .scroll-top-btn:hover {
        transform: translateY(-4px);
        opacity: 1;
    }
    </style>
    
    <a href="#top" class="scroll-top-btn" title="Back to Top">
        ⬆️
    </a>
    """, unsafe_allow_html=True)


def render_help_fab() -> None:
    """Render a help floating action button."""
    st.markdown("""
    <style>
    .help-fab {
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 9999;
    }
    
    .help-fab-btn {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        color: white;
        font-size: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        box-shadow: 0 4px 20px rgba(67, 233, 123, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .help-fab-btn:hover {
        transform: rotate(90deg) scale(1.1);
    }
    </style>
    
    <div class="help-fab">
        <a href="/About" class="help-fab-btn" title="Need Help?">
            ❓
        </a>
    </div>
    """, unsafe_allow_html=True)


def render_action_bar() -> None:
    """Render horizontal action bar at bottom of page."""
    st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; right: 0; z-index: 1000;
                background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                border-top: 1px solid #e2e8f0; padding: 12px 24px;
                display: flex; justify-content: center; gap: 24px;">
    <a href="/" style="display: flex; flex-direction: column; align-items: center; 
                       text-decoration: none; color: #667eea; font-size: 12px;">
        <span style="font-size: 24px;">🏠</span>
        Home
    </a>
    <a href="/Categories" style="display: flex; flex-direction: column; align-items: center; 
                                  text-decoration: none; color: #64748b; font-size: 12px;">
        <span style="font-size: 24px;">📚</span>
        Categories
    </a>
    <a href="/Reading_Lists" style="display: flex; flex-direction: column; align-items: center; 
                                     text-decoration: none; color: #64748b; font-size: 12px;">
        <span style="font-size: 24px;">📋</span>
        Lists
    </a>
    <a href="/About" style="display: flex; flex-direction: column; align-items: center; 
                            text-decoration: none; color: #64748b; font-size: 12px;">
        <span style="font-size: 24px;">ℹ️</span>
        About
    </a>
    </div>
    
    <!-- Add padding at bottom to prevent content being hidden -->
    <div style="height: 80px;"></div>
    """, unsafe_allow_html=True)
