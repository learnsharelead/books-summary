"""
Comprehensive Unit Tests for Components
Tests all component functions with mocking and edge cases.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================================================
# IMAGE HANDLER TESTS
# ============================================================================

class TestImageHandler:
    """Test image handler component"""
    
    def test_placeholder_images_defined(self):
        """Test that placeholder images are defined"""
        from components.image_handler import PLACEHOLDER_IMAGES
        
        assert "book" in PLACEHOLDER_IMAGES
        assert "concept" in PLACEHOLDER_IMAGES
        assert "takeaway" in PLACEHOLDER_IMAGES
        assert "genre" in PLACEHOLDER_IMAGES
    
    def test_get_placeholder_image_book(self):
        """Test getting book placeholder"""
        from components.image_handler import get_placeholder_image
        
        result = get_placeholder_image("book")
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_get_placeholder_image_default(self):
        """Test that unknown type falls back to book"""
        from components.image_handler import get_placeholder_image
        
        result = get_placeholder_image("unknown")
        book_result = get_placeholder_image("book")
        assert result == book_result
    
    def test_get_open_library_cover(self):
        """Test Open Library cover URL generation"""
        from components.image_handler import get_open_library_cover
        
        result = get_open_library_cover("1234567890")
        assert "1234567890" in result
        assert "openlibrary.org" in result
    
    def test_get_open_library_cover_sizes(self):
        """Test Open Library cover sizes"""
        from components.image_handler import get_open_library_cover
        
        small = get_open_library_cover("123", "S")
        medium = get_open_library_cover("123", "M")
        large = get_open_library_cover("123", "L")
        
        assert "-S.jpg" in small
        assert "-M.jpg" in medium
        assert "-L.jpg" in large
    
    def test_get_unsplash_image(self):
        """Test Unsplash fallback image"""
        from components.image_handler import get_unsplash_image
        
        result = get_unsplash_image("test query")
        assert isinstance(result, str)
        assert "unsplash.com" in result
    
    @patch('components.image_handler.check_image_url')
    def test_load_image_safe_with_valid_url(self, mock_check):
        """Test load_image_safe with valid URL"""
        mock_check.return_value = True
        from components.image_handler import load_image_safe
        
        test_url = "https://example.com/image.jpg"
        result = load_image_safe(test_url)
        assert result == test_url
    
    @patch('components.image_handler.check_image_url')
    def test_load_image_safe_with_invalid_url(self, mock_check):
        """Test load_image_safe with invalid URL falls back"""
        mock_check.return_value = False
        from components.image_handler import load_image_safe, PLACEHOLDER_IMAGES
        
        result = load_image_safe("https://broken.com/image.jpg", "book")
        assert result == PLACEHOLDER_IMAGES["book"]
    
    def test_load_image_safe_with_none(self):
        """Test load_image_safe with None returns placeholder"""
        from components.image_handler import load_image_safe, PLACEHOLDER_IMAGES
        
        result = load_image_safe(None)
        assert result == PLACEHOLDER_IMAGES["book"]


# ============================================================================
# DISCOVERY COMPONENT TESTS
# ============================================================================

class TestDiscoveryComponent:
    """Test discovery component functions"""
    
    def test_add_bookmark(self):
        """Test adding bookmark to session"""
        with patch('streamlit.session_state', {}) as mock_state:
            # Import after mocking
            import components.discovery as discovery
            
            # Manually set up the mock
            st_mock = MagicMock()
            st_mock.session_state = {}
            
            with patch.object(discovery, 'st', st_mock):
                discovery.add_bookmark("test-slug", "Test Book", "Test Author")
                
                assert "bookmarks" in st_mock.session_state
                assert len(st_mock.session_state["bookmarks"]) == 1
    
    def test_add_duplicate_bookmark(self):
        """Test that duplicate bookmarks are not added"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "bookmarks": [{"slug": "test-slug", "title": "Test Book", "author": "Test Author"}]
        }
        
        import components.discovery as discovery
        
        with patch.object(discovery, 'st', st_mock):
            discovery.add_bookmark("test-slug", "Test Book", "Test Author")
            assert len(st_mock.session_state["bookmarks"]) == 1
    
    def test_remove_bookmark(self):
        """Test removing bookmark from session"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "bookmarks": [
                {"slug": "test-slug", "title": "Test Book", "author": "Test Author"},
                {"slug": "other-slug", "title": "Other Book", "author": "Other Author"}
            ]
        }
        
        import components.discovery as discovery
        
        with patch.object(discovery, 'st', st_mock):
            discovery.remove_bookmark("test-slug")
            assert len(st_mock.session_state["bookmarks"]) == 1
            assert st_mock.session_state["bookmarks"][0]["slug"] == "other-slug"
    
    def test_is_bookmarked_true(self):
        """Test is_bookmarked returns True for bookmarked book"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "bookmarks": [{"slug": "test-slug", "title": "Test Book", "author": "Test Author"}]
        }
        
        import components.discovery as discovery
        
        with patch.object(discovery, 'st', st_mock):
            result = discovery.is_bookmarked("test-slug")
            assert result is True
    
    def test_is_bookmarked_false(self):
        """Test is_bookmarked returns False for non-bookmarked book"""
        st_mock = MagicMock()
        st_mock.session_state = {"bookmarks": []}
        
        import components.discovery as discovery
        
        with patch.object(discovery, 'st', st_mock):
            result = discovery.is_bookmarked("test-slug")
            assert result is False


