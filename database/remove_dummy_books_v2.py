"""
Script to remove dummy/template books with proper cascade handling
"""

from database.connection import get_db_session
from database.models import Book, Summary
from sqlalchemy import delete

def remove_dummy_books_properly():
    """
    Remove template/dummy books and their related data
    """
    with get_db_session() as session:
        # Find dummy books
        dummy_books = session.query(Book).filter(
            Book.title.like("%Vol %"),
            Book.author == "Expert Author"
        ).all()
        
        total_books = session.query(Book).count()
        
        print(f"Total books in database: {total_books}")
        print(f"Dummy/template books found: {len(dummy_books)}")
        print(f"Real books: {total_books - len(dummy_books)}")
        print("=" * 80)
        
        if not dummy_books:
            print("\n✓ No dummy books found!")
            return
        
        # Show sample
        print(f"\nSample of dummy books to be removed:")
        for book in dummy_books[:10]:
            print(f"  - '{book.title}' by {book.author}")
        
        if len(dummy_books) > 10:
            print(f"  ... and {len(dummy_books) - 10} more")
        
        print(f"\n{'=' * 80}")
        response = input(f"\nRemove {len(dummy_books)} dummy books? (y/n): ").lower()
        
        if response != 'y':
            print("Cancelled.")
            return
        
        # Delete summaries first (to avoid foreign key constraint)
        dummy_book_ids = [book.id for book in dummy_books]
        
        print("\nRemoving associated summaries...")
        deleted_summaries = session.query(Summary).filter(
            Summary.book_id.in_(dummy_book_ids)
        ).delete(synchronize_session=False)
        print(f"✓ Removed {deleted_summaries} summaries")
        
        # Now delete the books
        print("\nRemoving dummy books...")
        deleted_books = session.query(Book).filter(
            Book.id.in_(dummy_book_ids)
        ).delete(synchronize_session=False)
        
        session.commit()
        
        print(f"\n{'=' * 80}")
        print(f"✓ Successfully removed:")
        print(f"  - {deleted_summaries} summaries")
        print(f"  - {deleted_books} books")
        print(f"\n✓ Database now contains {total_books - deleted_books} real books")
        print(f"✓ Refresh your browser to see the clean data!")


if __name__ == "__main__":
    print("BookWise - Dummy Book Remover (v2)")
    print("=" * 80)
    print("This will remove template/filler books and their summaries")
    print("=" * 80)
    print()
    
    remove_dummy_books_properly()
