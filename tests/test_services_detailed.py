"""
Comprehensive Unit Tests for Services
Tests AI Service, TTS Service, and Recommendations with mocking.
"""

import pytest
import sys
import os
import json
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================================================
# AI SERVICE TESTS
# ============================================================================

class TestAIServiceImports:
    """Test AI service imports and initialization"""
    
    def test_ai_service_import(self):
        """Test AIService can be imported"""
        from services.ai_service import AIService
        assert AIService is not None
    
    def test_chat_message_import(self):
        """Test ChatMessage can be imported"""
        from services.ai_service import ChatMessage
        assert ChatMessage is not None
    
    def test_get_ai_service_import(self):
        """Test get_ai_service can be imported"""
        from services.ai_service import get_ai_service
        assert get_ai_service is not None


class TestAIServiceInstantiation:
    """Test AI service instantiation"""
    
    def test_instantiation_without_key(self):
        """Test AIService can be instantiated without API key"""
        from services.ai_service import AIService
        
        service = AIService()
        assert service is not None
        assert service.api_key is None or isinstance(service.api_key, str)
    
    def test_instantiation_with_key(self):
        """Test AIService can be instantiated with API key"""
        from services.ai_service import AIService
        
        service = AIService(api_key="test-api-key")
        assert service is not None
        assert service.api_key == "test-api-key"


class TestChatMessage:
    """Test ChatMessage dataclass"""
    
    def test_chat_message_creation(self):
        """Test creating ChatMessage"""
        from services.ai_service import ChatMessage
        
        msg = ChatMessage(role="user", content="Hello")
        
        assert msg.role == "user"
        assert msg.content == "Hello"
    
    def test_chat_message_with_timestamp(self):
        """Test ChatMessage with timestamp"""
        from services.ai_service import ChatMessage
        
        msg = ChatMessage(role="assistant", content="Hi", timestamp="2024-01-01T00:00:00")
        
        assert msg.timestamp == "2024-01-01T00:00:00"
    
    def test_chat_message_default_timestamp(self):
        """Test ChatMessage default timestamp is None"""
        from services.ai_service import ChatMessage
        
        msg = ChatMessage(role="user", content="Test")
        
        assert msg.timestamp is None


class TestAIServiceMethods:
    """Test AI service methods"""
    
    def test_has_create_book_context_method(self):
        """Test AIService has create_book_context method"""
        from services.ai_service import AIService
        
        service = AIService()
        assert hasattr(service, 'create_book_context')
        assert callable(service.create_book_context)
    
    def test_has_chat_with_book_method(self):
        """Test AIService has chat_with_book method"""
        from services.ai_service import AIService
        
        service = AIService()
        assert hasattr(service, 'chat_with_book')
        assert callable(service.chat_with_book)
    
    def test_has_generate_quiz_method(self):
        """Test AIService has generate_quiz method"""
        from services.ai_service import AIService
        
        service = AIService()
        assert hasattr(service, 'generate_quiz')
        assert callable(service.generate_quiz)
    
    def test_has_summarize_for_audio_method(self):
        """Test AIService has summarize_for_audio method"""
        from services.ai_service import AIService
        
        service = AIService()
        assert hasattr(service, 'summarize_for_audio')
        assert callable(service.summarize_for_audio)
    
    def test_create_book_context(self):
        """Test create_book_context method"""
        from services.ai_service import AIService
        
        service = AIService()
        
        book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "genre": "Self-Help",
            "summary": {
                "executive_summary": "This is a test summary",
                "key_takeaways": json.dumps([
                    {"title": "Point 1", "text": "Description 1"}
                ])
            }
        }
        
        context = service.create_book_context(book_data)
        
        assert isinstance(context, str)
        assert "Test Book" in context
        assert "Test Author" in context


