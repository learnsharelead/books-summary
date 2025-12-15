"""
Genre themes for BookWise.
Provides unique colors and styling for each genre.
"""

# Genre color themes
GENRE_THEMES = {
    "self-improvement": {
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "primary": "#667eea",
        "secondary": "#764ba2",
        "light": "#e0e7ff",
        "icon": "🎯"
    },
    "productivity": {
        "gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
        "primary": "#fa709a",
        "secondary": "#fee140",
        "light": "#fef3c7",
        "icon": "⚡"
    },
    "finance": {
        "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
        "primary": "#43e97b",
        "secondary": "#38f9d7",
        "light": "#d1fae5",
        "icon": "💰"
    },
    "psychology": {
        "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "primary": "#4facfe",
        "secondary": "#00f2fe",
        "light": "#dbeafe",
        "icon": "🧠"
    },
    "leadership": {
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "primary": "#f093fb",
        "secondary": "#f5576c",
        "light": "#fce7f3",
        "icon": "👔"
    },
    "entrepreneurship": {
        "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
        "primary": "#ff9a9e",
        "secondary": "#fecfef",
        "light": "#ffe4e6",
        "icon": "🚀"
    },
    "communication": {
        "gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
        "primary": "#a8edea",
        "secondary": "#fed6e3",
        "light": "#cffafe",
        "icon": "💬"
    },
    "philosophy": {
        "gradient": "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
        "primary": "#30cfd0",
        "secondary": "#330867",
        "light": "#c7d2fe",
        "icon": "🏛️"
    },
    "health": {
        "gradient": "linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%)",
        "primary": "#84fab0",
        "secondary": "#8fd3f4",
        "light": "#d1fae5",
        "icon": "❤️"
    },
    "creativity": {
        "gradient": "linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)",
        "primary": "#a18cd1",
        "secondary": "#fbc2eb",
        "light": "#f3e8ff",
        "icon": "🎨"
    },
    # Default theme
    "default": {
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "primary": "#667eea",
        "secondary": "#764ba2",
        "light": "#e0e7ff",
        "icon": "📚"
    }
}


def get_genre_theme(genre_slug: str) -> dict:
    """
    Get theme for a genre.
    
    Args:
        genre_slug: The genre's slug
    
    Returns:
        dict: Theme colors and gradient
    """
    return GENRE_THEMES.get(genre_slug, GENRE_THEMES["default"])


def get_genre_gradient(genre_slug: str) -> str:
    """Get just the gradient for a genre."""
    theme = get_genre_theme(genre_slug)
    return theme["gradient"]


def get_genre_primary(genre_slug: str) -> str:
    """Get primary color for a genre."""
    theme = get_genre_theme(genre_slug)
    return theme["primary"]


def apply_genre_theme_css(genre_slug: str) -> str:
    """
    Generate CSS for a genre theme.
    
    Args:
        genre_slug: The genre's slug
    
    Returns:
        str: CSS string with theme variables
    """
    theme = get_genre_theme(genre_slug)
    
    return f"""
    <style>
    :root {{
        --genre-gradient: {theme['gradient']};
        --genre-primary: {theme['primary']};
        --genre-secondary: {theme['secondary']};
        --genre-light: {theme['light']};
    }}
    
    .genre-header {{
        background: {theme['gradient']};
    }}
    
    .genre-accent {{
        color: {theme['primary']};
    }}
    
    .genre-badge {{
        background: {theme['light']};
        color: {theme['primary']};
    }}
    
    .genre-btn {{
        background: {theme['gradient']} !important;
    }}
    </style>
    """


def render_genre_header(genre_name: str, genre_slug: str, book_count: int) -> str:
    """
    Generate HTML for a themed genre header.
    
    Args:
        genre_name: Display name of the genre
        genre_slug: Slug of the genre
        book_count: Number of books in genre
    
    Returns:
        str: HTML string for header
    """
    theme = get_genre_theme(genre_slug)
    
    return f"""
    <div style="background: {theme['gradient']}; padding: 60px 32px; 
                border-radius: 0 0 24px 24px; margin-bottom: 32px;">
    <div style="max-width: 1200px; margin: 0 auto; text-align: center;">
    <div style="font-size: 64px; margin-bottom: 16px;">{theme['icon']}</div>
    <h1 style="font-family: 'Playfair Display', serif; font-size: 42px; font-weight: 900;
               color: white; margin-bottom: 12px;">{genre_name}</h1>
    <p style="font-size: 16px; color: rgba(255,255,255,0.9);">
    {book_count} book summaries to accelerate your growth
    </p>
    </div>
    </div>
    """


def get_all_themes() -> dict:
    """Get all genre themes."""
    return GENRE_THEMES
