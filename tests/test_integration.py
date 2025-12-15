"""
Integration tests for BookWise pages
Tests that pages can be imported and key functions work
"""

import sys
import os
import traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test all critical imports"""
    print("\n📦 Testing Imports...")
    print("-" * 50)
    
    errors = []
    
    # Test database imports
    imports_to_test = [
        ("database.models", ["Genre", "Book", "Summary", "SummaryImage"]),
        ("database.connection", ["get_db_session", "engine"]),
        ("database.queries", [
            "get_all_genres", "get_all_books", "get_books_count",
            "get_genres_count", "get_featured_books", "get_random_book",
            "get_top_rated_books", "get_recent_books", "search_books",
            "get_book_by_slug", "get_genre_by_slug", "get_books_by_genre"
        ]),
    ]
    
    for module_name, functions in imports_to_test:
        try:
            module = __import__(module_name, fromlist=functions)
            for func_name in functions:
                if not hasattr(module, func_name):
                    errors.append(f"Missing: {module_name}.{func_name}")
                else:
                    print(f"  ✅ {module_name}.{func_name}")
        except Exception as e:
            errors.append(f"Import error {module_name}: {e}")
            print(f"  ❌ {module_name}: {e}")
    
    return errors


def test_component_imports():
    """Test all component imports"""
    print("\n🧩 Testing Component Imports...")
    print("-" * 50)
    
    errors = []
    
    component_files = [
        "components.navigation",
        "components.footer",
        "components.search",
        "components.discovery",
        "components.theme",
        "components.newsletter",
        "components.reading_lists",
        "components.book_of_day",
        "components.testimonials",
        "components.quick_actions",
        "components.progress_tracker",
        "components.related_books",
        "components.filters",
        "components.stats_bar",
        "components.genre_themes",
        "components.image_handler",
        "components.book_card",
        "components.genre_card",
        "components.seo",
    ]
    
    for comp in component_files:
        try:
            __import__(comp)
            print(f"  ✅ {comp}")
        except Exception as e:
            errors.append(f"{comp}: {e}")
            print(f"  ❌ {comp}: {e}")
    
    return errors


def test_query_functions():
    """Test that query functions return correct types"""
    print("\n🔍 Testing Query Functions...")
    print("-" * 50)
    
    errors = []
    
    from database.queries import (
        get_all_genres, get_all_books, get_books_count,
        get_featured_books, get_random_book, get_top_rated_books,
        get_recent_books, search_books
    )
    
    tests = [
        ("get_all_genres()", get_all_genres, list),
        ("get_all_books()", get_all_books, list),
        ("get_books_count()", get_books_count, int),
        ("get_featured_books(6)", lambda: get_featured_books(6), list),
        ("get_random_book()", get_random_book, (type(None), object)),
        ("get_top_rated_books(6)", lambda: get_top_rated_books(6), list),
        ("get_recent_books(6)", lambda: get_recent_books(6), list),
        ("search_books('test')", lambda: search_books("test"), list),
    ]
    
    for name, func, expected_type in tests:
        try:
            result = func()
            if isinstance(expected_type, tuple):
                assert isinstance(result, expected_type), f"Expected {expected_type}, got {type(result)}"
            else:
                assert isinstance(result, expected_type), f"Expected {expected_type}, got {type(result)}"
            print(f"  ✅ {name} -> {type(result).__name__}")
        except Exception as e:
            errors.append(f"{name}: {e}")
            print(f"  ❌ {name}: {e}")
    
    return errors


def test_data_integrity():
    """Test data integrity in database"""
    print("\n📊 Testing Data Integrity...")
    print("-" * 50)
    
    errors = []
    
    from database.queries import get_all_genres, get_all_books, get_books_by_genre
    
    # Check genres
    genres = get_all_genres()
    print(f"  📚 Genres: {len(genres)}")
    
    # Check each genre has books
    for genre in genres:
        books = get_books_by_genre(genre.slug)
        if len(books) == 0:
            errors.append(f"Genre '{genre.name}' has no books")
            print(f"    ⚠️ {genre.name}: 0 books")
        else:
            print(f"    ✅ {genre.name}: {len(books)} books")
    
    # Check books have required fields
    books = get_all_books()
    print(f"\n  📖 Books: {len(books)}")
    
    missing_fields = {"title": 0, "author": 0, "slug": 0, "genre": 0}
    
    for book in books:
        if not book.title:
            missing_fields["title"] += 1
        if not book.author:
            missing_fields["author"] += 1
        if not book.slug:
            missing_fields["slug"] += 1
        if not book.genre:
            missing_fields["genre"] += 1
    
    for field, count in missing_fields.items():
        if count > 0:
            errors.append(f"{count} books missing {field}")
            print(f"    ⚠️ {count} books missing '{field}'")
        else:
            print(f"    ✅ All books have '{field}'")
    
    return errors


def test_reading_lists():
    """Test reading lists have valid book slugs"""
    print("\n📋 Testing Reading Lists...")
    print("-" * 50)
    
    errors = []
    
    from components.reading_lists import READING_LISTS
    from database.queries import get_book_by_slug
    
    for list_id, reading_list in READING_LISTS.items():
        print(f"\n  📋 {reading_list['title']}")
        found = 0
        missing = []
        
        for book_slug in reading_list["books"]:
            book = get_book_by_slug(book_slug)
            if book:
                found += 1
            else:
                missing.append(book_slug)
        
        print(f"    Found: {found}/{len(reading_list['books'])}")
        
        if missing:
            for slug in missing:
                errors.append(f"Reading list '{list_id}': Missing book '{slug}'")
                print(f"    ⚠️ Missing: {slug}")
    
    return errors


def run_integration_tests():
    """Run all integration tests"""
    print("\n" + "="*60)
    print("🔬 BOOKWISE INTEGRATION TESTS")
    print("="*60)
    
    all_errors = []
    
    # Run tests
    all_errors.extend(test_imports())
    all_errors.extend(test_component_imports())
    all_errors.extend(test_query_functions())
    all_errors.extend(test_data_integrity())
    all_errors.extend(test_reading_lists())
    
    # Summary
    print("\n" + "="*60)
    print("📊 INTEGRATION TEST SUMMARY")
    print("="*60)
    
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} issues:\n")
        for i, error in enumerate(all_errors, 1):
            print(f"  {i}. {error}")
    else:
        print("\n✅ All integration tests passed!")
    
    return all_errors


if __name__ == "__main__":
    errors = run_integration_tests()
    sys.exit(1 if errors else 0)
