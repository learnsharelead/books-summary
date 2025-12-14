"""
Script to fetch and update book cover images from Google Books API
"""

import requests
import time
from database.connection import get_db_session
from database.models import Book

def get_google_books_cover(title, author):
    """
    Fetch book cover from Google Books API
    
    Args:
        title: Book title
        author: Author name
        
    Returns:
        str: Cover image URL or None
    """
    try:
        # Build search query
        query = f"{title} {author}".replace(" ", "+")
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=1"
        
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            
            if data.get('totalItems', 0) > 0:
                volume_info = data['items'][0].get('volumeInfo', {})
                image_links = volume_info.get('imageLinks', {})
                
                # Try to get the largest image available
                cover_url = (
                    image_links.get('extraLarge') or
                    image_links.get('large') or
                    image_links.get('medium') or
                    image_links.get('thumbnail')
                )
                
                # Google Books thumbnails use http, upgrade to https
                if cover_url and cover_url.startswith('http://'):
                    cover_url = cover_url.replace('http://', 'https://')
                    # Also increase image size if it's a thumbnail
                    cover_url = cover_url.replace('&zoom=1', '&zoom=2')
                
                return cover_url
    except Exception as e:
        print(f"Error fetching cover for '{title}': {e}")
    
    return None


def update_all_covers():
    """
    Update cover images for all books in the database
    """
    with get_db_session() as session:
        # Fetch all books
        books = session.query(Book).all()
        
        print(f"Found {len(books)} books to process...")
        
        updated = 0
        failed = 0
        skipped = 0
        
        for book in books:
            print(f"\n[{updated + failed + skipped + 1}/{len(books)}] Processing: {book.title}")
            
            # Check if already has a working Google Books cover
            if book.cover_image_url and 'books.google.com' in book.cover_image_url:
                print(f"⊙ Already has Google Books cover, skipping...")
                skipped += 1
                continue
            
            # Fetch new cover from Google Books
            new_cover_url = get_google_books_cover(book.title, book.author)
            
            if new_cover_url:
                # Update book
                book.cover_image_url = new_cover_url
                print(f"✓ Updated cover: {new_cover_url[:70]}...")
                updated += 1
            else:
                print(f"✗ Failed to find cover")
                failed += 1
            
            # Commit every 10 books to avoid losing progress
            if (updated + failed) % 10 == 0:
                session.commit()
                print(f"  → Progress saved ({updated} updated so far)")
            
            # Rate limiting - be nice to Google's API
            time.sleep(0.3)
        
        # Final commit
        session.commit()
        
        print(f"\n{'='*70}")
        print(f"Summary:")
        print(f"  Total books: {len(books)}")
        print(f"  Updated: {updated}")
        print(f"  Skipped (already has Google Books cover): {skipped}")
        print(f"  Failed: {failed}")
        print(f"{'='*70}")


if __name__ == "__main__":
    print("BookWise - Book Cover Updater")
    print("=" * 70)
    print("This will fetch book covers from Google Books API")
    print("and update the database with working image URLs.")
    print("=" * 70)
    
    response = input("\nProceed? (y/n): ").lower()
    
    if response == 'y':
        update_all_covers()
        print("\n✓ All book covers have been updated!")
        print("  Refresh your browser to see the changes.")
    else:
        print("Cancelled.")
