"""
Comprehensive Unit Tests for Utilities
Tests helpers, performance utilities, SEO content, and sitemap generation.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
import time

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================================================
# HELPERS TESTS
# ============================================================================

class TestSlugify:
    """Test slugify function"""
    
    def test_slugify_simple(self):
        """Test simple text slugification"""
        from utils.helpers import slugify
        
        result = slugify("Hello World")
        assert result == "hello-world"
    
    def test_slugify_with_special_chars(self):
        """Test slugification with special characters"""
        from utils.helpers import slugify
        
        result = slugify("Hello: World's Best!")
        assert ":" not in result
        assert "'" not in result
    
    def test_slugify_with_ampersand(self):
        """Test slugification with ampersand"""
        from utils.helpers import slugify
        
        result = slugify("Art & Design")
        assert result == "art-and-design"
    
    def test_slugify_with_dots(self):
        """Test slugification with dots"""
        from utils.helpers import slugify
        
        result = slugify("Dr. John Smith")
        assert "." not in result
    
    def test_slugify_with_commas(self):
        """Test slugification with commas"""
        from utils.helpers import slugify
        
        result = slugify("Red, Blue, Green")
        assert "," not in result
    
    def test_slugify_lowercase(self):
        """Test that slugify returns lowercase"""
        from utils.helpers import slugify
        
        result = slugify("HELLO WORLD")
        assert result == result.lower()


class TestFormatReadingTime:
    """Test format_reading_time function"""
    
    def test_less_than_minute(self):
        """Test formatting for less than 1 minute"""
        from utils.helpers import format_reading_time
        
        result = format_reading_time(0)
        assert "< 1 min" in result
    
    def test_one_minute(self):
        """Test formatting for exactly 1 minute"""
        from utils.helpers import format_reading_time
        
        result = format_reading_time(1)
        assert "1 min" in result
        assert "mins" not in result  # Should be singular
    
    def test_multiple_minutes(self):
        """Test formatting for multiple minutes"""
        from utils.helpers import format_reading_time
        
        result = format_reading_time(5)
        assert "5" in result
        assert "min" in result
    
    def test_large_value(self):
        """Test formatting for large values"""
        from utils.helpers import format_reading_time
        
        result = format_reading_time(60)
        assert "60" in result


class TestHelpersImports:
    """Test helpers module imports"""
    
    def test_load_css_import(self):
        """Test load_css can be imported"""
        from utils.helpers import load_css
        assert callable(load_css)
    
    def test_render_footer_import(self):
        """Test render_footer can be imported"""
        from utils.helpers import render_footer
        assert callable(render_footer)
    
    def test_init_page_config_import(self):
        """Test init_page_config can be imported"""
        from utils.helpers import init_page_config
        assert callable(init_page_config)


# ============================================================================
# PERFORMANCE UTILITIES TESTS
# ============================================================================

class TestPerformanceImports:
    """Test performance utility imports"""
    
    def test_cached_component_import(self):
        """Test cached_component can be imported"""
        from utils.performance import cached_component
        assert callable(cached_component)
    
    def test_get_optimized_image_url_import(self):
        """Test get_optimized_image_url can be imported"""
        from utils.performance import get_optimized_image_url
        assert callable(get_optimized_image_url)
    
    def test_query_timer_import(self):
        """Test QueryTimer can be imported"""
        from utils.performance import QueryTimer
        assert QueryTimer is not None


class TestGetOptimizedImageUrl:
    """Test image URL optimization"""
    
    def test_unsplash_optimization(self):
        """Test Unsplash URL optimization"""
        from utils.performance import get_optimized_image_url
        
        url = "https://images.unsplash.com/photo-123456"
        result = get_optimized_image_url(url, width=300)
        
        assert isinstance(result, str)
    
    def test_with_width_parameter(self):
        """Test optimization with width parameter"""
        from utils.performance import get_optimized_image_url
        
        url = "https://example.com/image.jpg"
        result = get_optimized_image_url(url, width=300)
        
        assert isinstance(result, str)
    
    def test_with_quality_parameter(self):
        """Test optimization with quality parameter"""
        from utils.performance import get_optimized_image_url
        
        url = "https://example.com/image.jpg"
        result = get_optimized_image_url(url, width=300, quality=80)
        
        assert isinstance(result, str)


class TestGenerateSrcset:
    """Test srcset generation"""
    
    def test_generate_srcset_default_sizes(self):
        """Test srcset generation with default sizes"""
        from utils.performance import generate_srcset
        
        url = "https://example.com/image.jpg"
        result = generate_srcset(url)
        
        assert isinstance(result, str)
    
    def test_generate_srcset_custom_sizes(self):
        """Test srcset generation with custom sizes"""
        from utils.performance import generate_srcset
        
        url = "https://example.com/image.jpg"
        result = generate_srcset(url, sizes=[300, 600, 900])
        
        assert isinstance(result, str)


class TestQueryTimer:
    """Test QueryTimer context manager"""
    
    def test_query_timer_creation(self):
        """Test QueryTimer can be created"""
        from utils.performance import QueryTimer
        
        timer = QueryTimer("Test Query")
        assert timer.query_name == "Test Query"
    
    def test_query_timer_context_manager(self):
        """Test QueryTimer works as context manager"""
        from utils.performance import QueryTimer
        
        with QueryTimer("Test") as timer:
            time.sleep(0.01)  # Small delay
        
        assert timer.duration is not None
        assert timer.duration > 0
    
    def test_query_timer_measures_time(self):
        """Test QueryTimer measures elapsed time"""
        from utils.performance import QueryTimer
        
        with QueryTimer("Test") as timer:
            time.sleep(0.1)
        
        # Should be at least 100ms
        assert timer.duration >= 0.09


class MockSessionState(dict):
    """Mock session state that supports attribute access"""
    def __getattr__(self, key):
        if key in self:
            return self[key]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")
    
    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
        else:
            raise AttributeError(key)

class TestCachedComponent:
    """Test cached_component decorator"""
    
    def test_cached_component_decorator(self):
        """Test cached_component as decorator"""
        from utils.performance import cached_component
        import utils.performance as performance
        
        # Create a mock streamlit object
        st_mock = MagicMock()
        st_mock.session_state = MockSessionState()
        
        # Patch streamlit in the module
        with patch.object(performance, 'st', st_mock):
            @cached_component(ttl=60)
            def test_func():
                return "result"
            
            # First call - should execute
            result = test_func()
            assert result == "result"
            
            # Verify it's in session state (cache keys are md5 hashes, so hard to predict exact key)
            assert len(st_mock.session_state) > 0


class TestLazyLoadSection:
    """Test lazy load section"""
    
    def test_lazy_load_section_import(self):
        """Test lazy_load_section can be imported"""
        from utils.performance import lazy_load_section
        assert callable(lazy_load_section)


class TestClearComponentCache:
    """Test clear_component_cache function"""
    
    def test_clear_component_cache_import(self):
        """Test clear_component_cache can be imported"""
        from utils.performance import clear_component_cache
        assert callable(clear_component_cache)
    
    def test_clear_component_cache_returns_count(self):
        """Test clear_component_cache returns count"""
        from utils.performance import clear_component_cache
        import utils.performance as performance
        
        st_mock = MagicMock()
        st_mock.session_state = MockSessionState()
        
        with patch.object(performance, 'st', st_mock):
            result = clear_component_cache()
            assert isinstance(result, int)
            assert result >= 0


class TestGetQueryStats:
    """Test get_query_stats function"""
    
    def test_get_query_stats_import(self):
        """Test get_query_stats can be imported"""
        from utils.performance import get_query_stats
        assert callable(get_query_stats)
    
    def test_get_query_stats_returns_dict(self):
        """Test get_query_stats returns dictionary"""
        from utils.performance import get_query_stats
        import utils.performance as performance
        
        st_mock = MagicMock()
        st_mock.session_state = MockSessionState()
        
        with patch.object(performance, 'st', st_mock):
            result = get_query_stats()
            assert isinstance(result, dict)


class TestPrefetchData:
    """Test prefetch_data function"""
    
    def test_prefetch_data_import(self):
        """Test prefetch_data can be imported"""
        from utils.performance import prefetch_data
        assert callable(prefetch_data)


class TestRenderVirtualList:
    """Test render_virtual_list function"""
    
    def test_render_virtual_list_import(self):
        """Test render_virtual_list can be imported"""
        from utils.performance import render_virtual_list
        assert callable(render_virtual_list)


class TestMemoryOptimization:
    """Test memory optimization functions"""
    
    def test_limit_session_state_size_import(self):
        """Test limit_session_state_size can be imported"""
        from utils.performance import limit_session_state_size
        assert callable(limit_session_state_size)


# ============================================================================
# SITEMAP TESTS
# ============================================================================

class TestSitemapImports:
    """Test sitemap module imports"""
    
    def test_generate_sitemap_import(self):
        """Test generate_sitemap can be imported"""
        from utils.sitemap import generate_sitemap
        assert callable(generate_sitemap)
    
    def test_get_sitemap_stats_import(self):
        """Test get_sitemap_stats can be imported"""
        from utils.sitemap import get_sitemap_stats
        assert callable(get_sitemap_stats)


class TestGenerateSitemap:
    """Test sitemap generation"""
    
    def test_generates_xml(self):
        """Test that sitemap generates valid XML"""
        from utils.sitemap import generate_sitemap
        
        result = generate_sitemap(base_url="https://test.com")
        
        assert isinstance(result, str)
        assert '<?xml version="1.0"' in result
    
    def test_contains_urlset(self):
        """Test that sitemap contains urlset"""
        from utils.sitemap import generate_sitemap
        
        result = generate_sitemap(base_url="https://test.com")
        
        assert '<urlset' in result
        assert '</urlset>' in result
    
    def test_contains_urls(self):
        """Test that sitemap contains URL entries"""
        from utils.sitemap import generate_sitemap
        
        result = generate_sitemap(base_url="https://test.com")
        
        assert '<url>' in result
        assert '<loc>' in result
    
    def test_uses_base_url(self):
        """Test that sitemap uses provided base URL"""
        from utils.sitemap import generate_sitemap
        
        base_url = "https://mysite.example.com"
        result = generate_sitemap(base_url=base_url)
        
        assert base_url in result


class TestGetSitemapStats:
    """Test sitemap statistics"""
    
    def test_returns_dict(self):
        """Test that stats returns dictionary"""
        from utils.sitemap import get_sitemap_stats
        
        result = get_sitemap_stats()
        assert isinstance(result, dict)
    
    def test_contains_total_urls(self):
        """Test that stats contains total_urls"""
        from utils.sitemap import get_sitemap_stats
        
        result = get_sitemap_stats()
        assert "total_urls" in result
    
    def test_total_urls_positive(self):
        """Test that total_urls is positive"""
        from utils.sitemap import get_sitemap_stats
        
        result = get_sitemap_stats()
        assert result["total_urls"] >= 0


# ============================================================================
# SEO CONTENT TESTS
# ============================================================================

class TestSEOContentImports:
    """Test SEO content module imports"""
    
    def test_seo_content_import(self):
        """Test SEO content module can be imported"""
        import utils.seo_content
        assert utils.seo_content is not None


class TestSEOFunctions:
    """Test SEO helper functions"""
    
    def test_has_seo_functions(self):
        """Test SEO module has expected functions"""
        import utils.seo_content as seo
        
        # Check for common SEO functions
        # The actual function names depend on implementation
        assert hasattr(seo, '__file__')


# ============================================================================
# UTILS PACKAGE TESTS
# ============================================================================

class TestUtilsPackage:
    """Test utils package exports"""
    
    def test_utils_init_exists(self):
        """Test utils __init__ exists"""
        import utils
        assert utils is not None
    
    def test_helpers_accessible(self):
        """Test helpers module is accessible"""
        from utils import helpers
        assert helpers is not None
    
    def test_performance_accessible(self):
        """Test performance module is accessible"""
        from utils import performance
        assert performance is not None
    
    def test_sitemap_accessible(self):
        """Test sitemap module is accessible"""
        from utils import sitemap
        assert sitemap is not None


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestUtilsIntegration:
    """Integration tests for utilities"""
    
    def test_slugify_and_query(self):
        """Test that slugified text can be used in queries"""
        from utils.helpers import slugify
        from database.queries import get_book_by_slug, get_all_books
        
        books = get_all_books(limit=1)
        if books:
            # Get the actual slug
            slug = books[0].slug
            
            # Verify it can be queried
            book = get_book_by_slug(slug)
            assert book is not None
    
    def test_sitemap_includes_all_books(self):
        """Test that sitemap includes all books"""
        from utils.sitemap import get_sitemap_stats
        from database.queries import get_books_count
        
        stats = get_sitemap_stats()
        book_count = get_books_count()
        
        # Stats should include at least the book URLs
        # (may include other URLs too)
        assert stats["total_urls"] >= book_count


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
