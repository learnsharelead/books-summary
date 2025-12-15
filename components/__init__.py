"""Components package for BookWise UI elements."""

from components.seo import inject_seo_meta, get_page_seo
from components.book_card import render_book_card, render_book_grid
from components.genre_card import render_genre_card, render_genre_grid
from components.image_handler import load_image_safe, get_placeholder_image
from components.navigation import render_navigation, render_breadcrumb
from components.footer import render_footer
from components.search import render_search_bar, render_search_results, handle_search
from components.discovery import (
    render_random_book_button, render_social_share_buttons,
    render_compact_share_buttons, render_bookmarks_sidebar,
    add_bookmark, remove_bookmark, is_bookmarked
)
from components.theme import (
    init_theme, get_current_theme, toggle_theme,
    render_theme_toggle, get_theme_css, apply_theme
)
from components.newsletter import render_newsletter_signup, get_subscriber_count
from components.reading_lists import get_reading_lists, render_reading_lists_section
from components.related_books import render_related_books
from components.progress_tracker import (
    render_progress_bar, render_section_checkboxes,
    render_reading_stats, get_reading_progress
)
from components.filters import render_filters, apply_filters
from components.stats_bar import render_stats_bar, render_compact_stats
from components.book_of_day import render_book_of_the_day, get_book_of_the_day
from components.quick_actions import render_quick_actions, render_scroll_to_top, render_action_bar
from components.testimonials import render_testimonials, render_stats_with_social_proof
from components.genre_themes import get_genre_theme, get_genre_gradient, apply_genre_theme_css

__all__ = [
    # SEO
    "inject_seo_meta", "get_page_seo",
    # Cards
    "render_book_card", "render_book_grid",
    "render_genre_card", "render_genre_grid",
    # Images
    "load_image_safe", "get_placeholder_image",
    # Navigation
    "render_navigation", "render_breadcrumb", "render_footer",
    # Search
    "render_search_bar", "render_search_results", "handle_search",
    # Discovery
    "render_random_book_button", "render_social_share_buttons",
    "render_compact_share_buttons", "render_bookmarks_sidebar",
    "add_bookmark", "remove_bookmark", "is_bookmarked",
    # Theme
    "init_theme", "get_current_theme", "toggle_theme",
    "render_theme_toggle", "get_theme_css", "apply_theme",
    # Newsletter
    "render_newsletter_signup", "get_subscriber_count",
    # Reading Lists
    "get_reading_lists", "render_reading_lists_section",
    # Related Books
    "render_related_books",
    # Progress Tracker
    "render_progress_bar", "render_section_checkboxes",
    "render_reading_stats", "get_reading_progress",
    # Filters
    "render_filters", "apply_filters",
    # Stats
    "render_stats_bar", "render_compact_stats",
    # Book of the Day
    "render_book_of_the_day", "get_book_of_the_day",
    # Quick Actions
    "render_quick_actions", "render_scroll_to_top", "render_action_bar",
    # Testimonials
    "render_testimonials", "render_stats_with_social_proof",
    # Genre Themes
    "get_genre_theme", "get_genre_gradient", "apply_genre_theme_css",
]



