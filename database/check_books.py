"""
Script to check book data and find issues
"""

from database.connection import get_db_session
from database.models import Book
from collections import Counter

def check_books():
    """
    Check for issues in book data
    """
    with get_db_session() as session:
        books = session.query(Book).all()
        
        print(f"Total books in database: {len(books)}")
        print("=" * 80)
        
        # Check for same cover URLs
        cover_urls = [book.cover_image_url for book in books if book.cover_image_url]
        cover_counter = Counter(cover_urls)
        
        duplicated_covers = {url: count for url, count in cover_counter.items() if count > 1}
        
        if duplicated_covers:
            print(f"\n⚠️  Found {len(duplicated_covers)} cover images used by multiple books:")
            print("=" * 80)
            
            for url, count in sorted(duplicated_covers.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"\n{count} books share this cover:")
                print(f"URL: {url[:80]}...")
                
                # Show which books use this cover
                books_with_cover = session.query(Book).filter(Book.cover_image_url == url).limit(5).all()
                for book in books_with_cover:
                    print(f"  - {book.title} by {book.author}")
        
        # Show sample of recent books
        print(f"\n\n📚 Sample of last 10 books in database:")
        print("=" * 80)
        recent_books = session.query(Book).order_by(Book.id.desc()).limit(10).all()
        for book in recent_books:
            print(f"\nID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Cover: {book.cover_image_url[:60] if book.cover_image_url else 'None'}...")


if __name__ == "__main__":
    check_books()
