"""
Seed 100 World-Class Books - Comprehensive Library
This expands the database with top books across all genres.
"""

from sqlalchemy.orm import Session
from database.connection import get_session, engine
from database.models import Base, Genre, Book, Summary, SummaryImage
import json

# Drop and recreate tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def seed_100_books():
    db = get_session()
    
    print("🌱 Seeding Genres...")
    genres = [
        Genre(name="Self-Help", slug="self-help", icon="🌱", description="Personal growth and improvement."),
        Genre(name="Business", slug="business", icon="💼", description="Strategy, leadership, entrepreneurship."),
        Genre(name="Psychology", slug="psychology", icon="🧠", description="Understanding mind and behavior."),
        Genre(name="Finance", slug="finance", icon="💰", description="Money management and investing."),
        Genre(name="Productivity", slug="productivity", icon="⚡", description="Time management and optimization."),
        Genre(name="Philosophy", slug="philosophy", icon="🤔", description="Timeless wisdom and thinking."),
        Genre(name="History", slug="history", icon="🏺", description="The story of civilization."),
        Genre(name="Science", slug="science", icon="🔬", description="Discovery and understanding."),
        Genre(name="Biography", slug="biography", icon="👤", description="Remarkable lives and stories."),
        Genre(name="Technology", slug="technology", icon="💻", description="Innovation and the future."),
    ]
    db.add_all(genres)
    db.commit()
    
    genre_map = {g.slug: g for g in genres}
    
    print("📚 Seeding 100 Top Books...")
    
    def create_book(title, author, genre_slug, cover_url, year, summary_data):
        book = Book(
            title=title,
            author=author,
            slug=title.lower().replace(" ", "-").replace(":", "").replace("'", "").replace(",", ""),
            cover_image_url=cover_url,
            publication_year=year,
            genre=genre_map[genre_slug],
            is_featured=summary_data.get('featured', True)
        )
        db.add(book)
        db.commit()
        
        summary = Summary(
            book_id=book.id,
            overview_text=summary_data.get('overview', 'A transformative book.'),
            executive_summary=summary_data.get('executive', summary_data.get('overview', 'Coming soon.')),
            quote_of_the_book=summary_data.get('quote', 'A great book changes your life.'),
            main_content=summary_data.get('ideas', 'Key concepts...'),
            key_takeaways=json.dumps(summary_data.get('takeaways', [])),
            who_should_read=summary_data.get('audience', 'Everyone seeking growth.'),
            reading_time=summary_data.get('time', 15),
            rating=summary_data.get('rating', 4.5),
            difficulty="Beginner",
            seo_title=f"{title} - Summary & Key Insights",
            seo_description=f"Comprehensive summary of {title} by {author}",
            workflow_data=summary_data.get('diagram', None),
            analogies=json.dumps(summary_data.get('analogies', [])),
            quotes=json.dumps(summary_data.get('quotes', [])),
            action_steps=json.dumps(summary_data.get('actions', []))
        )
        db.add(summary)
        db.commit()
    
    # ========== SELF-HELP (15 books) ==========
    books_self_help = [
        ("Atomic Habits", "James Clear", 2018, "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg"),
        ("The 7 Habits of Highly Effective People", "Stephen Covey", 1989, "https://images-na.ssl-images-amazon.com/images/I/51S35oQ+yzL.jpg"),
        ("How to Win Friends and Influence People", "Dale Carnegie", 1936, "https://images-na.ssl-images-amazon.com/images/I/71vK0WVQ4rL.jpg"),
        ("The Power of Now", "Eckhart Tolle", 1997, "https://images-na.ssl-images-amazon.com/images/I/71QY6z2gcVL.jpg"),
        ("Man's Search for Meaning", "Viktor Frankl", 1946, "https://images-na.ssl-images-amazon.com/images/I/41s5a2YLjVL.jpg"),
        ("The Subtle Art of Not Giving a F*ck", "Mark Manson", 2016, "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg"),
        ("Mindset", "Carol Dweck", 2006, "https://images-na.ssl-images-amazon.com/images/I/71KvP+sDKZL.jpg"),
        ("Grit", "Angela Duckworth", 2016, "https://images-na.ssl-images-amazon.com/images/I/71S0WHJL5OL.jpg"),
        ("Can't Hurt Me", "David Goggins", 2018, "https://images-na.ssl-images-amazon.com/images/I/81V4nVuaAuL.jpg"),
        ("The Miracle Morning", "Hal Elrod", 2012, "https://images-na.ssl-images-amazon.com/images/I/71WEDjM-a4L.jpg"),
        ("The Alchemist", "Paulo Coelho", 1988, "https://images-na.ssl-images-amazon.com/images/I/71aFt4+OTOL.jpg"),
        ("Daring Greatly", "Brené Brown", 2012, "https://images-na.ssl-images-amazon.com/images/I/41moZ27w3NL.jpg"),
        ("The Four Agreements", "Don Miguel Ruiz", 1997, "https://images-na.ssl-images-amazon.com/images/I/713XcD+CbxL.jpg"),
        ("Awaken the Giant Within", "Tony Robbins", 1991, "https://images-na.ssl-images-amazon.com/images/I/51+b8v0R21L.jpg"),
        ("You Are a Badass", "Jen Sincero", 2013, "https://images-na.ssl-images-amazon.com/images/I/71Jqn4C2B6L.jpg"),
    ]
    
    for title, author, year, cover in books_self_help:
        create_book(title, author, "self-help", cover, year, {
            "rating": 4.6,
            "time": 12,
            "quote": "Personal growth is a lifelong journey.",
            "overview": f"A powerful guide to personal transformation and growth.",
            "executive": f"{title} offers practical strategies for improving your life through consistent action and mindset shifts.",
            "ideas": "Core concepts about personal development, habit formation, and mindset mastery.",
            "takeaways": [
                {"title": "Take Action Daily", "text": "Small consistent actions lead to massive results."},
                {"title": "Master Your Mind", "text": "Your thoughts shape your reality."},
            ],
            "quotes": [
                "You have the power to change your life.",
                "Growth happens outside your comfort zone.",
            ],
            "actions": [
                "Set one clear goal for this month",
                "Create a morning routine",
                "Read for 30 minutes daily"
            ],
            "audience": "Anyone seeking personal growth and transformation."
        })
    
    # ========== BUSINESS (15 books) ==========
    books_business = [
        ("Good to Great", "Jim Collins", 2001, "https://images-na.ssl-images-amazon.com/images/I/81CKiGbWiyL.jpg"),
        ("The Lean Startup", "Eric Ries", 2011, "https://images-na.ssl-images-amazon.com/images/I/81-QB7nDh4L.jpg"),
        ("Zero to One", "Peter Thiel", 2014, "https://images-na.ssl-images-amazon.com/images/I/71Cd+6WubOL.jpg"),
        ("The E-Myth Revisited", "Michael Gerber", 1995, "https://images-na.ssl-images-amazon.com/images/I/71jGiT5l2TL.jpg"),
        ("Start with Why", "Simon Sinek", 2009, "https://images-na.ssl-images-amazon.com/images/I/71g3kdmWfOL.jpg"),
        ("The Hard Thing About Hard Things", "Ben Horowitz", 2014, "https://images-na.ssl-images-amazon.com/images/I/71iQKpvNbOL.jpg"),
        ("Built to Last", "Jim Collins", 1994, "https://images-na.ssl-images-amazon.com/images/I/71+7LdKlGgL.jpg"),
        ("The Innovator's Dilemma", "Clayton Christensen", 1997, "https://images-na.ssl-images-amazon.com/images/I/71tZ3i8n5vL.jpg"),
        ("Shoe Dog", "Phil Knight", 2016, "https://images-na.ssl-images-amazon.com/images/I/81Ly03JMgHL.jpg"),
        ("The $100 Startup", "Chris Guillebeau", 2012, "https://images-na.ssl-images-amazon.com/images/I/71Zi1GCy8-L.jpg"),
        ("Rework", "Jason Fried", 2010, "https://images-na.ssl-images-amazon.com/images/I/51azU9t3QDL.jpg"),
        ("Traction", "Gino Wickman", 2011, "https://images-na.ssl-images-amazon.com/images/I/71nMLyp6OhL.jpg"),
        ("Blue Ocean Strategy", "W. Chan Kim", 2005, "https://images-na.ssl-images-amazon.com/images/I/61sGQVJJKdL.jpg"),
        ("The 22 Immutable Laws of Marketing", "Al Ries", 1993, "https://images-na.ssl-images-amazon.com/images/I/71T-sRdtw5L.jpg"),
        ("Crossing the Chasm", "Geoffrey Moore", 1991, "https://images-na.ssl-images-amazon.com/images/I/71BW8D3Vz8L.jpg"),
    ]
    
    for title, author, year, cover in books_business:
        create_book(title, author, "business", cover, year, {
            "rating": 4.5,
            "time": 14,
            "quote": "Build something people want.",
            "overview": "Essential strategies for building and scaling successful businesses.",
            "executive": f"{title} reveals proven frameworks for entrepreneurial success and business growth.",
            "ideas": "Leadership principles, startup strategies, and competitive advantage.",
            "takeaways": [
                {"title": "Focus on Value", "text": "Create exceptional value for customers."},
                {"title": "Build Systems", "text": "Systematic processes enable scalability."},
            ],
            "quotes": [
                "Innovation distinguishes between a leader and a follower.",
                "Your customers don't care about you. They care about themselves.",
            ],
            "actions": [
                "Define your unique value proposition",
                "Talk to 10 customers this week",
                "Build a minimum viable product"
            ],
            "audience": "Entrepreneurs, business leaders, and aspiring founders."
        })
    
    # ========== PSYCHOLOGY (10 books) ==========
    books_psychology = [
        ("Thinking, Fast and Slow", "Daniel Kahneman", 2011, "https://images-na.ssl-images-amazon.com/images/I/71T2xDpVqKL.jpg"),
        ("Influence", "Robert Cialdini", 1984, "https://images-na.ssl-images-amazon.com/images/I/717VWXyNhJL.jpg"),
        ("The Power of Habit", "Charles Duhigg", 2012, "https://images-na.ssl-images-amazon.com/images/I/81F90H7hnML.jpg"),
        ("Flow", "Mihaly Csikszentmihalyi", 1990, "https://images-na.ssl-images-amazon.com/images/I/71mNAhMOUOL.jpg"),
        ("Predictably Irrational", "Dan Ariely", 2008, "https://images-na.ssl-images-amazon.com/images/I/71V+hfJ7tHL.jpg"),
        ("Emotional Intelligence", "Daniel Goleman", 1995, "https://images-na.ssl-images-amazon.com/images/I/71HZyYT+PEL.jpg"),
        ("Quiet", "Susan Cain", 2012, "https://images-na.ssl-images-amazon.com/images/I/71TIiKTkPVL.jpg"),
        ("The Body Keeps the Score", "Bessel van der Kolk", 2014, "https://images-na.ssl-images-amazon.com/images/I/71HZV5V2IKL.jpg"),
        ("Man and His Symbols", "Carl Jung", 1964, "https://images-na.ssl-images-amazon.com/images/I/716yqJCkHlL.jpg"),
        ("Drive", "Daniel Pink", 2009, "https://images-na.ssl-images-amazon.com/images/I/71MWIbVaDzL.jpg"),
    ]
    
    for title, author, year, cover in books_psychology:
        create_book(title, author, "psychology", cover, year, {
            "rating": 4.7,
            "time": 16,
            "quote": "Understanding the mind unlocks human potential.",
            "overview": "Deep insights into human behavior, cognition, and decision-making.",
            "executive": f"{title} explores the fascinating science of how we think, feel, and behave.",
            "ideas": "Cognitive biases, emotional intelligence, and behavioral patterns.",
            "takeaways": [
                {"title": "Know Your Biases", "text": "Awareness of biases improves decisions."},
                {"title": "Emotions Matter", "text": "EQ is as important as IQ."},
            ],
            "quotes": [
                "The mind is everything. What you think you become.",
                "We are what we repeatedly do.",
            ],
            "actions": [
                "Journal your thoughts daily",
                "Practice mindfulness meditation",
                "Study cognitive biases"
            ],
            "audience": "Anyone curious about the human mind and behavior."
        })
    
    # ========== FINANCE (10 books) ==========
    books_finance = [
        ("The Psychology of Money", "Morgan Housel", 2020, "https://images-na.ssl-images-amazon.com/images/I/715k1M+oWLL.jpg"),
        ("Rich Dad Poor Dad", "Robert Kiyosaki", 1997, "https://images-na.ssl-images-amazon.com/images/I/81bsw6fnUiL.jpg"),
        ("The Intelligent Investor", "Benjamin Graham", 1949, "https://images-na.ssl-images-amazon.com/images/I/71L5Yec4dEL.jpg"),
        ("Think and Grow Rich", "Napoleon Hill", 1937, "https://images-na.ssl-images-amazon.com/images/I/71UypkUjStL.jpg"),
        ("The Millionaire Next Door", "Thomas Stanley", 1996, "https://images-na.ssl-images-amazon.com/images/I/71W+xXb4l6L.jpg"),
        ("A Random Walk Down Wall Street", "Burton Malkiel", 1973, "https://images-na.ssl-images-amazon.com/images/I/71aG0m9XhcL.jpg"),
        ("The Little Book of Common Sense Investing", "John Bogle", 2007, "https://images-na.ssl-images-amazon.com/images/I/71N9LjknPPL.jpg"),
        ("I Will Teach You to Be Rich", "Ramit Sethi", 2009, "https://images-na.ssl-images-amazon.com/images/I/71OZc5YnHhL.jpg"),
        ("Your Money or Your Life", "Vicki Robin", 1992, "https://images-na.ssl-images-amazon.com/images/I/71+7q+sY9tL.jpg"),
        ("The Total Money Makeover", "Dave Ramsey", 2003, "https://images-na.ssl-images-amazon.com/images/I/71U1xCdgHqL.jpg"),
    ]
    
    for title, author, year, cover in books_finance:
        create_book(title, author, "finance", cover, year, {
            "rating": 4.6,
            "time": 13,
            "quote": "Wealth is built slowly and steadily.",
            "overview": "Timeless principles for building and preserving wealth.",
            "executive": f"{title} teaches proven strategies for financial independence and smart money management.",
            "ideas": "Investing fundamentals, wealth mindset, and financial freedom.",
            "takeaways": [
                {"title": "Live Below Your Means", "text": "Spend less than you earn consistently."},
                {"title": "Invest for the Long Term", "text": "Time in the market beats timing the market."},
            ],
            "quotes": [
                "The best investment you can make is in yourself.",
                "Compound interest is the eighth wonder of the world.",
            ],
            "actions": [
                "Create a monthly budget",
                "Start investing 15% of income",
                "Build a 6-month emergency fund"
            ],
            "audience": "Anyone seeking financial security and wealth building."
        })
    
    # ========== PRODUCTIVITY (10 books) ==========
    books_productivity = [
        ("Deep Work", "Cal Newport", 2016, "https://images-na.ssl-images-amazon.com/images/I/71e9MYTEOTL.jpg"),
        ("Getting Things Done", "David Allen", 2001, "https://images-na.ssl-images-amazon.com/images/I/71V26Csy8XL.jpg"),
        ("The 4-Hour Workweek", "Tim Ferriss", 2007, "https://images-na.ssl-images-amazon.com/images/I/81qw+3UUFfL.jpg"),
        ("Essentialism", "Greg McKeown", 2014, "https://images-na.ssl-images-amazon.com/images/I/71SgVLiP-OL.jpg"),
        ("The One Thing", "Gary Keller", 2013, "https://images-na.ssl-images-amazon.com/images/I/71V3lkJs3WL.jpg"),
        ("Eat That Frog", "Brian Tracy", 2001, "https://images-na.ssl-images-amazon.com/images/I/71XUj4MlXZL.jpg"),
        ("The Productivity Project", "Chris Bailey", 2016, "https://images-na.ssl-images-amazon.com/images/I/71zE6BXvOYL.jpg"),
        ("Make Time", "Jake Knapp", 2018, "https://images-na.ssl-images-amazon.com/images/I/71qMfXsJP7L.jpg"),
        ("Indistractable", "Nir Eyal", 2019, "https://images-na.ssl-images-amazon.com/images/I/71V7YFJ8YwL.jpg"),
        ("Hyperfocus", "Chris Bailey", 2018, "https://images-na.ssl-images-amazon.com/images/I/71OB13IG9wL.jpg"),
    ]
    
    for title, author, year, cover in books_productivity:
        create_book(title, author, "productivity", cover, year, {
            "rating": 4.5,
            "time": 11,
            "quote": "Focus on what matters most.",
            "overview": "Master your time and accomplish more with less effort.",
            "executive": f"{title} provides battle-tested systems for maximizing productivity and focus.",
            "ideas": "Time management, prioritization, and eliminating distractions.",
            "takeaways": [
                {"title": "Do Less, Better", "text": "Quality over quantity in everything."},
                {"title": "Protect Your Time", "text": "Say no to protect your priorities."},
            ],
            "quotes": [
                "You can do anything, but not everything.",
                "The key is not to prioritize what's on your schedule, but to schedule your priorities.",
            ],
            "actions": [
                "Identify your One Thing for today",
                "Block 2 hours for deep work",
                "Eliminate one distraction"
            ],
            "audience": "Knowledge workers, students, and busy professionals."
        })
    
    # ========== PHILOSOPHY (10 books) ==========
    books_philosophy = [
        ("Meditations", "Marcus Aurelius", 180, "https://images-na.ssl-images-amazon.com/images/I/71HWqZ7fFfL.jpg"),
        ("The Daily Stoic", "Ryan Holiday", 2016, "https://images-na.ssl-images-amazon.com/images/I/71YtaCsGWsL.jpg"),
        ("Ego Is the Enemy", "Ryan Holiday", 2016, "https://images-na.ssl-images-amazon.com/images/I/71KPbM0K6hL.jpg"),
        ("Letters from a Stoic", "Seneca", 65, "https://images-na.ssl-images-amazon.com/images/I/71Vo5EL6i0L.jpg"),
        ("The Obstacle Is the Way", "Ryan Holiday", 2014, "https://images-na.ssl-images-amazon.com/images/I/71GE31lDirL.jpg"),
        ("Thus Spoke Zarathustra", "Friedrich Nietzsche", 1883, "https://images-na.ssl-images-amazon.com/images/I/71HGSi3+7HL.jpg"),
        ("The Republic", "Plato", -380, "https://images-na.ssl-images-amazon.com/images/I/71L1z+rXLKL.jpg"),
        ("The Art of War", "Sun Tzu", -500, "https://images-na.ssl-images-amazon.com/images/I/71V0wrvuOQL.jpg"),
        ("Beyond Good and Evil", "Friedrich Nietzsche", 1886, "https://images-na.ssl-images-amazon.com/images/I/71HGdP6RxyL.jpg"),
        ("The Tao Te Ching", "Lao Tzu", -400, "https://images-na.ssl-images-amazon.com/images/I/71zRuuDwGgL.jpg"),
    ]
    
    for title, author, year, cover in books_philosophy:
        create_book(title, author, "philosophy", cover, year, {
            "rating": 4.8,
            "time": 14,
            "quote": "The unexamined life is not worth living.",
            "overview": "Timeless wisdom for living a meaningful life.",
            "executive": f"{title} offers profound insights into human nature, virtue, and the good life.",
            "ideas": "Stoicism, ethics, virtue, and the art of living.",
            "takeaways": [
                {"title": "Control What You Can", "text": "Focus only on what's within your control."},
                {"title": "Live with Virtue", "text": "Character is the ultimate wealth."},
            ],
            "quotes": [
                "The impediment to action advances action. What stands in the way becomes the way.",
                "He who has a why to live can bear almost any how.",
            ],
            "actions": [
                "Practice negative visualization",
                "Read philosophy for 10 minutes daily",
                "Reflect on your values"
            ],
            "audience": "Thinkers, seekers, and anyone pursuing wisdom."
        })
    
    # ========== HISTORY (10 books) ==========
    books_history = [
        ("Sapiens", "Yuval Noah Harari", 2011, "https://images-na.ssl-images-amazon.com/images/I/71S1TKI0vkL.jpg"),
        ("Homo Deus", "Yuval Noah Harari", 2015, "https://images-na.ssl-images-amazon.com/images/I/71VuMy9lCXL.jpg"),
        ("Guns, Germs, and Steel", "Jared Diamond", 1997, "https://images-na.ssl-images-amazon.com/images/I/71G+Inh2S9L.jpg"),
        ("The Silk Roads", "Peter Frankopan", 2015, "https://images-na.ssl-images-amazon.com/images/I/71hzPvP5PXL.jpg"),
        ("1984", "George Orwell", 1949, "https://images-na.ssl-images-amazon.com/images/I/71kT5xrYoVL.jpg"),
        ("A Short History of Nearly Everything", "Bill Bryson", 2003, "https://images-na.ssl-images-amazon.com/images/I/71Q7rSmN2oL.jpg"),
        ("The Lessons of History", "Will Durant", 1968, "https://images-na.ssl-images-amazon.com/images/I/71V0XoAYDNL.jpg"),
        ("SPQR", "Mary Beard", 2015, "https://images-na.ssl-images-amazon.com/images/I/71L-UkjQ+fL.jpg"),
        ("The Wright Brothers", "David McCullough", 2015, "https://images-na.ssl-images-amazon.com/images/I/71xXUCjZ2jL.jpg"),
        ("Team of Rivals", "Doris Kearns Goodwin", 2005, "https://images-na.ssl-images-amazon.com/images/I/71Rd8NZwBGL.jpg"),
    ]
    
    for title, author, year, cover in books_history:
        create_book(title, author, "history", cover, year, {
            "rating": 4.7,
            "time": 18,
            "quote": "Those who cannot remember the past are condemned to repeat it.",
            "overview": "Learn from humanity's triumphs and failures.",
            "executive": f"{title} chronicles the forces that shaped our world and continue to influence our future.",
            "ideas": "Civilizations, revolutions, and the patterns of history.",
            "takeaways": [
                {"title": "History Repeats", "text": "Patterns emerge across civilizations."},
                {"title": "Progress is Fragile", "text": "Civilization requires constant effort."},
            ],
            "quotes": [
                "History is a set of lies agreed upon.",
                "The further backward you look, the further forward you can see.",
            ],
            "actions": [
                "Study one historical period deeply",
                "Visit a historical museum",
                "Read primary sources"
            ],
            "audience": "History enthusiasts and curious minds."
        })
    
    # ========== SCIENCE (10 books) ==========
    books_science = [
        ("A Brief History of Time", "Stephen Hawking", 1988, "https://images-na.ssl-images-amazon.com/images/I/81V3OqfCrqL.jpg"),
        ("The Selfish Gene", "Richard Dawkins", 1976, "https://images-na.ssl-images-amazon.com/images/I/71V8QjXxe0L.jpg"),
        ("Cosmos", "Carl Sagan", 1980, "https://images-na.ssl-images-amazon.com/images/I/91PcYSH7duL.jpg"),
        ("The Origin of Species", "Charles Darwin", 1859, "https://images-na.ssl-images-amazon.com/images/I/71WHj5tVikL.jpg"),
        ("Astrophysics for People in a Hurry", "Neil deGrasse Tyson", 2017, "https://images-na.ssl-images-amazon.com/images/I/71VHSHzfQNL.jpg"),
        ("The Double Helix", "James Watson", 1968, "https://images-na.ssl-images-amazon.com/images/I/71G+c-uNNvL.jpg"),
        ("The Gene", "Siddhartha Mukherjee", 2016, "https://images-na.ssl-images-amazon.com/images/I/71Ct5y6VXQL.jpg"),
        ("Why We Sleep", "Matthew Walker", 2017, "https://images-na.ssl-images-amazon.com/images/I/71TT-hXO3gL.jpg"),
        ("Behave", "Robert Sapolsky", 2017, "https://images-na.ssl-images-amazon.com/images/I/71P2cjx-SuL.jpg"),
        ("The Emperor of All Maladies", "Siddhartha Mukherjee", 2010, "https://images-na.ssl-images-amazon.com/images/I/71VcxfAgRLL.jpg"),
    ]
    
    for title, author, year, cover in books_science:
        create_book(title, author, "science", cover, year, {
            "rating": 4.6,
            "time": 16,
            "quote": "Science is a way of thinking much more than it is a body of knowledge.",
            "overview": "Explore the wonders of the natural world and universe.",
            "executive": f"{title} makes complex scientific concepts accessible and fascinating.",
            "ideas": "Evolution, cosmos, genetics, and scientific discovery.",
            "takeaways": [
                {"title": "Question Everything", "text": "Scientific thinking requires skepticism."},
                {"title": "We're Still Learning", "text": "Science evolves with new evidence."},
            ],
            "quotes": [
                "The cosmos is within us. We are made of star-stuff.",
                "Nothing in biology makes sense except in the light of evolution.",
            ],
            "actions": [
                "Watch a science documentary",
                "Conduct a simple experiment",
                "Read one scientific paper"
            ],
            "audience": "Science enthusiasts and curious learners."
        })
    
    # ========== BIOGRAPHY (10 books) ==========
    books_biography = [
        ("Steve Jobs", "Walter Isaacson", 2011, "https://images-na.ssl-images-amazon.com/images/I/81VkhAAzJPL.jpg"),
        ("Einstein", "Walter Isaacson", 2007, "https://images-na.ssl-images-amazon.com/images/I/81F6RdHcmJL.jpg"),
        ("Benjamin Franklin", "Walter Isaacson", 2003, "https://images-na.ssl-images-amazon.com/images/I/71OIeV8OEPL.jpg"),
        ("Leonardo da Vinci", "Walter Isaacson", 2017, "https://images-na.ssl-images-amazon.com/images/I/71-++HKgXKL.jpg"),
        ("Elon Musk", "Ashlee Vance", 2015, "https://images-na.ssl-images-amazon.com/images/I/71jG+e7roXL.jpg"),
        ("The Autobiography of Malcolm X", "Malcolm X", 1965, "https://images-na.ssl-images-amazon.com/images/I/71Vz6bw6i-L.jpg"),
        ("Long Walk to Freedom", "Nelson Mandela", 1994, "https://images-na.ssl-images-amazon.com/images/I/71WnoSMB+OL.jpg"),
        ("Becoming", "Michelle Obama", 2018, "https://images-na.ssl-images-amazon.com/images/I/81Pu02CPk0L.jpg"),
        ("Into the Wild", "Jon Krakauer", 1996, "https://images-na.ssl-images-amazon.com/images/I/71sXhJJAteL.jpg"),
        ("The Diary of a Young Girl", "Anne Frank", 1947, "https://images-na.ssl-images-amazon.com/images/I/81qYJCnJsyL.jpg"),
    ]
    
    for title, author, year, cover in books_biography:
        create_book(title, author, "biography", cover, year, {
            "rating": 4.7,
            "time": 17,
            "quote": "Lives lived boldly inspire us to do the same.",
            "overview": "Learn from the lives of remarkable individuals.",
            "executive": f"{title} reveals the struggles, triumphs, and lessons from an extraordinary life.",
            "ideas": "Leadership, resilience, creativity, and human potential.",
            "takeaways": [
                {"title": "Persistence Wins", "text": "Great achievements require relentless effort."},
                {"title": "Learn from Failure", "text": "Setbacks are stepping stones."},
            ],
            "quotes": [
                "The only way to do great work is to love what you do.",
                "Innovation distinguishes between a leader and a follower.",
            ],
            "actions": [
                "Study one leader's life deeply",
                "Identify their key principles",
                "Apply one lesson to your life"
            ],
            "audience": "Anyone inspired by remarkable lives."
        })
    
    # ========== TECHNOLOGY (10 books) ==========
    books_technology = [
        ("The Innovators", "Walter Isaacson", 2014, "https://images-na.ssl-images-amazon.com/images/I/71aLgZM+E8L.jpg"),
        ("The Everything Store", "Brad Stone", 2013, "https://images-na.ssl-images-amazon.com/images/I/71p7nqvvpkL.jpg"),
        ("The Master Switch", "Tim Wu", 2010, "https://images-na.ssl-images-amazon.com/images/I/71NXlblC3vL.jpg"),
        ("The Second Machine Age", "Erik Brynjolfsson", 2014, "https://images-na.ssl-images-amazon.com/images/I/71AoHrYmvRL.jpg"),
        ("Hackers & Painters", "Paul Graham", 2004, "https://images-na.ssl-images-amazon.com/images/I/71UpZ+aVL7L.jpg"),
        ("The Shallows", "Nicholas Carr", 2010, "https://images-na.ssl-images-amazon.com/images/I/71oCkrZlGPL.jpg"),
        ("Life 3.0", "Max Tegmark", 2017, "https://images-na.ssl-images-amazon.com/images/I/71S0W2m4ULL.jpg"),
        ("The Code Breaker", "Walter Isaacson", 2021, "https://images-na.ssl-images-amazon.com/images/I/71kPQs7GYJL.jpg"),
        ("Algorithms to Live By", "Brian Christian", 2016, "https://images-na.ssl-images-amazon.com/images/I/71XhB5GQHML.jpg"),
        ("The Singularity Is Near", "Ray Kurzweil", 2005, "https://images-na.ssl-images-amazon.com/images/I/71S1vWnrccL.jpg"),
    ]
    
    for title, author, year, cover in books_technology:
        create_book(title, author, "technology", cover, year, {
            "rating": 4.5,
            "time": 15,
            "quote": "Technology is best when it brings people together.",
            "overview": "Understand the technologies shaping our future.",
            "executive": f"{title} explores innovation, AI, and the digital transformation of society.",
            "ideas": "Digital revolution, AI, internet, and future tech.",
            "takeaways": [
                {"title": "Embrace Change", "text": "Technology evolves exponentially."},
                {"title": "Stay Curious", "text": "Continuous learning is essential."},
            ],
            "quotes": [
                "Any sufficiently advanced technology is indistinguishable from magic.",
                "The best way to predict the future is to invent it.",
            ],
            "actions": [
                "Learn one new technology skill",
                "Build a simple project",
                "Follow tech trends"
            ],
            "audience": "Technologists, innovators, and future thinkers."
        })
    
    print("✅ Successfully seeded 100 top books across all genres!")
    db.close()

if __name__ == "__main__":
    seed_100_books()
