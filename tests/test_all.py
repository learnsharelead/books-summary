"""
Comprehensive Unit Tests for BookWise
Tests all components, queries, and functionality
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDatabaseQueries:
    """Test database query functions"""
    
    def test_get_all_genres(self):
        """Test getting all genres"""
        from database.queries import get_all_genres
        genres = get_all_genres()
        assert isinstance(genres, list)
        assert len(genres) > 0
        print(f"✅ get_all_genres: {len(genres)} genres found")
    
    def test_get_books_count(self):
        """Test getting books count"""
        from database.queries import get_books_count
        count = get_books_count()
        assert isinstance(count, int)
        assert count > 0
        print(f"✅ get_books_count: {count} books")
    
    def test_get_genres_count(self):
        """Test getting genres count"""
        from database.queries import get_genres_count
        count = get_genres_count()
        assert isinstance(count, int)
        assert count > 0
        print(f"✅ get_genres_count: {count} genres")
    
    def test_get_summaries_count(self):
        """Test getting summaries count"""
        from database.queries import get_summaries_count
        count = get_summaries_count()
        assert isinstance(count, int)
        assert count >= 0
        print(f"✅ get_summaries_count: {count} summaries")
    
    def test_get_featured_books(self):
        """Test getting featured books"""
        from database.queries import get_featured_books
        books = get_featured_books(limit=6)
        assert isinstance(books, list)
        print(f"✅ get_featured_books: {len(books)} featured books")
    
    def test_get_random_book(self):
        """Test getting random book"""
        from database.queries import get_random_book
        book = get_random_book()
        if book:
            assert hasattr(book, 'title')
            assert hasattr(book, 'author')
            print(f"✅ get_random_book: {book.title}")
        else:
            print("⚠️ get_random_book: No books in database")
    
    def test_get_top_rated_books(self):
        """Test getting top rated books"""
        from database.queries import get_top_rated_books
        books = get_top_rated_books(limit=6)
        assert isinstance(books, list)
        print(f"✅ get_top_rated_books: {len(books)} books")
    
    def test_get_recent_books(self):
        """Test getting recent books"""
        from database.queries import get_recent_books
        books = get_recent_books(limit=6)
        assert isinstance(books, list)
        print(f"✅ get_recent_books: {len(books)} books")
    
    def test_search_books(self):
        """Test book search"""
        from database.queries import search_books
        results = search_books("habit", limit=10)
        assert isinstance(results, list)
        print(f"✅ search_books('habit'): {len(results)} results")
    
    def test_get_all_books(self):
        """Test getting all books"""
        from database.queries import get_all_books
        books = get_all_books()
        assert isinstance(books, list)
        assert len(books) > 0
        print(f"✅ get_all_books: {len(books)} books")
    
    def test_get_book_by_slug(self):
        """Test getting book by slug"""
        from database.queries import get_all_books, get_book_by_slug
        books = get_all_books()
        if books:
            slug = books[0].slug
            book = get_book_by_slug(slug)
            assert book is not None
            assert book.slug == slug
            print(f"✅ get_book_by_slug: Found '{book.title}'")
        else:
            print("⚠️ get_book_by_slug: No books to test")
    
    def test_get_genre_by_slug(self):
        """Test getting genre by slug"""
        from database.queries import get_all_genres, get_genre_by_slug
        genres = get_all_genres()
        if genres:
            slug = genres[0].slug
            genre = get_genre_by_slug(slug)
            assert genre is not None
            print(f"✅ get_genre_by_slug: Found '{genre.name}'")
        else:
            print("⚠️ get_genre_by_slug: No genres to test")


class TestComponents:
    """Test UI components"""
    
    def test_image_handler_import(self):
        """Test image handler imports"""
        from components.image_handler import load_image_safe, get_placeholder_image
        placeholder = get_placeholder_image("book")
        assert placeholder is not None
        assert "http" in placeholder or "data:" in placeholder
        print(f"✅ image_handler: Placeholder generated")
    
    def test_discovery_imports(self):
        """Test discovery component imports"""
        from components.discovery import (
            render_random_book_button,
            render_social_share_buttons,
            render_compact_share_buttons,
            add_bookmark,
            remove_bookmark,
            is_bookmarked
        )
        print("✅ discovery: All functions imported")
    
    def test_theme_imports(self):
        """Test theme component imports"""
        from components.theme import (
            init_theme,
            get_current_theme,
            toggle_theme,
            get_theme_css
        )
        css = get_theme_css()
        assert "<style>" in css
        print("✅ theme: CSS generated")
    
    def test_newsletter_imports(self):
        """Test newsletter component imports"""
        from components.newsletter import render_newsletter_signup, get_subscriber_count
        print("✅ newsletter: Functions imported")
    
    def test_reading_lists(self):
        """Test reading lists"""
        from components.reading_lists import READING_LISTS, get_reading_lists
        lists = get_reading_lists()
        assert isinstance(lists, dict)
        assert len(lists) >= 6
        print(f"✅ reading_lists: {len(lists)} collections")
    
    def test_book_of_day(self):
        """Test book of the day"""
        from components.book_of_day import get_book_of_the_day
        book = get_book_of_the_day()
        if book:
            assert hasattr(book, 'title')
            print(f"✅ book_of_day: Today's book is '{book.title}'")
        else:
            print("⚠️ book_of_day: No books available")
    
    def test_testimonials(self):
        """Test testimonials"""
        from components.testimonials import TESTIMONIALS, get_testimonials
        testimonials = get_testimonials()
        assert isinstance(testimonials, list)
        assert len(testimonials) >= 3
        print(f"✅ testimonials: {len(testimonials)} testimonials")
    
    def test_genre_themes(self):
        """Test genre themes"""
        from components.genre_themes import get_genre_theme, get_genre_gradient, GENRE_THEMES
        theme = get_genre_theme("productivity")
        assert "gradient" in theme
        assert "primary" in theme
        print(f"✅ genre_themes: {len(GENRE_THEMES)} themes defined")
    
    def test_filters(self):
        """Test filters component"""
        from components.filters import get_filter_options
        options = get_filter_options()
        assert "years" in options
        print(f"✅ filters: {len(options['years'])} years available")
    
    def test_progress_tracker(self):
        """Test progress tracker"""
        from components.progress_tracker import get_reading_progress
        # Test with mock slug
        progress = get_reading_progress("test-book")
        assert "sections_read" in progress
        assert "percentage" in progress
        print("✅ progress_tracker: Progress tracking works")


class TestUtilities:
    """Test utility functions"""
    
    def test_sitemap_generator(self):
        """Test sitemap generator"""
        from utils.sitemap import generate_sitemap, get_sitemap_stats
        stats = get_sitemap_stats()
        assert "total_urls" in stats
        assert stats["total_urls"] > 0
        print(f"✅ sitemap: {stats['total_urls']} URLs")
    
    def test_sitemap_content(self):
        """Test sitemap XML content"""
        from utils.sitemap import generate_sitemap
        content = generate_sitemap(base_url="https://test.com")
        assert '<?xml version="1.0"' in content
        assert '<urlset' in content
        assert '</urlset>' in content
        print("✅ sitemap: Valid XML generated")


class TestDatabaseConnection:
    """Test database connection"""
    
    def test_connection(self):
        """Test database connection"""
        from database.connection import get_db_session
        with get_db_session() as session:
            assert session is not None
        print("✅ database: Connection successful")
    
    def test_models(self):
        """Test database models"""
        from database.models import Genre, Book, Summary, SummaryImage
        assert Genre is not None
        assert Book is not None
        assert Summary is not None
        print("✅ models: All models imported")


def run_all_tests():
    """Run all tests and collect results"""
    print("\n" + "="*60)
    print("🧪 BOOKWISE UNIT TESTS")
    print("="*60 + "\n")
    
    results = {
        "passed": 0,
        "failed": 0,
        "errors": []
    }
    
    # Test classes
    test_classes = [
        TestDatabaseConnection,
        TestDatabaseQueries,
        TestComponents,
        TestUtilities,
    ]
    
    for test_class in test_classes:
        print(f"\n📦 {test_class.__name__}")
        print("-" * 40)
        
        instance = test_class()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                try:
                    getattr(instance, method_name)()
                    results["passed"] += 1
                except Exception as e:
                    results["failed"] += 1
                    error_msg = f"❌ {method_name}: {str(e)}"
                    print(error_msg)
                    results["errors"].append({
                        "test": f"{test_class.__name__}.{method_name}",
                        "error": str(e)
                    })
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    print(f"✅ Passed: {results['passed']}")
    print(f"❌ Failed: {results['failed']}")
    print(f"📈 Total:  {results['passed'] + results['failed']}")
    
    if results["errors"]:
        print("\n🔴 ERRORS TO FIX:")
        print("-" * 40)
        for error in results["errors"]:
            print(f"  • {error['test']}")
            print(f"    Error: {error['error']}")
    
    return results


if __name__ == "__main__":
    run_all_tests()
