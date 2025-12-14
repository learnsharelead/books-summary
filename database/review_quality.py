"""
Quality Check Script - Review Content Across All Categories
"""

from database.connection import get_session
from database.models import Book, Summary, Genre
import json

def review_content_quality():
    db = get_session()
    
    print("=" * 80)
    print("📊 CONTENT QUALITY REVIEW")
    print("=" * 80)
    print()
    
    # Get all genres
    genres = db.query(Genre).all()
    
    for genre in genres:
        books = db.query(Book).filter(Book.genre_id == genre.id).limit(3).all()
        
        if not books:
            continue
            
        print(f"\n{'='*80}")
        print(f"🎯 {genre.icon} {genre.name.upper()} - Reviewing {len(books)} sample books")
        print(f"{'='*80}")
        
        for i, book in enumerate(books, 1):
            summary = db.query(Summary).filter(Summary.book_id == book.id).first()
            
            if not summary:
                print(f"   ⚠️  {book.title} - NO SUMMARY FOUND")
                continue
            
            print(f"\n{i}. 📚 {book.title}")
            print(f"   Author: {book.author}")
            print(f"   Year: {book.publication_year}")
            print(f"   Rating: {summary.rating}/5 ⭐")
            print(f"   Reading Time: {summary.reading_time} min")
            
            # Content quality checks
            takeaways = json.loads(summary.key_takeaways) if summary.key_takeaways else []
            quotes = json.loads(summary.quotes) if summary.quotes else []
            actions = json.loads(summary.action_steps) if summary.action_steps else []
            analogies = json.loads(summary.analogies) if summary.analogies else []
            
            print(f"\n   📋 Content Quality:")
            print(f"      ✅ Executive Summary: {len(summary.executive_summary)} chars")
            print(f"      ✅ Framework: {summary.main_content[:50]}...")
            print(f"      ✅ Takeaways: {len(takeaways)} detailed points")
            print(f"      ✅ Quotes: {len(quotes)} inspiring quotes")
            print(f"      ✅ Action Steps: {len(actions)} practical actions")
            print(f"      ✅ Analogies: {len(analogies)} explanatory analogies")
            print(f"      ✅ Visual Map: {'Yes - Custom Graphviz' if summary.workflow_data else 'No'}")
            
            # Show first quote as sample
            if quotes:
                print(f"\n   💬 Sample Quote:")
                print(f'      "{quotes[0][:120]}{"..." if len(quotes[0]) > 120 else ""}"')
            
            # Show first takeaway as sample
            if takeaways:
                print(f"\n   🎯 Sample Takeaway:")
                print(f"      Title: {takeaways[0].get('title', 'N/A')}")
                print(f"      Text: {takeaways[0].get('text', 'N/A')[:100]}...")
    
    # Summary statistics
    print(f"\n\n{'='*80}")
    print("📊 OVERALL STATISTICS")
    print(f"{'='*80}")
    
    total_books = db.query(Book).count()
    total_summaries = db.query(Summary).count()
    
    print(f"Total Books: {total_books}")
    print(f"Total Summaries: {total_summaries}")
    print(f"Coverage: {(total_summaries/total_books*100):.1f}%")
    
    # Genre breakdown
    print(f"\n📚 Books per Genre:")
    for genre in genres:
        count = db.query(Book).filter(Book.genre_id == genre.id).count()
        print(f"   {genre.icon} {genre.name:15s}: {count:4d} books")
    
    # Quality metrics
    print(f"\n✅ Quality Checks:")
    books_with_visual = db.query(Summary).filter(Summary.workflow_data != None, Summary.workflow_data != '').count()
    books_with_quotes = db.query(Summary).filter(Summary.quotes != None, Summary.quotes != '').count()
    books_with_actions = db.query(Summary).filter(Summary.action_steps != None, Summary.action_steps != '').count()
    
    print(f"   Visual Maps: {books_with_visual}/{total_books} ({books_with_visual/total_books*100:.1f}%)")
    print(f"   Quotes: {books_with_quotes}/{total_books} ({books_with_quotes/total_books*100:.1f}%)")
    print(f"   Action Steps: {books_with_actions}/{total_books} ({books_with_actions/total_books*100:.1f}%)")
    
    print(f"\n{'='*80}")
    print("✅ REVIEW COMPLETE")
    print(f"{'='*80}\n")
    
    db.close()

if __name__ == "__main__":
    review_content_quality()
