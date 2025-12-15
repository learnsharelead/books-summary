"""
Theme management for BookWise.
Provides dark/light mode toggle functionality.
"""

import streamlit as st


def init_theme() -> None:
    """Initialize theme in session state."""
    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"


def get_current_theme() -> str:
    """Get current theme setting."""
    init_theme()
    return st.session_state["theme"]


def toggle_theme() -> None:
    """Toggle between dark and light themes."""
    init_theme()
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"


def render_theme_toggle() -> None:
    """Render the theme toggle button."""
    init_theme()
    
    current_theme = st.session_state["theme"]
    icon = "🌙" if current_theme == "light" else "☀️"
    label = "Dark Mode" if current_theme == "light" else "Light Mode"
    
    if st.button(f"{icon}", key="theme_toggle", help=f"Switch to {label}"):
        toggle_theme()
        st.rerun()


def get_theme_css() -> str:
    """Get CSS for current theme."""
    init_theme()
    
    if st.session_state["theme"] == "dark":
        return """
        <style>
        /* Dark Theme */
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-card: #1e293b;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --border-color: #334155;
            --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        body, .stApp {
            background-color: #0f172a !important;
            color: #f1f5f9 !important;
        }
        
        .block-container {
            background-color: #0f172a !important;
        }
        
        /* Cards */
        .hover-lift, [data-testid="stVerticalBlock"] > div {
            background-color: #1e293b !important;
            border-color: #334155 !important;
        }
        
        /* Text */
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: #f1f5f9 !important;
        }
        
        /* Navigation */
        [data-testid="stHeader"] {
            background-color: rgba(15, 23, 42, 0.95) !important;
        }
        
        /* Inputs */
        input[type="text"], textarea {
            background-color: #1e293b !important;
            color: #f1f5f9 !important;
            border-color: #334155 !important;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #1e293b !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            color: #94a3b8 !important;
        }
        
        .stTabs [aria-selected="true"] {
            color: #f1f5f9 !important;
        }
        
        /* Expanders */
        .streamlit-expanderHeader {
            background-color: #1e293b !important;
            color: #f1f5f9 !important;
        }
        
        .streamlit-expanderContent {
            background-color: #0f172a !important;
        }
        </style>
        """
    else:
        return """
        <style>
        /* Light Theme (Default) */
        :root {
            --bg-primary: #f8fafc;
            --bg-secondary: #ffffff;
            --bg-card: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --border-color: #e2e8f0;
            --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        body, .stApp {
            background-color: #f8fafc !important;
            color: #1e293b !important;
        }
        </style>
        """


def apply_theme() -> None:
    """Apply the current theme CSS to the page."""
    css = get_theme_css()
    st.markdown(css, unsafe_allow_html=True)


def render_theme_toggle_inline() -> str:
    """
    Get HTML for inline theme toggle (for use in navigation).
    Note: This returns HTML only, actual toggle needs Streamlit button.
    """
    init_theme()
    current_theme = st.session_state["theme"]
    icon = "🌙" if current_theme == "light" else "☀️"
    
    return f"""
    <div style="cursor: pointer; padding: 8px; border-radius: 50%; 
                background: rgba(102, 126, 234, 0.1); font-size: 18px;"
         title="Toggle theme">
        {icon}
    </div>
    """
