"""
Comprehensive Tests for AI Services and Components
Tests: TTS Service, Recommendations Service, AI Service, Theme, Pagination, PWA
"""

import pytest
import sys
import os
import json
from unittest.mock import Mock, patch, MagicMock

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================================================
# TTS SERVICE TESTS
# ============================================================================

class TestTTSService:
    """Test Text-to-Speech service functionality"""
    
    def test_tts_service_import(self):
        """Test TTS service can be imported"""
        from services.tts_service import TTSService, render_audio_summary
        assert TTSService is not None
        assert render_audio_summary is not None
        print("✅ TTSService: Imports successful")
    
    def test_tts_service_instantiation(self):
        """Test TTSService can be instantiated"""
        from services.tts_service import TTSService
        service = TTSService()
        assert service is not None
        print("✅ TTSService: Instantiation successful")
    
    def test_tts_voices_defined(self):
        """Test TTS voices are defined"""
        from services.tts_service import TTSService
        
        assert hasattr(TTSService, 'VOICES')
        assert 'default' in TTSService.VOICES
        assert 'lang' in TTSService.VOICES['default']
        print("✅ TTSService: Voices defined correctly")
    
    def test_tts_has_render_methods(self):
        """Test TTS has render methods"""
        from services.tts_service import TTSService
        
        assert hasattr(TTSService, 'render_audio_player')
        assert hasattr(TTSService, 'render_mini_player')
        assert callable(TTSService.render_audio_player)
        assert callable(TTSService.render_mini_player)
        print("✅ TTSService: Render methods available")


# ============================================================================
# RECOMMENDATIONS SERVICE TESTS
# ============================================================================

class TestRecommendationsService:
    """Test the recommendation engine"""
    
    def test_recommendation_imports(self):
        """Test recommendation service imports"""
        from services.recommendations import (
            RecommendationEngine,
            BookScore,
            render_smart_recommendations
        )
        assert RecommendationEngine is not None
        assert BookScore is not None
        print("✅ RecommendationEngine: Imports successful")
    
    def test_engine_instantiation(self):
        """Test recommendation engine instantiation"""
        from services.recommendations import RecommendationEngine
        engine = RecommendationEngine()
        assert engine is not None
        print("✅ RecommendationEngine: Instantiation successful")
    
    def test_engine_has_methods(self):
        """Test engine has required methods"""
        from services.recommendations import RecommendationEngine
        engine = RecommendationEngine()
        
        assert hasattr(engine, 'get_book_keywords')
        assert hasattr(engine, 'get_recommendations')
        print("✅ RecommendationEngine: Has required methods")


# ============================================================================
# AI SERVICE TESTS
# ============================================================================

class TestAIService:
    """Test AI service functionality"""
    
    def test_ai_service_import(self):
        """Test AI service imports"""
        from services.ai_service import AIService
        assert AIService is not None
        print("✅ AIService: Import successful")
    
    def test_ai_service_instantiation(self):
        """Test AI service instantiation"""
        from services.ai_service import AIService
        service = AIService()
        assert service is not None
        print("✅ AIService: Instantiation successful")
    
    def test_ai_service_has_methods(self):
        """Test AI service has required methods"""
        from services.ai_service import AIService
        service = AIService()
        
        assert hasattr(service, 'create_book_context')
        print("✅ AIService: Has create_book_context method")


# ============================================================================
# THEME COMPONENT TESTS
# ============================================================================

class TestThemeComponent:
    """Test theme component functionality"""
    
    def test_theme_imports(self):
        """Test theme imports"""
        from components.theme import (
            COLORS, TYPOGRAPHY, SPACING,
            get_theme, set_theme, toggle_theme,
            get_theme_colors, generate_global_css
        )
        assert COLORS is not None
        assert TYPOGRAPHY is not None
        print("✅ Theme: All constants and functions imported")
    
    def test_colors_has_themes(self):
        """Test colors has theme variants"""
        from components.theme import COLORS
        
        assert "light" in COLORS
        assert "dark" in COLORS
        assert "primary" in COLORS
        print("✅ Theme: Colors has theme variants")
    
    def test_typography_structure(self):
        """Test typography dictionary structure"""
        from components.theme import TYPOGRAPHY
        
        assert "font_family_base" in TYPOGRAPHY
        assert "text_base" in TYPOGRAPHY
        print("✅ Theme: Typography structure valid")
    
    def test_generate_css(self):
        """Test CSS generation"""
        from components.theme import generate_global_css
        
        css = generate_global_css()
        
        assert isinstance(css, str)
        assert len(css) > 100  # Should be substantial CSS
        print("✅ Theme: CSS generated successfully")


# ============================================================================
# PAGINATION COMPONENT TESTS
# ============================================================================

class TestPaginationComponent:
    """Test pagination component functionality"""
    
    def test_pagination_imports(self):
        """Test pagination imports"""
        from components.pagination import (
            PaginationConfig,
            paginate_items,
            get_pagination_state,
            render_pagination
        )
        assert PaginationConfig is not None
        assert paginate_items is not None
        print("✅ Pagination: All functions imported")
    
    def test_pagination_config(self):
        """Test pagination configuration"""
        from components.pagination import PaginationConfig
        
        config = PaginationConfig(items_per_page=10)
        
        assert config.items_per_page == 10
        assert config.show_first_last == True
        print("✅ Pagination: Config works correctly")


