"""
Expert Seed Script - Complete 100 Books
Merges all book databases
"""

from database.connection import get_session, engine
from database.models import Base, Genre, Book, Summary
from database.book_database import BOOK_DATABASE
from database.book_database_selfhelp import SELFHELP_BOOKS
from database.book_database_batch2 import BOOKS_BATCH_2
from database.book_database_batch3 import BOOKS_BATCH_3_100
from database.book_database_final import BOOKS_FINAL_BATCH
from database.book_database_complete import FINAL_40_BOOKS
from database.book_database_last import LAST_9_BOOKS
from database.book_database_selfhelp_100 import SELFHELP_100_MORE
from database.book_database_all_genres_100 import GENRE_100_BOOKS
import json

# Merge ALL book databases
ALL_BOOKS = {
    **BOOK_DATABASE,
    **SELFHELP_BOOKS,
    **BOOKS_BATCH_2,
    **BOOKS_BATCH_3_100,
    **BOOKS_FINAL_BATCH,
    **FINAL_40_BOOKS,
    **LAST_9_BOOKS,
    **SELFHELP_100_MORE,
    **GENRE_100_BOOKS
}

print(f"📚 Total books to seed: {len(ALL_BOOKS)}")

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def seed_expert_library():
    db = get_session()
    
    print("🌱 Seeding Genres...")
    genres = [
        Genre(name="Self-Help", slug="self-help", icon="🌱", description="Personal growth and transformation."),
        Genre(name="Business", slug="business", icon="💼", description="Strategy, leadership, and entrepreneurship."),
        Genre(name="Psychology", slug="psychology", icon="🧠", description="Understanding mind and behavior."),
        Genre(name="Finance", slug="finance", icon="💰", description="Money management and wealth building."),
        Genre(name="Productivity", slug="productivity", icon="⚡", description="Time management and focus."),
        Genre(name="Philosophy", slug="philosophy", icon="🤔", description="Timeless wisdom and principles."),
        Genre(name="History", slug="history", icon="🏺", description="The story of civilization."),
        Genre(name="Science", slug="science", icon="🔬", description="Discovery and understanding."),
        Genre(name="Biography", slug="biography", icon="👤", description="Remarkable lives and stories."),
        Genre(name="Technology", slug="technology", icon="💻", description="Innovation and the future."),
    ]
    db.add_all(genres)
    db.commit()
    genre_map = {g.slug: g for g in genres}
    
    print(f"📖 Seeding {len(ALL_BOOKS)} Expert-Curated Books...")
    print()
    
    book_count = 0
    for title, data in ALL_BOOKS.items():
        book_count += 1
        print(f"   {book_count}. {title} ({data['author']})")
        
        book = Book(
            title=title,
            author=data['author'],
            slug=title.lower().replace(" ", "-").replace(":", "").replace("'", "").replace(",", "").replace("*", "").replace("(", "").replace(")", ""),
            cover_image_url=data['cover'],
            publication_year=data['year'],
            genre=genre_map[data['genre']],
            is_featured=book_count <= 20  # First 20 are featured
        )
        db.add(book)
        db.commit()
        
        summary = Summary(
            book_id=book.id,
            overview_text=data['overview'],
            executive_summary=data['executive'],
            quote_of_the_book=data['quotes'][0],
            main_content=f"Framework: {data['framework']}",
            key_takeaways=json.dumps(data['takeaways']),
            who_should_read=f"Perfect for readers interested in {data['genre']}, personal development, and mastering the {data['framework']} framework.",
            reading_time=data['time'],
            rating=data['rating'],
            difficulty="Intermediate",
            seo_title=f"{title} Summary - {data['framework']} | BookWise",
            seo_description=f"Expert summary of {title} by {data['author']}. Master the {data['framework']} framework with key takeaways, quotes, and action steps.",
            action_steps=json.dumps(data['actions']),
            quotes=json.dumps(data['quotes']),
            analogies=json.dumps(data['analogies']),
            workflow_data=data['visual_map']
        )
        db.add(summary)
        db.commit()
    
    print()
    print("="*60)
    print(f"✅ Successfully seeded {len(ALL_BOOKS)} expert-curated books!")
    print("="*60)
    print()
    print("📊 Library Summary by Genre:")
    genre_counts = {}
    for book_data in ALL_BOOKS.values():
        genre = book_data['genre']
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    
    for genre, count in sorted(genre_counts.items(), key=lambda x: -x[1]):
        print(f"   {genre.capitalize():15s}: {count:2d} books")
    
    print()
    print("🎯 Featured Books: First 20")
    print("💡 Each book includes:")
    print("   • Actual book-specific framework")
    print("   • 5+ detailed takeaways")
    print("   • Real quotes")
    print("   • 5 action steps")
    print("   • Analogies")
    print("   • Custom visual map")
    print()
    
    db.close()

if __name__ == "__main__":
    seed_expert_library()
