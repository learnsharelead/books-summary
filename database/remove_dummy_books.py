"""
Script to remove dummy/template books and keep only real books
"""

from database.connection import get_db_session
from database.models import Book

def remove_dummy_books(dry_run=True):
    """
    Remove template/dummy books that have generic titles
    
    Args:
        dry_run: If True, only show what would be deleted
    """
    with get_db_session() as session:
        # Patterns that indicate dummy books
        dummy_patterns = [
            "Vol ",  # Books titled "Something Vol 1", "Something Vol 2", etc.
            "Expert Author",  # Books by "Expert Author"
        ]
        
        # Find all books
        all_books = session.query(Book).all()
        
        # Identify dummy books
        dummy_books = []
        for book in all_books:
            is_dummy = False
            
            # Check if title contains volume numbers
            if "Vol " in book.title and book.author == "Expert Author":
                is_dummy = True
            
            if is_dummy:
                dummy_books.append(book)
        
        print(f"Total books in database: {len(all_books)}")
        print(f"Dummy/template books found: {len(dummy_books)}")
        print(f"Real books: {len(all_books) - len(dummy_books)}")
        print("=" * 80)
        
        if not dummy_books:
            print("\n✓ No dummy books found!")
            return
        
        # Show sample of what will be deleted
        print(f"\nSample of dummy books to be removed:")
        for book in dummy_books[:10]:
            if dry_run:
                print(f"  Would delete: '{book.title}' by {book.author}")
            else:
                session.delete(book)
                print(f"  ✗ Deleted: '{book.title}' by {book.author}")
        
        if len(dummy_books) > 10:
            print(f"  ... and {len(dummy_books) - 10} more")
        
        print(f"\n{'=' * 80}")
        
        if dry_run:
            print(f"⚠️  DRY RUN - No changes were made")
            print(f"   Run with dry_run=False to actually delete {len(dummy_books)} dummy books")
        else:
            session.commit()
            print(f"✓ Successfully removed {len(dummy_books)} dummy books!")
            print(f"✓ Database now contains {len(all_books) - len(dummy_books)} real books")


if __name__ == "__main__":
    print("BookWise - Dummy Book Remover")
    print("=" * 80)
    print("This will remove template/filler books created during seeding")
    print("and keep only real book summaries.")
    print("=" * 80)
    
    # First, show what would be deleted
    print("\n🔍 Scanning for dummy books...")
    remove_dummy_books(dry_run=True)
    
    print("\n" + "=" * 80)
    response = input("\nProceed with deletion? (y/n): ").lower()
    
    if response == 'y':
        print("\nRemoving dummy books...")
        remove_dummy_books(dry_run=False)
        print("\n✓ Done! Refresh your browser to see the clean data.")
    else:
        print("Cancelled.")
