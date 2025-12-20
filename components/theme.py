"""
Centralized Theme System for BookWise.
Single source of truth for all styling, colors, and theme management.
"""

import streamlit as st
from typing import Dict, Any


# ============================================================================
# COLOR PALETTE
# ============================================================================

COLORS = {
    # Primary Palette
    "primary": "#667eea",
    "primary_dark": "#764ba2",
    "primary_light": "#a78bfa",
    "primary_gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    
    # Secondary/Accent
    "accent": "#f59e0b",
    "accent_gradient": "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
    "success": "#10b981",
    "success_gradient": "linear-gradient(135deg, #10b981 0%, #059669 100%)",
    "warning": "#f59e0b",
    "error": "#ef4444",
    "info": "#3b82f6",
    
    # Genre Colors
    "genres": {
        "self-help": "#667eea",
        "business": "#f093fb",
        "psychology": "#4facfe",
        "finance": "#43e97b",
        "productivity": "#fa709a",
        "philosophy": "#30cfd0",
        "history": "#a8edea",
        "science": "#ff9a9e",
        "biography": "#ffecd2",
        "technology": "#ff6e7f",
    },
    
    # Light Theme
    "light": {
        "background": "#f8fafc",
        "surface": "#ffffff",
        "surface_elevated": "#ffffff",
        "text_primary": "#1e293b",
        "text_secondary": "#64748b",
        "text_muted": "#94a3b8",
        "border": "#e2e8f0",
        "border_light": "#f1f5f9",
        "shadow": "rgba(0, 0, 0, 0.08)",
        "shadow_elevated": "rgba(0, 0, 0, 0.12)",
    },
    
    # Dark Theme
    "dark": {
        "background": "#0f172a",
        "surface": "#1e293b",
        "surface_elevated": "#334155",
        "text_primary": "#f1f5f9",
        "text_secondary": "#94a3b8",
        "text_muted": "#64748b",
        "border": "#334155",
        "border_light": "#475569",
        "shadow": "rgba(0, 0, 0, 0.3)",
        "shadow_elevated": "rgba(0, 0, 0, 0.4)",
    }
}

# ============================================================================
# TYPOGRAPHY
# ============================================================================

TYPOGRAPHY = {
    "font_family_base": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "font_family_display": "'Playfair Display', Georgia, serif",
    
    # Font sizes
    "text_xs": "11px",
    "text_sm": "12px",
    "text_base": "14px",
    "text_lg": "16px",
    "text_xl": "18px",
    "text_2xl": "20px",
    "text_3xl": "24px",
    "text_4xl": "32px",
    "text_5xl": "40px",
    
    # Font weights
    "font_normal": "400",
    "font_medium": "500",
    "font_semibold": "600",
    "font_bold": "700",
    "font_extrabold": "800",
    "font_black": "900",
    
    # Line heights
    "leading_tight": "1.2",
    "leading_normal": "1.5",
    "leading_relaxed": "1.6",
}

# ============================================================================
# SPACING & LAYOUT
# ============================================================================

SPACING = {
    "xs": "4px",
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "xl": "20px",
    "2xl": "24px",
    "3xl": "32px",
    "4xl": "40px",
}

LAYOUT = {
    "max_width": "1200px",
    "border_radius_sm": "6px",
    "border_radius_md": "8px",
    "border_radius_lg": "12px",
    "border_radius_xl": "16px",
    "border_radius_full": "9999px",
}


# ============================================================================
# THEME MANAGEMENT
# ============================================================================

def get_theme() -> str:
    """Get current theme (light or dark)."""
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
    return st.session_state.theme


def set_theme(theme: str) -> None:
    """Set theme (light or dark)."""
    st.session_state.theme = theme


def toggle_theme() -> str:
    """Toggle between light and dark theme. Returns new theme."""
    current = get_theme()
    new_theme = "dark" if current == "light" else "light"
    set_theme(new_theme)
    return new_theme


def get_theme_colors() -> Dict[str, str]:
    """Get colors for current theme."""
    theme = get_theme()
    return COLORS[theme]


def get_genre_color(genre_slug: str) -> str:
    """Get color for a specific genre."""
    return COLORS["genres"].get(genre_slug, COLORS["primary"])


# ============================================================================
# CSS GENERATION
# ============================================================================