# ============================================================================
# PWA COMPONENT TESTS
# ============================================================================

class TestPWAComponent:
    """Test PWA component functionality"""
    
    def test_pwa_imports(self):
        """Test PWA imports"""
        from components.pwa import (
            inject_pwa_support,
            render_pwa_install_button,
            render_offline_indicator
        )
        assert inject_pwa_support is not None
        print("✅ PWA: All functions imported")
    
    def test_pwa_manifest_exists(self):
        """Test PWA manifest file exists"""
        
        manifest_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "static", "manifest.json"
        )
        
        assert os.path.exists(manifest_path), "manifest.json not found"
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        assert "name" in manifest
        assert "short_name" in manifest
        assert "icons" in manifest
        print("✅ PWA: Manifest valid")
    
    def test_service_worker_exists(self):
        """Test service worker file exists"""
        
        sw_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "static", "sw.js"
        )
        
        assert os.path.exists(sw_path), "sw.js not found"
        print("✅ PWA: Service worker exists")


# ============================================================================
# PERFORMANCE UTILS TESTS
# ============================================================================

class TestPerformanceUtils:
    """Test performance utility functions"""
    
    def test_performance_imports(self):
        """Test performance utils imports"""
        from utils.performance import (
            get_optimized_image_url,
            QueryTimer
        )
        assert QueryTimer is not None
        print("✅ Performance: All functions imported")
    
    def test_optimized_image_url(self):
        """Test image URL optimization"""
        from utils.performance import get_optimized_image_url
        
        original_url = "https://example.com/image.jpg"
        optimized = get_optimized_image_url(original_url, width=300)
        
        assert isinstance(optimized, str)
        print("✅ Performance: Image URL optimization works")


# ============================================================================
# DATABASE INTEGRATION TESTS
# ============================================================================

class TestDatabaseIntegration:
    """Test database integration for new features"""
    
    def test_summary_fields(self):
        """Test that summaries have all required fields"""
        from database.queries import get_all_books, get_summary_for_book
        
        books = get_all_books()
        if not books:
            print("⚠️ No books in database")
            return
        
        book = books[0]
        summary = get_summary_for_book(book.id)
        
        if not summary:
            print("⚠️ No summary for test book")
            return
        
        # Check required fields exist
        assert hasattr(summary, 'executive_summary')
        assert hasattr(summary, 'key_takeaways')
        assert hasattr(summary, 'quotes')
        assert hasattr(summary, 'action_steps')
        print("✅ Database: Summary has all required fields")
    
    def test_takeaways_json_format(self):
        """Test that takeaways are valid JSON"""
        from database.queries import get_all_books, get_summary_for_book
        
        books = get_all_books()
        if not books:
            return
        
        summary = get_summary_for_book(books[0].id)
        if not summary:
            return
        
        if summary.key_takeaways:
            takeaways = json.loads(summary.key_takeaways)
            assert isinstance(takeaways, list)
            
            if takeaways:
                assert "title" in takeaways[0]
                assert "text" in takeaways[0]
        
        print("✅ Database: Takeaways are valid JSON format")
    
    def test_biography_content_quality(self):
        """Test biography books have quality content"""
        from database.connection import get_session
        from database.models import Genre, Book, Summary
        
        db = get_session()
        bio_genre = db.query(Genre).filter(Genre.slug == "biography").first()
        
        if not bio_genre:
            db.close()
            print("⚠️ No biography genre found")
            return
        
        bio_books = db.query(Book).filter(Book.genre_id == bio_genre.id).all()
        
        for book in bio_books:
            summary = db.query(Summary).filter(Summary.book_id == book.id).first()
            if summary and summary.key_takeaways:
                takeaways = json.loads(summary.key_takeaways)
                if takeaways:
                    # Check content is not placeholder
                    text = takeaways[0].get("text", "")
                    assert len(text) > 50, f"Short content in {book.title}"
        
        db.close()
        print(f"✅ Database: {len(bio_books)} biography books have quality content")


# ============================================================================
# SERVICES PACKAGE TESTS
# ============================================================================

class TestServicesPackage:
    """Test services package exports"""
    
    def test_services_init(self):
        """Test services package initialization"""
        from services import AIService, TTSService, RecommendationEngine
        
        assert AIService is not None
        assert TTSService is not None
        assert RecommendationEngine is not None
        print("✅ Services: Package exports work correctly")


# ============================================================================
# RUN ALL TESTS
# ============================================================================

def run_all_tests():
    """Run all service and component tests"""
    print("\n" + "="*60)
    print("🧪 BOOKWISE SERVICE & COMPONENT TESTS")
    print("="*60 + "\n")
    
    results = {
        "passed": 0,
        "failed": 0,
        "errors": []
    }
    
    test_classes = [
        TestTTSService,
        TestRecommendationsService,
        TestAIService,
        TestThemeComponent,
        TestPaginationComponent,
        TestPWAComponent,
        TestPerformanceUtils,
        TestDatabaseIntegration,
        TestServicesPackage,
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
            print(f"    Error: {error['error'][:100]}")
    
    return results


if __name__ == "__main__":
    run_all_tests()
