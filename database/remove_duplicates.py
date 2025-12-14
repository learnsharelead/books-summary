"""
Script to find and remove duplicate books from the database
"""

from database.connection import get_db_session
from database.models import Book
from sqlalchemy import func

def find_duplicates():
    """
    Find duplicate books based on title + author
    """
    with get_db_session() as session:
        # Find duplicate title+author combinations
        duplicates = (
            session.query(
                Book.title,
                Book.author,
                func.count(Book.id).label('count')
            )
            .group_by(Book.title, Book.author)
            .having(func.count(Book.id) > 1)
            .all()
        )
        
        return duplicates


def remove_duplicates(dry_run=True):
    """
    Remove duplicate books, keeping only the first occurrence
    
    Args:
        dry_run: If True, only show what would be deleted
    """
    with get_db_session() as session:
        # Find all duplicate groups
        duplicates = (
            session.query(
                Book.title,
                Book.author,
                func.count(Book.id).label('count')
            )
            .group_by(Book.title, Book.author)
            .having(func.count(Book.id) > 1)
            .all()
        )
        
        if not duplicates:
            print("✓ No duplicates found!")
            return
        
        print(f"Found {len(duplicates)} duplicate book groups:")
        print("=" * 80)
        
        total_to_remove = 0
        
        for title, author, count in duplicates:
            print(f"\n📚 '{title}' by {author}")
            print(f"   Found {count} copies")
            
            # Get all instances of this book
            books = (
                session.query(Book)
                .filter(Book.title == title, Book.author == author)
                .order_by(Book.id)
                .all()
            )
            
            # Keep the first one, mark others for deletion
            to_delete = books[1:]  # All except the first
            total_to_remove += len(to_delete)
            
            for book in to_delete:
                if dry_run:
                    print(f"   Would delete: ID={book.id}, Slug={book.slug}")
                else:
                    session.delete(book)
                    print(f"   ✗ Deleted: ID={book.id}, Slug={book.slug}")
        
        print(f"\n{'=' * 80}")
        print(f"Summary:")
        print(f"  Duplicate groups: {len(duplicates)}")
        print(f"  Books to remove: {total_to_remove}")
        
        if dry_run:
            print(f"\n⚠️  DRY RUN - No changes were made")
            print(f"   Run with dry_run=False to actually delete duplicates")
        else:
            session.commit()
            print(f"\n✓ Duplicates removed successfully!")


if __name__ == "__main__":
    print("BookWise - Duplicate Book Remover")
    print("=" * 80)
    
    # First, show what would be deleted
    print("\nScanning for duplicates...")
    duplicates = find_duplicates()
    
    if duplicates:
        print(f"\nFound {len(duplicates)} duplicate book groups!")
        
        print("\n" + "=" * 80)
        print("DRY RUN - Showing what would be deleted:")
        print("=" * 80)
        remove_duplicates(dry_run=True)
        
        print("\n" + "=" * 80)
        response = input("\nProceed with deletion? (y/n): ").lower()
        
        if response == 'y':
            print("\nRemoving duplicates...")
            remove_duplicates(dry_run=False)
        else:
            print("Cancelled.")
    else:
        print("\n✓ No duplicates found! Database is clean.")
