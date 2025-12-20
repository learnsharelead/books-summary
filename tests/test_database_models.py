"""
Comprehensive Unit Tests for Database Models and Connection
Tests database models, relationships, and connection handling.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================================================
# DATABASE CONNECTION TESTS
# ============================================================================

class TestDatabaseConnection:
    """Test database connection functionality"""
    
    def test_connection_import(self):
        """Test connection module can be imported"""
        from database.connection import get_db_session, engine
        assert get_db_session is not None
        assert engine is not None
    
    def test_get_db_session_context_manager(self):
        """Test get_db_session works as context manager"""
        from database.connection import get_db_session
        
        with get_db_session() as session:
            assert session is not None
    
    def test_session_can_query(self):
        """Test session can execute queries"""
        from database.connection import get_db_session
        from database.models import Genre
        
        with get_db_session() as session:
            # Simple query should work
            result = session.query(Genre).first()
            # May return None if no data, but should not raise
    
    def test_engine_is_configured(self):
        """Test engine is properly configured"""
        from database.connection import engine
        
        assert engine is not None
        assert engine.url is not None


# ============================================================================
# DATABASE MODELS TESTS
# ============================================================================

class TestGenreModel:
    """Test Genre model"""
    
    def test_genre_import(self):
        """Test Genre model can be imported"""
        from database.models import Genre
        assert Genre is not None
    
    def test_genre_has_required_fields(self):
        """Test Genre has required fields"""
        from database.models import Genre
        
        # Check class attributes
        assert hasattr(Genre, 'id')
        assert hasattr(Genre, 'name')
        assert hasattr(Genre, 'slug')
    
    def test_genre_has_books_relationship(self):
        """Test Genre has books relationship"""
        from database.models import Genre
        
        assert hasattr(Genre, 'books')
    
    def test_genre_instance_creation(self):
        """Test Genre instance can be created"""
        from database.models import Genre
        
        genre = Genre(name="Test Genre", slug="test-genre")
        
        assert genre.name == "Test Genre"
        assert genre.slug == "test-genre"


class TestBookModel:
    """Test Book model"""
    
    def test_book_import(self):
        """Test Book model can be imported"""
        from database.models import Book
        assert Book is not None
    
    def test_book_has_required_fields(self):
        """Test Book has required fields"""
        from database.models import Book
        
        assert hasattr(Book, 'id')
        assert hasattr(Book, 'title')
        assert hasattr(Book, 'author')
        assert hasattr(Book, 'slug')
        assert hasattr(Book, 'genre_id')
    
    def test_book_has_genre_relationship(self):
        """Test Book has genre relationship"""
        from database.models import Book
        
        assert hasattr(Book, 'genre')
    
    def test_book_has_summary_relationship(self):
        """Test Book has summary relationship"""
        from database.models import Book
        
        assert hasattr(Book, 'summary') or hasattr(Book, 'summaries')
    
    def test_book_instance_creation(self):
        """Test Book instance can be created"""
        from database.models import Book
        
        book = Book(
            title="Test Book",
            author="Test Author",
            slug="test-book",
            genre_id=1
        )
        
        assert book.title == "Test Book"
        assert book.author == "Test Author"
    
    def test_book_optional_fields(self):
        """Test Book has optional fields"""
        from database.models import Book
        
        assert hasattr(Book, 'cover_image_url')
        assert hasattr(Book, 'publication_year')


class TestSummaryModel:
    """Test Summary model"""
    
    def test_summary_import(self):
        """Test Summary model can be imported"""
        from database.models import Summary
        assert Summary is not None
    
    def test_summary_has_required_fields(self):
        """Test Summary has required fields"""
        from database.models import Summary
        
        assert hasattr(Summary, 'id')
        assert hasattr(Summary, 'book_id')
        assert hasattr(Summary, 'executive_summary')
    
    def test_summary_content_fields(self):
        """Test Summary has content fields"""
        from database.models import Summary
        
        assert hasattr(Summary, 'key_takeaways')
        assert hasattr(Summary, 'quotes')
        assert hasattr(Summary, 'action_steps')
    
    def test_summary_has_book_relationship(self):
        """Test Summary has book relationship"""
        from database.models import Summary
        
        assert hasattr(Summary, 'book')


class TestSummaryImageModel:
    """Test SummaryImage model"""
    
    def test_summary_image_import(self):
        """Test SummaryImage model can be imported"""
        from database.models import SummaryImage
        assert SummaryImage is not None
    
    def test_summary_image_has_required_fields(self):
        """Test SummaryImage has required fields"""
        from database.models import SummaryImage
        
        assert hasattr(SummaryImage, 'id')
        assert hasattr(SummaryImage, 'summary_id')
    
    def test_summary_image_has_url_field(self):
        """Test SummaryImage has URL field"""
        from database.models import SummaryImage
        
        assert hasattr(SummaryImage, 'image_url') or hasattr(SummaryImage, 'url')


# ============================================================================
# MODEL RELATIONSHIPS TESTS
# ============================================================================

class TestModelRelationships:
    """Test model relationships"""
    
    def test_genre_to_books(self):
        """Test Genre to Books relationship"""
        from database.connection import get_db_session
        from database.models import Genre
        
        with get_db_session() as session:
            genre = session.query(Genre).first()
            if genre:
                # Accessing books should not raise
                _ = genre.books
    
    def test_book_to_genre(self):
        """Test Book to Genre relationship"""
        from database.connection import get_db_session
        from database.models import Book
        
        with get_db_session() as session:
            book = session.query(Book).first()
            if book:
                # Accessing genre should not raise
                _ = book.genre
    
    def test_book_to_summary(self):
        """Test Book to Summary relationship"""
        from database.connection import get_db_session
        from database.models import Book, Summary
        
        with get_db_session() as session:
            book = session.query(Book).first()
            if book:
                # Query summary for book
                summary = session.query(Summary).filter(Summary.book_id == book.id).first()
                # May be None, but should not raise


# ============================================================================
# DATA INTEGRITY TESTS
# ============================================================================

class TestDataIntegrity:
    """Test data integrity"""
    
    def test_all_books_have_genre(self):
        """Test all books have a genre assigned"""
        from database.connection import get_db_session
        from database.models import Book
        
        with get_db_session() as session:
            books = session.query(Book).all()
            
            for book in books:
                assert book.genre_id is not None, f"Book '{book.title}' has no genre"
    
    def test_all_books_have_slug(self):
        """Test all books have a slug"""
        from database.connection import get_db_session
        from database.models import Book
        
        with get_db_session() as session:
            books = session.query(Book).all()
            
            for book in books:
                assert book.slug is not None, f"Book '{book.title}' has no slug"
                assert len(book.slug) > 0, f"Book '{book.title}' has empty slug"
    
    def test_book_slugs_are_unique(self):
        """Test book slugs are unique"""
        from database.connection import get_db_session
        from database.models import Book
        
        with get_db_session() as session:
            books = session.query(Book).all()
            slugs = [book.slug for book in books]
            
            assert len(slugs) == len(set(slugs)), "Duplicate book slugs found"
    
    def test_genre_slugs_are_unique(self):
        """Test genre slugs are unique"""
        from database.connection import get_db_session
        from database.models import Genre
        
        with get_db_session() as session:
            genres = session.query(Genre).all()
            slugs = [genre.slug for genre in genres]
            
            assert len(slugs) == len(set(slugs)), "Duplicate genre slugs found"
    
    def test_all_genres_have_books(self):
        """Test all genres have at least one book"""
        from database.connection import get_db_session
        from database.models import Genre, Book
        
        with get_db_session() as session:
            genres = session.query(Genre).all()
            
            for genre in genres:
                book_count = session.query(Book).filter(Book.genre_id == genre.id).count()
                assert book_count > 0, f"Genre '{genre.name}' has no books"


# ============================================================================
# SUMMARY CONTENT TESTS
# ============================================================================

class TestSummaryContent:
    """Test summary content quality"""
    
    def test_summaries_have_executive_summary(self):
        """Test summaries have executive summary"""
        from database.connection import get_db_session
        from database.models import Summary
        
        with get_db_session() as session:
            summaries = session.query(Summary).limit(10).all()
            
            for summary in summaries:
                if summary.executive_summary:
                    assert len(summary.executive_summary) > 50, "Executive summary too short"
    
    def test_takeaways_valid_json(self):
        """Test key_takeaways is valid JSON"""
        import json
        from database.connection import get_db_session
        from database.models import Summary
        
        with get_db_session() as session:
            summaries = session.query(Summary).limit(10).all()
            
            for summary in summaries:
                if summary.key_takeaways:
                    try:
                        takeaways = json.loads(summary.key_takeaways)
                        assert isinstance(takeaways, list)
                    except json.JSONDecodeError:
                        pytest.fail(f"Invalid JSON in key_takeaways for summary {summary.id}")
    
    def test_quotes_valid_json(self):
        """Test quotes is valid JSON"""
        import json
        from database.connection import get_db_session
        from database.models import Summary
        
        with get_db_session() as session:
            summaries = session.query(Summary).limit(10).all()
            
            for summary in summaries:
                if summary.quotes:
                    try:
                        quotes = json.loads(summary.quotes)
                        assert isinstance(quotes, list)
                    except json.JSONDecodeError:
                        pytest.fail(f"Invalid JSON in quotes for summary {summary.id}")
    
    def test_action_steps_valid_json(self):
        """Test action_steps is valid JSON"""
        import json
        from database.connection import get_db_session
        from database.models import Summary
        
        with get_db_session() as session:
            summaries = session.query(Summary).limit(10).all()
            
            for summary in summaries:
                if summary.action_steps:
                    try:
                        steps = json.loads(summary.action_steps)
                        assert isinstance(steps, list)
                    except json.JSONDecodeError:
                        pytest.fail(f"Invalid JSON in action_steps for summary {summary.id}")


# ============================================================================
# DATABASE QUERIES EDGE CASES
# ============================================================================

class TestQueryEdgeCases:
    """Test edge cases in queries"""
    
    def test_search_with_special_characters(self):
        """Test search handles special characters"""
        from database.queries import search_books
        
        # These should not raise errors
        result = search_books("test's")
        assert isinstance(result, list)
        
        result = search_books("test%")
        assert isinstance(result, list)
        
        result = search_books("test_underscore")
        assert isinstance(result, list)
    
    def test_get_book_by_slug_with_special_chars(self):
        """Test get_book_by_slug handles special characters"""
        from database.queries import get_book_by_slug
        
        # These should not raise errors
        result = get_book_by_slug("test's-book")
        # May be None, but should not raise
    
    def test_featured_books_with_zero_limit(self):
        """Test featured books with zero limit"""
        from database.queries import get_featured_books
        
        result = get_featured_books(limit=0)
        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_search_with_very_long_query(self):
        """Test search with very long query"""
        from database.queries import search_books
        
        long_query = "a" * 1000
        result = search_books(long_query)
        assert isinstance(result, list)
    
    def test_get_books_by_genre_with_special_slug(self):
        """Test get_books_by_genre with special slug"""
        from database.queries import get_books_by_genre
        
        result = get_books_by_genre("non-existent-genre-123")
        assert isinstance(result, list)
        assert len(result) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
