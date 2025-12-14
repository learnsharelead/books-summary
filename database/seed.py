"""
Seed database with World-Class rich book summaries.
Updated to include Analogies, Action Steps, Quotes, and Executive Summaries.
"""

from sqlalchemy.orm import Session
from database.connection import get_session, engine
from database.models import Base, Genre, Book, Summary, SummaryImage
import json

# Drop tables to ensure clean schema update
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def seed_data():
    db = get_session()
    
    print("🌱 Seeding Genres...")
    genres = [
        Genre(name="Self-Help", slug="self-help", icon="🌱", description="Books for personal growth and improvement."),
        Genre(name="Business", slug="business", icon="💼", description="Strategy, leadership, and entrepreneurship."),
        Genre(name="Psychology", slug="psychology", icon="🧠", description="Understanding the human mind and behavior."),
        Genre(name="Finance", slug="finance", icon="💰", description="Money management and investing wisdom."),
        Genre(name="Productivity", slug="productivity", icon="⚡", description="Optimization and time management."),
        Genre(name="Philosophy", slug="philosophy", icon="🤔", description="Timeless wisdom and critical thinking."),
        Genre(name="History", slug="history", icon="🏺", description="The story of humanity and civilization."),
    ]
    db.add_all(genres)
    db.commit()
    
    genre_map = {g.slug: g for g in genres}
    
    print("📚 Seeding Books & Summaries...")
    
    # helper for creating full content
    def create_content(title, author, genre_slug, cover_url, year, summary_data):
        book = Book(
            title=title,
            author=author,
            slug=title.lower().replace(" ", "-").replace(":", "").replace("'", ""),
            cover_image_url=cover_url,
            publication_year=year,
            genre=genre_map[genre_slug],
            is_featured=True
        )
        db.add(book)
        db.commit() # commit to get ID
        
        summary = Summary(
            book_id=book.id,
            overview_text=summary_data['overview'],
            executive_summary=summary_data.get('executive', summary_data['overview']),
            quote_of_the_book=summary_data.get('main_quote', "A great book is a friend that never lets you down."),
            main_content=summary_data['core_ideas'],
            key_takeaways=json.dumps(summary_data['takeaways']),
            who_should_read=summary_data['who_should_read'],
            reading_time=summary_data['read_time'],
            rating=summary_data.get('rating', 4.5),
            difficulty="Beginner" if summary_data.get('easy', True) else "Intermediate",
            seo_title=f"{title} Summary and Key Takeaways",
            seo_description=f"Read the summary of {title}. Key insights included.",
            workflow_data=summary_data.get('workflow', None),
            analogies=json.dumps(summary_data.get('analogies', [])),
            quotes=json.dumps(summary_data.get('quotes', [])),
            action_steps=json.dumps(summary_data.get('action_steps', []))
        )
        db.add(summary)
        
        # Add Concept Images if any
        if 'images' in summary_data:
            for img in summary_data['images']:
                db.add(SummaryImage(
                    summary=summary,
                    image_url=img['url'],
                    caption=img['caption'],
                    section_type="concept",
                    section_title="Core Concept"
                ))
        
        db.commit()

    # ==================== ATOMIC HABITS (COMPREHENSIVE) ====================
    create_content(
        title="Atomic Habits",
        author="James Clear",
        genre_slug="self-help",
        cover_url="https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg",
        year=2018,
        summary_data={
            "rating": 4.9,
            "read_time": 18,
            "main_quote": "You do not rise to the level of your goals. You fall to the level of your systems.",
            "overview": "A comprehensive, science-backed guide to building good habits and breaking bad ones through tiny, incremental changes.",
            "executive": """
**Atomic Habits** represents a paradigm shift in how we think about personal development and behavioral change. James Clear's fundamental thesis challenges the conventional wisdom that success requires massive, overnight transformations. Instead, he presents a compelling case for the power of marginal gains—the idea that improving by just 1% each day compounds into remarkable results over time.

The book's core philosophy rests on three interconnected pillars:

**1. Systems Trump Goals**  
While everyone has goals, Clear argues that winners and losers often share the same aspirations. What separates them is not the goal itself, but the systems they implement to achieve it. A goal is about the results you want to achieve; a system is about the processes that lead to those results. Clear emphasizes that if you're having trouble changing your habits, the problem isn't you—the problem is your system.

**2. Identity-Based Habits**  
Most people approach habit change from the outside in—focusing on what they want to achieve (outcome), then what they need to do (process), and rarely addressing who they need to become (identity). Clear flips this model, arguing that true behavior change starts with identity change. Instead of saying "I want to run a marathon" (outcome-based), say "I am a runner" (identity-based). Your current behaviors are simply a reflection of your current identity. To change your behavior for good, you need to change your beliefs about yourself.

**3. The Four Laws of Behavior Change**  
Clear distills behavioral psychology into a simple, actionable framework:
- Make it Obvious (Cue)
- Make it Attractive (Craving)  
- Make it Easy (Response)
- Make it Satisfying (Reward)

These laws apply to both building good habits and breaking bad ones. To break a bad habit, simply invert the laws: Make it invisible, make it unattractive, make it difficult, and make it unsatisfying.

The book's genius lies in its practical applicability. Clear doesn't just explain the science—he provides concrete strategies like habit stacking (pairing a new habit with an existing one), environment design (making cues obvious), the two-minute rule (scaling habits down to their smallest viable version), and implementation intentions (planning exactly when and where you'll act).

What makes this particularly powerful is the concept of **compound interest in self-improvement**. If you can get 1% better each day for one year, you'll end up thirty-seven times better by the time you're done. Conversely, if you get 1% worse each day for one year, you'll decline nearly down to zero. Small changes appear to make no difference until you cross a critical threshold—what Clear calls "the Plateau of Latent Potential."
            """,
            
            "core_ideas": """
### The Surprising Power of Atomic Habits

The backbone of the book is understanding that **habits are the compound interest of self-improvement**. Just as money multiplies through compound interest, the effects of your habits multiply as you repeat them. They seem to make little difference on any given day, yet their impact compounds over months and years.

**Why Small Habits Make a Big Difference:**
- A 1% improvement every day equals being 37.78 times better after one year
- A 1% decline every day reduces you nearly to zero  
- Small changes often appear to make no difference until you cross a critical threshold
- Mastery requires patience and the understanding that breakthroughs occur after periods of latent potential

### How Your Habits Shape Your Identity (and Vice Versa)

Most approaches to habit change fail because they focus on the wrong level of change. There are three layers:

1. **Outcomes** (what you get): Losing 20 pounds, publishing a book, winning a championship
2. **Processes** (what you do): Implementing a new gym routine, developing a writing practice  
3. **Identity** (what you believe): Your worldview, self-image, judgments about yourself and others

The most effective way to change your habits is to focus not on what you want to achieve, but on who you wish to become. Your identity emerges out of your habits—every action is a vote for the type of person you wish to become.

**The Identity Change Process:**
- Decide the type of person you want to be
- Prove it to yourself with small wins
- Each habit is basically suggesting: "Hey, you're the type of person who does this"

### The Four Laws in Depth

**LAW 1: Make It Obvious**  
You can't rely on motivation or willpower alone. Your environment shapes your behavior more than you realize. Clear introduces the concept of **implementation intentions**: a plan you make beforehand about when and where to act.

*Strategies:*
- Use implementation intentions: "I will [BEHAVIOR] at [TIME] in [LOCATION]"
- Apply habit stacking: "After [CURRENT HABIT], I will [NEW HABIT]"
- Design your environment so the cues of good habits are obvious and visible
- Use the Pointing-and-Calling technique to raise awareness of actions

**LAW 2: Make It Attractive**  
The more attractive an opportunity is, the more likely it is to become habit-forming. Dopamine drives our desire to take action.

*Strategies:*
- Use temptation bundling: pair an action you want to do with an action you need to do
- Join a culture where your desired behavior is the normal behavior  
- Create a motivation ritual by doing something you enjoy immediately before a difficult habit
- Reframe your mindset: highlight the benefits rather than drawbacks

**LAW 3: Make It Easy**  
The less energy a habit requires, the more likely it is to occur. Focus on taking action, not being in motion.

*Strategies:*
- Reduce friction: decrease the number of steps between you and your good habits
- Prime your environment to make future actions easier
- Master the decisive moment: optimize the small choices that deliver outsized impact
- Use the Two-Minute Rule: when you start a new habit, it should take less than two minutes
- Automate your habits through technology and one-time choices

**LAW 4: Make It Satisfying**  
We are more likely to repeat a behavior when the experience is satisfying. The Cardinal Rule of Behavior Change: What is immediately rewarded is repeated. What is immediately punished is avoided.

*Strategies:*
- Give yourself immediate reward when you complete your habit
- Use habit tracking to create visual proof of progress  
- Never miss twice: if you miss one day, get back on track quickly
- Get an accountability partner or sign a habit contract
            """,
            
            "takeaways": [
                {
                    "title": "Focus on Systems, Not Goals",
                    "text": "Goals are about the results you want to achieve. Systems are about the processes that lead to those results. Fall in love with the process rather than the product. You don't rise to the level of your goals, you fall to the level of your systems. Fix the inputs and the outputs will fix themselves."
                },
                {
                    "title": "The Plateau of Latent Potential", 
                    "text": "Imagine an ice cube sitting on the table at 25°F. You heat it to 26, 27, 28... nothing happens. At 32°F, it begins to melt. All the previous heating wasn't wasted—it was preparing the ice for transformation. Breakthrough moments are often the result of many previous actions which build up the potential required to unleash a major change."
                },
                {
                    "title": "Every Action is a Vote for Your Identity",
                    "text": "Each time you write a page, you are a writer. Each time you practice the violin, you are a musician. Each time you encourage your employees, you are a leader. Habits matter not because they can get you better results, but because they can change your beliefs about yourself."
                },
                {
                    "title": "Environment is the Invisible Hand",
                    "text": "Environment design allows you to take control and become the architect of your life. Create obvious visual cues to draw your attention toward a desired habit. A small change in what you see can lead to a big shift in what you do. Redesign your life so the actions that matter most are also the easiest to do."
                },
                {
                    "title": "The Two-Minute Rule",
                    "text": "When you start a new habit, it should take less than two minutes to do. The point is to master the habit of showing up. The truth is, a habit must be established before it can be improved. Instead of trying to engineer a perfect habit from the start, do the easy thing on a more consistent basis."
                }
            ],
            
            "analogies": [
                {
                    "concept": "Compound Growth & The Valley of Disappointment",
                    "analogy": "The Ice Cube Metaphor",
                    "explanation": "Imagine heating an ice cube from 25°F to 31°F. Nothing happens. At 32°F, it melts. All the previous energy wasn't wasted—it was accumulating beneath the surface. This is the Plateau of Latent Potential. You expect linear progress, but behavior change is nonlinear. Work that seems ineffective is actually building toward a breakthrough. The most powerful outcomes are delayed."
                },
                {
                    "concept": "Habit Stacking",
                    "analogy": "Building a Train",  
                    "explanation": "Your current habits are like a train already in motion. To add new cars (habits), you attach them to existing ones rather than starting a new train from scratch. Formula: After [CURRENT HABIT], I will [NEW HABIT]. Example: 'After I pour my morning coffee, I will meditate for one minute.' The key is to tie your desired behavior into something you already do each day."
                },
                {
                    "concept": "Environment Design",
                    "analogy": "The Supermarket Layout",
                    "explanation": "Grocery stores place milk and eggs at the back, forcing you to walk past thousands of other products. They know environment design influences behavior. Your home is the same—every habit is initiated by a cue, and we are more likely to notice cues that stand out. If you want to make a habit a big part of your life, make the cue a big part of your environment."
                }
            ],
            
            "quotes": [
                "Habits are the compound interest of self-improvement. Getting 1% better every day counts for a lot in the long run.",
                "You do not rise to the level of your goals. You fall to the level of your systems.",
                "Every action you take is a vote for the type of person you wish to become.",
                "The most effective way to change your habits is to focus not on what you want to achieve, but on who you wish to become.",
                "Success is the product of daily habits—not once-in-a-lifetime transformations.",
                "Be the designer of your world and not merely the consumer of it.",
                "Motivation is overrated; environment often matters more.",
                "The purpose of setting goals is to win the game. The purpose of building systems is to continue playing the game."
            ],
            
            "action_steps": [
                "Conduct a Habit Scorecard: Make a list of your daily habits. Mark each habit as positive (+), negative (-), or neutral (=). This awareness is the first step to change.",
                "Use Implementation Intentions: Write down exactly when and where you will perform your new habit. Format: 'I will [BEHAVIOR] at [TIME] in [LOCATION].'",
                "Apply Habit Stacking: Identify a current habit you already do and stack your new behavior on top. Use the formula: 'After [CURRENT HABIT], I will [NEW HABIT].'",
                "Redesign Your Environment: Make the cues of good habits obvious in your environment. Want to practice guitar? Place it in the middle of your living room.",
                "Use the Two-Minute Rule: Scale down your habits until they can be done in two minutes or less. 'Read before bed' becomes 'Read one page.' 'Do yoga' becomes 'Take out my yoga mat.'",
                "Implement the Paper Clip Strategy: Start with two jars. One has 120 paper clips. Each time you complete your habit, move one clip to the other jar. Visual progress creates satisfaction.",
                "Never Miss Twice: If you miss a day, make getting back on track your top priority the next day. Missing once is an accident. Missing twice is the start of a new bad habit."
            ],
            
            "who_should_read": """
**This book is essential for:**
- **Anyone struggling with consistency**: If you've started habits enthusiastically only to abandon them weeks later, this book explains why and how to fix it.
- **Leaders and managers**: Understanding the science of habit formation helps you design better systems for your team and organization.
- **People feeling stuck despite hard work**: If you're working hard but not seeing results, the problem might be your system, not your effort.
- **Students and lifelong learners**: The principles apply to building study habits, learning new skills, and mastering any discipline.
- **Athletes and performers**: Small improvements in technique, repeated consistently, compound into extraordinary results.
- **Anyone seeking personal transformation**: Rather than relying on motivation or willpower, you'll learn to engineer your environment and identity for automatic success.
            """,
            
            "workflow": """
            digraph {
                rankdir=LR;
                node [shape=box, style="filled,rounded", fillcolor="#FFFFFF", fontcolor="#000000", color="#333333", fontname="Arial", penwidth=1];
                edge [color="#666666", penwidth=1];
                bgcolor="transparent";
                
                subgraph cluster_0 {
                    label="The Habit Loop";
                    fontcolor="#666666";
                    style="dashed";
                    color="#AAAAAA";
                    
                    Cue [label="1. CUE\n(Make it Obvious)"];
                    Craving [label="2. CRAVING\n(Make it Attractive)"];
                    Response [label="3. RESPONSE\n(Make it Easy)"];
                    Reward [label="4. REWARD\n(Make it Satisfying)"];
                    
                    Cue -> Craving -> Response -> Reward;
                    Reward -> Cue [label="Reinforces", fontcolor="#666666", style=dotted];
                }
            }
            """
        }
    )

    # 2. Psychology of Money
    create_content(
        title="The Psychology of Money",
        author="Morgan Housel",
        genre_slug="finance",
        cover_url="https://images-na.ssl-images-amazon.com/images/I/715k1M+oWLL.jpg",
        year=2020,
        summary_data={
            "rating": 4.8,
            "read_time": 12,
            "main_quote": "Doing well with money has a little to do with how smart you are and a lot to do with how you behave.",
            "overview": "Timeless lessons on wealth, greed, and happiness.",
            "executive": "Money isn't about math; it's about psychology. Morgan Housel argues that financial success is soft skill, where how you behave is more important than what you know. It teaches you to manage your ego, understand risk, and appreciate the power of compounding.",
            "core_ideas": """
### 1. No One is Crazy
Your experience with money is based on when and where you were born. A person who grew up in the Great Depression thinks about risk differently than someone who grew up in the 90s tech boom. Both are rational based on their own experiences.

### 2. Getting vs. Staying Wealthy
Getting money requires risk, optimism, and putting yourself out there. **Staying wealthy** requires the opposite: paranoia, humility, and a survival mindset.

### 3. Freedom is the Highest Dividend
The ability to do what you want, when you want, with who you want, for as long as you want, is priceless. It is the highest dividend money pays.
            """,
            "takeaways": [
                {"title": "Compounding", "text": "$81.5 billion of Warren Buffett's $84.5 billion net worth came after his 65th birthday."},
                {"title": "Rich vs. Wealthy", "text": "Rich is current income (fast cars). Wealth is income not spent (freedom/options)."},
                {"title": "Enough", "text": "There is no reason to risk what you have and need for what you don't have and don't need."}
            ],
            "analogies": [
                {
                    "concept": "Volatility Fee",
                    "analogy": "Disney World Ticket",
                    "explanation": "Market drops aren't a fine; they are a fee. Like paying $100 for a Disney ticket, you pay a price (volatility) for the reward of long-term returns. It's the cost of admission."
                }
            ],
            "quotes": [
                "Spending money to show people how much money you have is the fastest way to have less money.",
                "Compounding is the eighth wonder of the world.",
                "Save money. You don't need a specific reason to save."
            ],
            "action_steps": [
                "Increase your savings rate regardless of your income.",
                "Define your 'Enough' point to stop moving the goalpost.",
                "Write down your financial 'Sleep at Night' test."
            ],
            "who_should_read": "Investors, savers, and anyone wanting peace of mind with money.",
            "workflow": """
            digraph {
                rankdir=TD;
                node [shape=box, style="filled,rounded", fillcolor="#FFFFFF", fontcolor="#000000", color="#333333", fontname="Arial", penwidth=1];
                edge [color="#666666", penwidth=1];
                bgcolor="transparent";
                
                Income [label="Income Stream"];
                Ego [label="Ego / Spending\n(Rich)"];
                Savings [label="Savings / Investing\n(Wealth)"];
                Time [label="Time (Compounding)"];
                Freedom [label="Freedom\n(The Goal)"];
                
                Income -> Ego [label="High Spend", fontcolor="#666666"];
                Income -> Savings [label="High Save", fontcolor="#666666"];
                Savings -> Time;
                Time -> Freedom;
            }
            """
        }
    )

    # 3. Deep Work
    create_content(
        title="Deep Work",
        author="Cal Newport",
        genre_slug="productivity",
        cover_url="https://images-na.ssl-images-amazon.com/images/I/71e9MYTEOTL.jpg",
        year=2016,
        summary_data={
            "rating": 4.7,
            "main_quote": "Focus is the new IQ in the knowledge economy.",
            "overview": "Rules for focused success in a distracted world.",
            "executive": "In a distracted world, the ability to focus without interruption is a superpower. Deep Work explains how to cultivate this skill to produce elite-level output and master complex information quickly.",
            "core_ideas": "Content about deep work...",
            "takeaways": [
                {"title": "Embrace Boredom", "text": "Train your brain to handle boredom without checking your phone."},
                {"title": "Drain the Shallows", "text": "Minimize logistical 'shallow' work like email."}
            ],
            "who_should_read": "Knowledge workers and students.",
            "read_time": 14,
            "action_steps": ["Schedule deep work blocks.", "Quit social media for 30 days."],
            "workflow": """
            digraph {
                rankdir=LR;
                node [shape=box, style="filled", fillcolor="#111111", fontcolor="white", fontname="Arial"];
                bgcolor="transparent";
                Input -> "Deep Work Block" -> "High Value Output";
            }
            """
        }
    )

    # 4. Sapiens
    create_content(
        title="Sapiens",
        author="Yuval Noah Harari",
        genre_slug="history",
        cover_url="https://covers.openlibrary.org/b/id/12367119-L.jpg",
        year=2011,
        summary_data={
            "rating": 4.8,
            "read_time": 20,
            "main_quote": "Money is the most universal and most efficient system of mutual trust ever devised.",
            "overview": "A brief history of humankind.",
            "executive": "Harari tracks the evolution of Homo sapiens from insignificant apes to rulers of the world, driven by three major revolutions: Cognitive, Agricultural, and Scientific.",
            "core_ideas": "Content about revolutions...",
            "takeaways": [{"title": "Imagined Orders", "text": "Nations and money exist only in our collective imagination."}],
            "who_should_read": "History buffs and thinkers.",
            "action_steps": ["Reflect on your 'imagined orders'.", "Study cross-cultural history."],
            "workflow": """
            digraph {
                rankdir=TD;
                node [shape=box, style="filled", fillcolor="#111111", fontcolor="white", fontname="Arial"];
                bgcolor="transparent";
                Cognitive -> Agricultural -> Scientific;
            }
            """
        }
    )

    print("✅ Database seeded successfully with WORLD-CLASS rich content!")
    db.close()

if __name__ == "__main__":
    seed_data()