def generate_global_css() -> str:
    """Generate global CSS based on current theme."""
    theme = get_theme()
    c = COLORS[theme]
    
    return f"""
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');
    
    /* Hide Streamlit defaults */
    #MainMenu, footer, header {{visibility: hidden;}}
    [data-testid="stSidebarNav"] {{display: none;}}
    
    /* Base styles */
    body {{
        font-family: {TYPOGRAPHY['font_family_base']};
        background: {c['background']};
        color: {c['text_primary']};
    }}
    
    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    
    /* Links */
    a {{
        color: {COLORS['primary']};
        text-decoration: none;
    }}
    
    a:hover {{
        color: {COLORS['primary_dark']};
    }}
    
    /* Buttons */
    div.stButton > button {{
        background: {COLORS['primary_gradient']};
        color: white;
        border: none;
        border-radius: {LAYOUT['border_radius_sm']};
        padding: 6px 12px;
        font-size: {TYPOGRAPHY['text_sm']};
        font-weight: {TYPOGRAPHY['font_semibold']};
        transition: all 0.2s ease;
    }}
    
    div.stButton > button:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 12px {c['shadow_elevated']};
    }}
    
    /* Inputs */
    input[type="text"], .stTextInput > div > div > input {{
        border: 1px solid {c['border']} !important;
        border-radius: {LAYOUT['border_radius_md']} !important;
        padding: 8px 12px !important;
        font-size: {TYPOGRAPHY['text_base']} !important;
        background: {c['surface']} !important;
        color: {c['text_primary']} !important;
    }}
    
    input[type="text"]:focus {{
        border-color: {COLORS['primary']} !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }}
    
    /* Cards */
    .card {{
        background: {c['surface']};
        border-radius: {LAYOUT['border_radius_lg']};
        box-shadow: 0 2px 8px {c['shadow']};
        transition: all 0.2s ease;
    }}
    
    .card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 16px {c['shadow_elevated']};
    }}
    
    /* Hover lift effect */
    .hover-lift {{
        transition: all 0.2s ease;
    }}
    
    .hover-lift:hover {{
        transform: translateY(-3px);
        box-shadow: 0 6px 12px {c['shadow_elevated']};
    }}
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background: {c['surface']};
        padding: 4px;
        border-radius: {LAYOUT['border_radius_md']};
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: {LAYOUT['border_radius_sm']};
        padding: 8px 16px;
        font-weight: {TYPOGRAPHY['font_semibold']};
        color: {c['text_secondary']};
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {COLORS['primary_gradient']};
        color: white !important;
    }}
    
    /* Expander */
    .streamlit-expanderHeader {{
        background: {c['surface']} !important;
        border-radius: {LAYOUT['border_radius_md']} !important;
    }}
    
    /* Scrollbar (dark mode friendly) */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {c['background']};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {c['border']};
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {c['text_muted']};
    }}
    """


def render_global_styles() -> None:
    """Render global CSS styles. Call this at the top of every page."""
    st.markdown(f"<style>{generate_global_css()}</style>", unsafe_allow_html=True)


# ============================================================================
# THEME TOGGLE COMPONENT
# ============================================================================

def render_theme_toggle() -> None:
    """Render a theme toggle button."""
    theme = get_theme()
    icon = "🌙" if theme == "light" else "☀️"
    label = "Dark Mode" if theme == "light" else "Light Mode"
    
    c = get_theme_colors()
    
    # Use JavaScript for smooth toggle
    toggle_id = "theme_toggle_btn"
    
    st.markdown(f"""
    <button id="{toggle_id}" onclick="
        // Toggle theme in session (handled by Streamlit)
        const btn = document.getElementById('{toggle_id}');
        btn.disabled = true;
        btn.textContent = 'Switching...';
    " style="
        background: {c['surface']};
        border: 1px solid {c['border']};
        border-radius: {LAYOUT['border_radius_full']};
        padding: 8px 16px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: {TYPOGRAPHY['text_sm']};
        font-weight: {TYPOGRAPHY['font_medium']};
        color: {c['text_primary']};
        transition: all 0.2s ease;
    ">
        <span>{icon}</span>
        <span>{label}</span>
    </button>
    """, unsafe_allow_html=True)
    
    # Actual toggle through Streamlit
    if st.button(f"{icon} {label}", key="theme_toggle_actual", type="secondary"):
        toggle_theme()
        st.rerun()


def render_inline_theme_toggle() -> bool:
    """Render inline theme toggle, returns True if toggled."""
    theme = get_theme()
    icon = "🌙" if theme == "light" else "☀️"
    
    col1, col2 = st.columns([10, 1])
    with col2:
        if st.button(icon, key="inline_theme_toggle", help=f"Switch to {'dark' if theme == 'light' else 'light'} mode"):
            toggle_theme()
            return True
    return False


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_card_style(elevated: bool = False) -> str:
    """Get CSS style string for a card."""
    c = get_theme_colors()
    shadow = c['shadow_elevated'] if elevated else c['shadow']
    return f"""
        background: {c['surface']};
        border-radius: {LAYOUT['border_radius_lg']};
        box-shadow: 0 2px 8px {shadow};
        border: 1px solid {c['border_light']};
    """


def get_gradient_bg(start_color: str = None, end_color: str = None) -> str:
    """Get gradient background CSS."""
    start = start_color or COLORS['primary']
    end = end_color or COLORS['primary_dark']
    return f"linear-gradient(135deg, {start} 0%, {end} 100%)"
