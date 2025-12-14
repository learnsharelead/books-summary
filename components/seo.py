"""
SEO components for BookWise.
Handles meta tags, Open Graph, and structured data injection.
"""

import streamlit as st
import json
from typing import Optional, Dict, Any


def inject_seo_meta(
    title: str,
    description: str,
    keywords: Optional[str] = None,
    og_image: Optional[str] = None,
    og_type: str = "website",
    canonical_url: Optional[str] = None,
    structured_data: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Inject SEO meta tags into the page.
    
    Args:
        title: Page title
        description: Meta description
        keywords: Comma-separated keywords
        og_image: Open Graph image URL
        og_type: Open Graph type (website, article, book)
        canonical_url: Canonical URL for the page
        structured_data: JSON-LD structured data
    """
    # Set page title
    st.set_page_config(
        page_title=title,
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Build meta tags HTML
    meta_html = f"""
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="{og_type}">
    """
    
    if keywords:
        meta_html += f'<meta name="keywords" content="{keywords}">\n'
    
    if og_image:
        meta_html += f'<meta property="og:image" content="{og_image}">\n'
    
    if canonical_url:
        meta_html += f'<link rel="canonical" href="{canonical_url}">\n'
    
    # Add structured data
    if structured_data:
        meta_html += f"""
        <script type="application/ld+json">
        {json.dumps(structured_data)}
        </script>
        """
    
    st.markdown(meta_html, unsafe_allow_html=True)


def get_page_seo(page_type: str, **kwargs) -> Dict[str, Any]:
    """
    Get SEO configuration for different page types.
    
    Args:
        page_type: Type of page (home, category, book, about, etc.)
        **kwargs: Additional parameters (book, genre, etc.)
    
    Returns:
        Dict with SEO configuration
    """
    base_url = "https://bookwise.app"  # Update with actual URL
    
    seo_configs = {
        "home": {
            "title": "BookWise - AI-Powered Book Summaries | 500+ Books",
            "description": "Discover key insights from 500+ bestselling books. Read AI-powered summaries, explore genres, and accelerate your learning journey.",
            "keywords": "book summaries, book insights, reading, self-improvement, business books, psychology books",
            "og_type": "website",
            "structured_data": {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": "BookWise",
                "description": "AI-Powered Book Summary Platform",
                "url": base_url,
            }
        },
        "category": {
            "title": f"{kwargs.get('genre_name', 'Books')} - Book Summaries | BookWise",
            "description": kwargs.get('genre_description', 'Explore book summaries in this category.'),
            "keywords": f"{kwargs.get('genre_name', '').lower()} books, book summaries, reading",
            "og_type": "website",
        },
        "book": {
            "title": f"{kwargs.get('book_title', 'Book')} Summary | BookWise",
            "description": f"Read the summary of {kwargs.get('book_title', 'this book')} by {kwargs.get('author', 'Author')}. Key insights and takeaways.",
            "keywords": f"{kwargs.get('book_title', '')}, {kwargs.get('author', '')}, book summary",
            "og_type": "book",
            "og_image": kwargs.get('cover_url'),
            "structured_data": {
                "@context": "https://schema.org",
                "@type": "Book",
                "name": kwargs.get('book_title', ''),
                "author": {"@type": "Person", "name": kwargs.get('author', '')},
            }
        },
        "about": {
            "title": "About BookWise - Our Mission",
            "description": "Learn about BookWise, our mission to make knowledge accessible through AI-powered book summaries.",
            "og_type": "website",
        },
    }
    
    return seo_configs.get(page_type, seo_configs["home"])


def render_breadcrumb(items: list) -> None:
    """Render breadcrumb navigation."""
    breadcrumb_html = '<nav aria-label="breadcrumb"><ol style="display:flex;gap:0.5rem;list-style:none;padding:0;color:#94a3b8;font-size:0.9rem;">'
    for i, item in enumerate(items):
        if i < len(items) - 1:
            breadcrumb_html += f'<li><a href="{item["url"]}" style="color:#6366f1;text-decoration:none;">{item["label"]}</a> /</li>'
        else:
            breadcrumb_html += f'<li style="color:#e2e8f0;">{item["label"]}</li>'
    breadcrumb_html += '</ol></nav>'
    st.markdown(breadcrumb_html, unsafe_allow_html=True)
