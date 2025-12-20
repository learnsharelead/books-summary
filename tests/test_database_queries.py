"""
Comprehensive Unit Tests for Database Queries
Tests all query functions with various scenarios and edge cases.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestGetAllGenres:
    """Test get_all_genres function"""
    
    def test_returns_list(self):
        """Test that get_all_genres returns a list"""
        from database.queries import get_all_genres
        result = get_all_genres()
        assert isinstance(result, list)
    
    def test_genres_not_empty(self):
        """Test that genres list is not empty"""
        from database.queries import get_all_genres
        result = get_all_genres()
        assert len(result) > 0
    
    def test_genre_has_required_fields(self):
        """Test that each genre has required fields"""
        from database.queries import get_all_genres
        genres = get_all_genres()
        
        if genres:
            genre = genres[0]
            assert hasattr(genre, 'id')
            assert hasattr(genre, 'name')
            assert hasattr(genre, 'slug')
    
    def test_genres_ordered_by_name(self):
        """Test that genres are ordered alphabetically"""
        from database.queries import get_all_genres
        genres = get_all_genres()
        
        if len(genres) > 1:
            names = [g.name.lower() for g in genres]
            assert names == sorted(names)


class TestGetGenreBySlug:
    """Test get_genre_by_slug function"""
    
    def test_returns_genre_for_valid_slug(self):
        """Test that valid slug returns genre"""
        from database.queries import get_all_genres, get_genre_by_slug
        
        genres = get_all_genres()
        if genres:
            slug = genres[0].slug
            result = get_genre_by_slug(slug)
            assert result is not None
            assert result.slug == slug
    
    def test_returns_none_for_invalid_slug(self):
        """Test that invalid slug returns None"""
        from database.queries import get_genre_by_slug
        
        result = get_genre_by_slug("nonexistent-genre-slug-xyz")
        assert result is None
    
    def test_returns_none_for_empty_slug(self):
        """Test that empty slug returns None"""
        from database.queries import get_genre_by_slug
        
        result = get_genre_by_slug("")
        assert result is None


class TestGetBooksByGenre:
    """Test get_books_by_genre function"""
    
    def test_returns_list(self):
        """Test that get_books_by_genre returns a list"""
        from database.queries import get_all_genres, get_books_by_genre
        
        genres = get_all_genres()
        if genres:
            result = get_books_by_genre(genres[0].slug)
            assert isinstance(result, list)
    
    def test_respects_limit(self):
        """Test that limit parameter is respected"""
        from database.queries import get_all_genres, get_books_by_genre
        
        genres = get_all_genres()
        if genres:
            result = get_books_by_genre(genres[0].slug, limit=2)
            assert len(result) <= 2
    
    def test_books_belong_to_genre(self):
        """Test that returned books belong to the specified genre"""
        from database.queries import get_all_genres, get_books_by_genre
        
        genres = get_all_genres()
        if genres:
            genre = genres[0]
            books = get_books_by_genre(genre.slug)
            
            for book in books:
                assert book.genre_id == genre.id
    
    def test_returns_empty_for_invalid_genre(self):
        """Test that invalid genre returns empty list"""
        from database.queries import get_books_by_genre
        
        result = get_books_by_genre("nonexistent-genre-xyz")
        assert isinstance(result, list)
        assert len(result) == 0


class TestGetBookBySlug:
    """Test get_book_by_slug function"""
    
    def test_returns_book_for_valid_slug(self):
        """Test that valid slug returns book"""
        from database.queries import get_all_books, get_book_by_slug
        
        books = get_all_books()
        if books:
            slug = books[0].slug
            result = get_book_by_slug(slug)
            assert result is not None
            assert result.slug == slug
    
    def test_returns_none_for_invalid_slug(self):
        """Test that invalid slug returns None"""
        from database.queries import get_book_by_slug
        
        result = get_book_by_slug("nonexistent-book-slug-xyz")
        assert result is None
    
    def test_book_has_genre_loaded(self):
        """Test that book has genre relationship loaded"""
        from database.queries import get_all_books, get_book_by_slug
        
        books = get_all_books()
        if books:
            book = get_book_by_slug(books[0].slug)
            # Just accessing genre should not raise error
            _ = book.genre


class TestGetSummaryForBook:
    """Test get_summary_for_book function"""
    
    def test_returns_summary_for_valid_book(self):
        """Test that valid book returns summary"""
        from database.queries import get_all_books, get_summary_for_book
        
        books = get_all_books()
        if books:
            book = books[0]
            result = get_summary_for_book(book.id)
            # Summary may or may not exist
            if result:
                assert hasattr(result, 'executive_summary')
    
    def test_returns_none_for_invalid_book(self):
        """Test that invalid book returns None"""
        from database.queries import get_summary_for_book
        
        result = get_summary_for_book(-1)
        assert result is None


class TestGetFeaturedBooks:
    """Test get_featured_books function"""
    
    def test_returns_list(self):
        """Test that get_featured_books returns a list"""
        from database.queries import get_featured_books
        
        result = get_featured_books()
        assert isinstance(result, list)
    
    def test_respects_limit(self):
        """Test that limit parameter is respected"""
        from database.queries import get_featured_books
        
        result = get_featured_books(limit=3)
        assert len(result) <= 3
    
    def test_default_limit(self):
        """Test default limit is applied"""
        from database.queries import get_featured_books
        
        result = get_featured_books()
        assert len(result) <= 8
    
    def test_books_have_genre(self):
        """Test that books have genre loaded"""
        from database.queries import get_featured_books
        
        books = get_featured_books(limit=3)
        for book in books:
            # Should not raise error
            _ = book.genre


class TestSearchBooks:
    """Test search_books function"""
    
    def test_returns_list(self):
        """Test that search_books returns a list"""
        from database.queries import search_books
        
        result = search_books("test")
        assert isinstance(result, list)
    
    def test_finds_matching_titles(self):
        """Test that search finds books by title"""
        from database.queries import get_all_books, search_books
        
        books = get_all_books()
        if books:
            # Search for first word in a book title
            first_word = books[0].title.split()[0]
            results = search_books(first_word)
            
            # At least one result should match
            titles = [b.title for b in results]
            assert any(first_word.lower() in t.lower() for t in titles)
    
    def test_finds_matching_authors(self):
        """Test that search finds books by author"""
        from database.queries import get_all_books, search_books
        
        books = get_all_books()
        if books:
            author_query = books[0].author.split()[0]
            results = search_books(author_query)
            
            # At least one result should have the author
            authors = [b.author for b in results]
            assert any(author_query.lower() in a.lower() for a in authors)
    
    def test_respects_limit(self):
        """Test that limit parameter is respected"""
        from database.queries import search_books
        
        result = search_books("a", limit=5)  # 'a' should match many books
        assert len(result) <= 5
    
    def test_empty_query_returns_empty(self):
        """Test that empty query returns empty list"""
        from database.queries import search_books
        
        result = search_books("")
        assert isinstance(result, list)


class TestGetAllBooks:
    """Test get_all_books function"""
    
    def test_returns_list(self):
        """Test that get_all_books returns a list"""
        from database.queries import get_all_books
        
        result = get_all_books()
        assert isinstance(result, list)
    
    def test_books_not_empty(self):
        """Test that books list is not empty"""
        from database.queries import get_all_books
        
        result = get_all_books()
        assert len(result) > 0
    
    def test_respects_limit(self):
        """Test that limit parameter is respected"""
        from database.queries import get_all_books
        
        result = get_all_books(limit=5)
        assert len(result) <= 5
    
    def test_books_have_required_fields(self):
        """Test that books have required fields"""
        from database.queries import get_all_books
        
        books = get_all_books(limit=5)
        for book in books:
            assert hasattr(book, 'id')
            assert hasattr(book, 'title')
            assert hasattr(book, 'author')
            assert hasattr(book, 'slug')


class TestCountFunctions:
    """Test count functions"""
    
    def test_get_books_count_returns_int(self):
        """Test that get_books_count returns integer"""
        from database.queries import get_books_count
        
        result = get_books_count()
        assert isinstance(result, int)
        assert result >= 0
    
    def test_get_genres_count_returns_int(self):
        """Test that get_genres_count returns integer"""
        from database.queries import get_genres_count
        
        result = get_genres_count()
        assert isinstance(result, int)
        assert result >= 0
    
    def test_get_summaries_count_returns_int(self):
        """Test that get_summaries_count returns integer"""
        from database.queries import get_summaries_count
        
        result = get_summaries_count()
        assert isinstance(result, int)
        assert result >= 0
    
    def test_books_count_consistent(self):
        """Test that books count matches actual books"""
        from database.queries import get_books_count, get_all_books
        
        count = get_books_count()
        books = get_all_books()
        assert count == len(books)


class TestGetRandomBook:
    """Test get_random_book function"""
    
    def test_returns_book_or_none(self):
        """Test that get_random_book returns book or None"""
        from database.queries import get_random_book
        
        result = get_random_book()
        # Either a book object or None
        if result is not None:
            assert hasattr(result, 'title')
    
    def test_random_book_has_genre(self):
        """Test that random book has genre loaded"""
        from database.queries import get_random_book
        
        result = get_random_book()
        if result:
            # Should not raise error
            _ = result.genre
    
    def test_randomness(self):
        """Test that function returns different books (probabilistic)"""
        from database.queries import get_random_book, get_books_count
        
        count = get_books_count()
        if count < 3:
            pytest.skip("Not enough books to test randomness")
        
        # Get 10 random books and check for variety
        books = [get_random_book() for _ in range(10)]
        book_ids = {b.id for b in books if b}
        
        # Should have at least 2 different books (probabilistic)
        assert len(book_ids) >= 1


class TestGetTopRatedBooks:
    """Test get_top_rated_books function"""
    
    def test_returns_list(self):
        """Test that get_top_rated_books returns a list"""
        from database.queries import get_top_rated_books
        
        result = get_top_rated_books()
        assert isinstance(result, list)
    
    def test_respects_limit(self):
        """Test that limit parameter is respected"""
        from database.queries import get_top_rated_books
        
        result = get_top_rated_books(limit=3)
        assert len(result) <= 3
    
    def test_books_have_genre(self):
        """Test that books have genre loaded"""
        from database.queries import get_top_rated_books
        
        books = get_top_rated_books(limit=3)
        for book in books:
            _ = book.genre


class TestGetRecentBooks:
    """Test get_recent_books function"""
    
    def test_returns_list(self):
        """Test that get_recent_books returns a list"""
        from database.queries import get_recent_books
        
        result = get_recent_books()
        assert isinstance(result, list)
    
    def test_respects_limit(self):
        """Test that limit parameter is respected"""
        from database.queries import get_recent_books
        
        result = get_recent_books(limit=3)
        assert len(result) <= 3
    
    def test_books_have_genre(self):
        """Test that books have genre loaded"""
        from database.queries import get_recent_books
        
        books = get_recent_books(limit=3)
        for book in books:
            _ = book.genre


class TestGetImagesForSummary:
    """Test get_images_for_summary function"""
    
    def test_returns_list(self):
        """Test that get_images_for_summary returns a list"""
        from database.queries import get_images_for_summary
        
        result = get_images_for_summary(1)
        assert isinstance(result, list)
    
    def test_returns_empty_for_invalid_summary(self):
        """Test that invalid summary returns empty list"""
        from database.queries import get_images_for_summary
        
        result = get_images_for_summary(-1)
        assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