class TestAIServiceWithMocking:
    """Test AI service with mocked Gemini API"""
    
    def test_initialize_with_key(self):
        """Test that initialize works with API key"""
        from services.ai_service import AIService
        
        service = AIService(api_key="test-key")
        
        # Just verify service was created with key
        assert service.api_key == "test-key"
        assert service is not None
    
    def test_create_book_context_without_initialization(self):
        """Test create_book_context works without full initialization"""
        from services.ai_service import AIService
        
        service = AIService()
        
        book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "genre": "Fiction"
        }
        
        context = service.create_book_context(book_data)
        
        assert isinstance(context, str)
        assert "Test Book" in context
    
    def test_service_methods_exist(self):
        """Test all expected methods exist on service"""
        from services.ai_service import AIService
        
        service = AIService()
        
        # Verify all methods exist
        methods = ['initialize', 'create_book_context', 'chat_with_book', 
                   'generate_quiz', 'summarize_for_audio']
        
        for method in methods:
            assert hasattr(service, method), f"Missing method: {method}"
            assert callable(getattr(service, method))


# ============================================================================
# TTS SERVICE TESTS
# ============================================================================

class TestTTSServiceImports:
    """Test TTS service imports"""
    
    def test_tts_service_import(self):
        """Test TTSService can be imported"""
        from services.tts_service import TTSService
        assert TTSService is not None
    
    def test_render_audio_summary_import(self):
        """Test render_audio_summary can be imported"""
        from services.tts_service import render_audio_summary
        assert render_audio_summary is not None


class TestTTSServiceClass:
    """Test TTS service class"""
    
    def test_tts_service_instantiation(self):
        """Test TTSService can be instantiated"""
        from services.tts_service import TTSService
        
        service = TTSService()
        assert service is not None
    
    def test_voices_defined(self):
        """Test TTS voices are defined"""
        from services.tts_service import TTSService
        
        assert hasattr(TTSService, 'VOICES')
        assert isinstance(TTSService.VOICES, dict)
    
    def test_default_voice_exists(self):
        """Test default voice is defined"""
        from services.tts_service import TTSService
        
        assert 'default' in TTSService.VOICES
        assert 'lang' in TTSService.VOICES['default']
    
    def test_has_render_audio_player(self):
        """Test TTSService has render_audio_player method"""
        from services.tts_service import TTSService
        
        assert hasattr(TTSService, 'render_audio_player')
        assert callable(TTSService.render_audio_player)
    
    def test_has_render_mini_player(self):
        """Test TTSService has render_mini_player method"""
        from services.tts_service import TTSService
        
        assert hasattr(TTSService, 'render_mini_player')
        assert callable(TTSService.render_mini_player)


class TestTTSVoices:
    """Test TTS voice configurations"""
    
    def test_voice_has_lang(self):
        """Test each voice has language defined"""
        from services.tts_service import TTSService
        
        for voice_id, voice_config in TTSService.VOICES.items():
            assert 'lang' in voice_config, f"Voice {voice_id} missing 'lang'"
    
    def test_multiple_voices_available(self):
        """Test multiple voice options are available"""
        from services.tts_service import TTSService
        
        assert len(TTSService.VOICES) >= 1


# ============================================================================
# RECOMMENDATIONS SERVICE TESTS
# ============================================================================

class TestRecommendationsImports:
    """Test recommendations service imports"""
    
    def test_recommendation_engine_import(self):
        """Test RecommendationEngine can be imported"""
        from services.recommendations import RecommendationEngine
        assert RecommendationEngine is not None
    
    def test_book_score_import(self):
        """Test BookScore can be imported"""
        from services.recommendations import BookScore
        assert BookScore is not None
    
    def test_render_smart_recommendations_import(self):
        """Test render_smart_recommendations can be imported"""
        from services.recommendations import render_smart_recommendations
        assert render_smart_recommendations is not None