# ============================================================================
# PROGRESS TRACKER TESTS
# ============================================================================

class TestProgressTracker:
    """Test progress tracker component"""
    
    def test_get_reading_progress_new_book(self):
        """Test getting progress for new book"""
        st_mock = MagicMock()
        st_mock.session_state = {}
        
        import components.progress_tracker as progress_tracker
        
        with patch.object(progress_tracker, 'st', st_mock):
            result = progress_tracker.get_reading_progress("new-book")
            
            assert "sections_read" in result
            assert "percentage" in result
            assert result["percentage"] == 0
            assert result["sections_read"] == []
    
    def test_get_reading_progress_existing_book(self):
        """Test getting progress for existing book"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "reading_progress": {
                "existing-book": {
                    "sections_read": ["Section 1"],
                    "started_at": "2024-01-01",
                    "completed_at": None,
                    "percentage": 20
                }
            }
        }
        
        import components.progress_tracker as progress_tracker
        
        with patch.object(progress_tracker, 'st', st_mock):
            result = progress_tracker.get_reading_progress("existing-book")
            
            assert result["percentage"] == 20
            assert "Section 1" in result["sections_read"]
    
    def test_update_reading_progress(self):
        """Test updating reading progress"""
        st_mock = MagicMock()
        st_mock.session_state = {}
        
        import components.progress_tracker as progress_tracker
        
        with patch.object(progress_tracker, 'st', st_mock):
            progress_tracker.update_reading_progress("test-book", "Section 1", 5)
            
            assert "reading_progress" in st_mock.session_state
            progress = st_mock.session_state["reading_progress"]["test-book"]
            assert "Section 1" in progress["sections_read"]
            assert progress["percentage"] == 20  # 1/5 * 100
    
    def test_update_reading_progress_completion(self):
        """Test that 100% marks completion"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "reading_progress": {
                "test-book": {
                    "sections_read": ["S1", "S2", "S3", "S4"],
                    "started_at": "2024-01-01",
                    "completed_at": None,
                    "percentage": 80
                }
            }
        }
        
        import components.progress_tracker as progress_tracker
        
        with patch.object(progress_tracker, 'st', st_mock):
            progress_tracker.update_reading_progress("test-book", "S5", 5)
            
            progress = st_mock.session_state["reading_progress"]["test-book"]
            assert progress["percentage"] == 100
            assert progress["completed_at"] is not None
    
    def test_get_books_in_progress(self):
        """Test getting books in progress"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "reading_progress": {
                "book-1": {"percentage": 50, "completed_at": None},
                "book-2": {"percentage": 100, "completed_at": "2024-01-01"},
                "book-3": {"percentage": 30, "completed_at": None}
            }
        }
        
        import components.progress_tracker as progress_tracker
        
        with patch.object(progress_tracker, 'st', st_mock):
            result = progress_tracker.get_books_in_progress()
            
            assert "book-1" in result
            assert "book-3" in result
            assert "book-2" not in result  # Completed
    
    def test_get_completed_books(self):
        """Test getting completed books"""
        st_mock = MagicMock()
        st_mock.session_state = {
            "reading_progress": {
                "book-1": {"percentage": 50, "completed_at": None},
                "book-2": {"percentage": 100, "completed_at": "2024-01-01"}
            }
        }
        
        import components.progress_tracker as progress_tracker
        
        with patch.object(progress_tracker, 'st', st_mock):
            result = progress_tracker.get_completed_books()
            
            assert "book-2" in result
            assert "book-1" not in result


# ============================================================================
# NEWSLETTER COMPONENT TESTS
# ============================================================================

class TestNewsletterComponent:
    """Test newsletter component"""
    
    def test_get_subscriber_count_empty(self):
        """Test subscriber count with no subscribers"""
        import components.newsletter as newsletter
        
        st_mock = MagicMock()
        st_mock.session_state = MagicMock()
        st_mock.session_state.get = MagicMock(return_value=[])
        
        with patch.object(newsletter, 'st', st_mock):
            result = newsletter.get_subscriber_count()
            assert result == 0
    
    def test_get_subscriber_count_with_subscribers(self):
        """Test subscriber count with subscribers"""
        import components.newsletter as newsletter
        
        subscribers = ["user1@test.com", "user2@test.com"]
        
        st_mock = MagicMock()
        st_mock.session_state = MagicMock()
        st_mock.session_state.get = MagicMock(return_value=subscribers)
        
        with patch.object(newsletter, 'st', st_mock):
            result = newsletter.get_subscriber_count()
            assert result == 2
    
    def test_newsletter_functions_exist(self):
        """Test newsletter functions exist"""
        from components.newsletter import render_newsletter_signup, get_subscriber_count
        
        assert callable(render_newsletter_signup)
        assert callable(get_subscriber_count)


# ============================================================================
# FILTERS COMPONENT TESTS
# ============================================================================

class TestFiltersComponent:
    """Test filters component"""
    
    def test_get_filter_options(self):
        """Test getting filter options"""
        from components.filters import get_filter_options
        
        options = get_filter_options()
        
        assert isinstance(options, dict)
        assert "years" in options
        assert "reading_times" in options
        assert "difficulties" in options
    
    def test_apply_filters_year(self):
        """Test applying year filter"""
        from components.filters import apply_filters
        
        # Create mock books
        book1 = Mock()
        book1.publication_year = 2020
        book1.title = "Book A"
        
        book2 = Mock()
        book2.publication_year = 2021
        book2.title = "Book B"
        
        books = [book1, book2]
        filters = {"year": 2020}
        
        result = apply_filters(books, filters)
        
        assert len(result) == 1
        assert result[0].publication_year == 2020
    
    def test_apply_filters_sort_title_asc(self):
        """Test sorting by title ascending"""
        from components.filters import apply_filters
        
        book1 = Mock()
        book1.title = "Zebra Book"
        book1.publication_year = None
        
        book2 = Mock()
        book2.title = "Apple Book"
        book2.publication_year = None
        
        result = apply_filters([book1, book2], {"sort": "Title (A-Z)"})
        
        assert result[0].title == "Apple Book"
        assert result[1].title == "Zebra Book"
    
    def test_apply_filters_sort_title_desc(self):
        """Test sorting by title descending"""
        from components.filters import apply_filters
        
        book1 = Mock()
        book1.title = "Apple Book"
        book1.publication_year = None
        
        book2 = Mock()
        book2.title = "Zebra Book"
        book2.publication_year = None
        
        result = apply_filters([book1, book2], {"sort": "Title (Z-A)"})
        
        assert result[0].title == "Zebra Book"
        assert result[1].title == "Apple Book"
    
    def test_apply_filters_sort_newest(self):
        """Test sorting by newest first"""
        from components.filters import apply_filters
        
        book1 = Mock()
        book1.title = "Old Book"
        book1.publication_year = 2000
        
        book2 = Mock()
        book2.title = "New Book"
        book2.publication_year = 2023
        
        result = apply_filters([book1, book2], {"sort": "Newest First"})
        
        assert result[0].publication_year == 2023
        assert result[1].publication_year == 2000
    
    def test_apply_filters_sort_oldest(self):
        """Test sorting by oldest first"""
        from components.filters import apply_filters
        
        book1 = Mock()
        book1.title = "New Book"
        book1.publication_year = 2023
        
        book2 = Mock()
        book2.title = "Old Book"
        book2.publication_year = 2000
        
        result = apply_filters([book1, book2], {"sort": "Oldest First"})
        
        assert result[0].publication_year == 2000
        assert result[1].publication_year == 2023


# ============================================================================
# GENRE THEMES TESTS
# ============================================================================

class TestGenreThemes:
    """Test genre themes component"""
    
    def test_genre_themes_defined(self):
        """Test that genre themes are defined"""
        from components.genre_themes import GENRE_THEMES
        
        assert isinstance(GENRE_THEMES, dict)
        assert len(GENRE_THEMES) > 0
    
    def test_get_genre_theme_existing(self):
        """Test getting theme for existing genre"""
        from components.genre_themes import get_genre_theme
        
        result = get_genre_theme("productivity")
        
        assert isinstance(result, dict)
        assert "gradient" in result
        assert "primary" in result
    
    def test_get_genre_theme_fallback(self):
        """Test getting theme for unknown genre uses default"""
        from components.genre_themes import get_genre_theme
        
        result = get_genre_theme("nonexistent-genre")
        
        assert isinstance(result, dict)
        assert "gradient" in result
    
    def test_get_genre_gradient(self):
        """Test getting genre gradient"""
        from components.genre_themes import get_genre_gradient
        
        result = get_genre_gradient("productivity")
        
        assert isinstance(result, str)
        assert "gradient" in result.lower() or "#" in result


# ============================================================================
# READING LISTS TESTS
# ============================================================================

class TestReadingLists:
    """Test reading lists component"""
    
    def test_reading_lists_defined(self):
        """Test that reading lists are defined"""
        from components.reading_lists import READING_LISTS
        
        assert isinstance(READING_LISTS, dict)
        assert len(READING_LISTS) > 0
    
    def test_get_reading_lists(self):
        """Test getting reading lists"""
        from components.reading_lists import get_reading_lists
        
        result = get_reading_lists()
        
        assert isinstance(result, dict)
        assert len(result) >= 6
    
    def test_reading_list_structure(self):
        """Test reading list structure"""
        from components.reading_lists import READING_LISTS
        
        for list_id, reading_list in READING_LISTS.items():
            assert "title" in reading_list
            assert "books" in reading_list
            assert isinstance(reading_list["books"], list)


# ============================================================================
# TESTIMONIALS TESTS
# ============================================================================

class TestTestimonials:
    """Test testimonials component"""
    
    def test_testimonials_defined(self):
        """Test that testimonials are defined"""
        from components.testimonials import TESTIMONIALS
        
        assert isinstance(TESTIMONIALS, list)
        assert len(TESTIMONIALS) > 0
    
    def test_get_testimonials(self):
        """Test getting testimonials"""
        from components.testimonials import get_testimonials
        
        result = get_testimonials()
        
        assert isinstance(result, list)
        assert len(result) >= 3
    
    def test_testimonial_structure(self):
        """Test testimonial structure"""
        from components.testimonials import TESTIMONIALS
        
        for testimonial in TESTIMONIALS:
            assert "name" in testimonial or "author" in testimonial
            assert "text" in testimonial or "quote" in testimonial or "content" in testimonial


# ============================================================================
# BOOK OF DAY TESTS
# ============================================================================

class TestBookOfDay:
    """Test book of the day component"""
    
    def test_get_book_of_the_day(self):
        """Test getting book of the day"""
        from components.book_of_day import get_book_of_the_day
        
        result = get_book_of_the_day()
        
        # Either returns a book or None
        if result:
            assert hasattr(result, 'title')
            assert hasattr(result, 'author')
    
    def test_book_of_day_consistent_same_day(self):
        """Test that same day returns same book"""
        from components.book_of_day import get_book_of_the_day
        
        # Call twice, should return same book (based on date seed)
        book1 = get_book_of_the_day()
        book2 = get_book_of_the_day()
        
        if book1 and book2:
            assert book1.id == book2.id


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
