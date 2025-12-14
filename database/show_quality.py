"""
Simple Quality Check - Display Top Books
"""
from database.connection import get_session
from database.models import Book, Summary
import json

db = get_session()

# Get a high-quality book
book = db.query(Book).filter(Book.title == "Atomic Habits").first()
if book:
    summary = db.query(Summary).filter(Summary.book_id == book.id).first()
    
    print("=" * 80)
    print("SAMPLE QUALITY CHECK: ATOMIC HABITS")
    print("=" * 80)
    print(f"\nAuthor: {book.author}")
    print(f"Year: {book.publication_year}")
    print(f"Rating: {summary.rating}/5 ⭐")
    print(f"Reading Time: {summary.reading_time} minutes")
    
    print(f"\n{'='*80}")
    print("EXECUTIVE SUMMARY:")
    print(f"{'='*80}")
    print(summary.executive_summary)
    
    takeaways = json.loads(summary.key_takeaways)
    print(f"\n{'='*80}")
    print(f"KEY TAKEAWAYS ({len(takeaways)}):")
    print(f"{'='*80}")
    for i, ta in enumerate(takeaways, 1):
        print(f"\n{i}. {ta['title']}")
        print(f"   {ta['text']}")
    
    quotes = json.loads(summary.quotes)
    print(f"\n{'='*80}")
    print(f"QUOTES ({len(quotes)}):")
    print(f"{'='*80}")
    for quote in quotes:
        print(f'   • "{quote}"')
    
    actions = json.loads(summary.action_steps)
    print(f"\n{'='*80}")
    print(f"ACTION STEPS ({len(actions)}):")
    print(f"{'='*80}")
    for i, action in enumerate(actions, 1):
        print(f"   {i}. {action}")
    
    analogies = json.loads(summary.analogies)
    print(f"\n{'='*80}")
    print(f"ANALOGIES ({len(analogies)}):")
    print(f"{'='*80}")
    for analogy in analogies:
        print(f"\n   Concept: {analogy['concept']}")
        print(f"   Analogy: {analogy['analogy']}")
        print(f"   Explanation: {analogy['explanation']}")
    
    print(f"\n{'='*80}")
    print(f"VISUAL MAP:")
    print(f"{'='*80}")
    if summary.workflow_data:
        print("✅ YES - Custom Graphviz diagram included")
        print(summary.workflow_data[:200] + "...")
    else:
        print("❌ NO")
    
    print(f"\n{'='*80}")

db.close()