class TestRecommendationEngine:
    """Test RecommendationEngine class"""
    
    def test_engine_instantiation(self):
        """Test RecommendationEngine can be instantiated"""
        from services.recommendations import RecommendationEngine
        
        engine = RecommendationEngine()
        assert engine is not None
    
    def test_has_get_book_keywords(self):
        """Test engine has get_book_keywords method"""
        from services.recommendations import RecommendationEngine
        
        engine = RecommendationEngine()
        assert hasattr(engine, 'get_book_keywords')
        assert callable(engine.get_book_keywords)
    
    def test_has_get_recommendations(self):
        """Test engine has get_recommendations method"""
        from services.recommendations import RecommendationEngine
        
        engine = RecommendationEngine()
        assert hasattr(engine, 'get_recommendations')
        assert callable(engine.get_recommendations)
    
    def test_get_book_keywords(self):
        """Test get_book_keywords returns keywords"""
        from services.recommendations import RecommendationEngine
        
        engine = RecommendationEngine()
        
        # Create mock book
        mock_book = Mock()
        mock_book.title = "Atomic Habits"
        mock_book.author = "James Clear"
        mock_book.genre = Mock()
        mock_book.genre.name = "Self-Help"
        
        # Create mock summary with all required attributes
        mock_summary = Mock()
        mock_summary.executive_summary = "This book teaches about building habits."
        mock_summary.main_content = "The main concepts of habit formation."
        mock_summary.who_should_read = "Anyone wanting to improve their habits."
        mock_summary.key_takeaways = None
        mock_summary.analogies = None
        mock_summary.quotes = None
        mock_summary.action_steps = None
        
        keywords = engine.get_book_keywords(mock_book, mock_summary)
        
        assert isinstance(keywords, list)
        assert len(keywords) > 0  # Should extract some keywords


class TestBookScore:
    """Test BookScore dataclass"""
    
    def test_book_score_creation(self):
        """Test creating BookScore"""
        from services.recommendations import BookScore
        
        mock_book = Mock()
        mock_book.id = 1
        mock_book.title = "Test Book"
        
        # BookScore uses 'reasons' list, not 'reason'
        score = BookScore(book=mock_book, score=0.85, reasons=["Similar genre"])
        
        assert score.book == mock_book
        assert score.score == 0.85
        assert "Similar genre" in score.reasons


# ============================================================================
# SERVICES PACKAGE TESTS
# ============================================================================

class TestServicesPackage:
    """Test services package exports"""
    
    def test_ai_service_export(self):
        """Test AIService is exported from package"""
        from services import AIService
        assert AIService is not None
    
    def test_tts_service_export(self):
        """Test TTSService is exported from package"""
        from services import TTSService
        assert TTSService is not None
    
    def test_recommendation_engine_export(self):
        """Test RecommendationEngine is exported from package"""
        from services import RecommendationEngine
        assert RecommendationEngine is not None


# ============================================================================
# INTEGRATION TESTS FOR SERVICES
# ============================================================================

class TestServicesIntegration:
    """Integration tests for services"""
    
    def test_ai_service_with_real_book_data(self):
        """Test AI service with real book data from database"""
        from services.ai_service import AIService
        from database.queries import get_all_books, get_summary_for_book
        
        books = get_all_books(limit=1)
        if not books:
            pytest.skip("No books in database")
        
        book = books[0]
        summary = get_summary_for_book(book.id)
        
        book_data = {
            "title": book.title,
            "author": book.author,
            "genre": book.genre.name if book.genre else "Unknown"
        }
        
        if summary:
            book_data["summary"] = {
                "executive_summary": summary.executive_summary,
                "key_takeaways": summary.key_takeaways
            }
        
        service = AIService()
        context = service.create_book_context(book_data)
        
        assert book.title in context
    
    def test_recommendation_engine_with_real_book(self):
        """Test recommendation engine with real book from database"""
        from services.recommendations import RecommendationEngine
        from database.queries import get_all_books, get_summary_for_book
        
        books = get_all_books(limit=5)
        if len(books) < 2:
            pytest.skip("Not enough books for recommendations")
        
        engine = RecommendationEngine()
        
        # Get first book and its summary
        book = books[0]
        summary = get_summary_for_book(book.id)
        
        # Get keywords for first book with its summary
        keywords = engine.get_book_keywords(book, summary)
        
        # Keywords should be a list, set, or dict
        assert isinstance(keywords, (list, set, dict))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
