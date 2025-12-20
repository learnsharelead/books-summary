"""
Fix Biography Books Content
Updates placeholder content with rich, detailed summaries.
Run with: python -m database.fix_biography_content
"""

import json
from database.connection import get_session
from database.models import Genre, Book, Summary

# Books that need full content updates
BIOGRAPHY_BOOKS = [
    {
        "title": "Steve Jobs",
        "takeaways": [
            {"title": "Reality Distortion Field", "text": "Jobs could convince people that seemingly impossible things were achievable through sheer force of will. He believed that ordinary rules didn't apply to him, and this mindset often led to extraordinary achievements. When his engineers said something couldn't be done, he would simply reject reality and demand they find a way."},
            {"title": "Simplicity is the Ultimate Sophistication", "text": "Jobs obsessed over creating products that were elegantly simple. He believed that truly understanding a problem meant you could distill it to its essence. Every Apple product went through countless iterations to remove unnecessary complexity and achieve perfect simplicity."},
            {"title": "End-to-End Control", "text": "Jobs insisted on controlling both hardware and software to create seamless user experiences. He believed that integrated systems, where every component was designed to work together, produced superior products compared to open platforms with mix-and-match components."},
            {"title": "Design is How it Works", "text": "For Jobs, design wasn't just about aesthetics—it was about function. Beautiful products that didn't work well were failures. He pushed teams to create products where form followed function, but both were executed with extreme attention to detail."}
        ],
        "quotes": [
            "Stay hungry, stay foolish.",
            "Design is not just what it looks like. Design is how it works.",
            "Innovation distinguishes between a leader and a follower.",
            "The people who are crazy enough to think they can change the world are the ones who do."
        ],
        "action_steps": [
            "Identify one area in your work where you can simplify dramatically",
            "Challenge a 'limitation' that others have accepted as unchangeable",
            "Focus on the complete experience, not just individual features",
            "Say no to a hundred things to focus on what truly matters"
        ]
    },
    {
        "title": "The Innovators",
        "takeaways": [
            {"title": "Collaboration Drives Innovation", "text": "The digital revolution was not created by lone geniuses but by teams of creative people. From Ada Lovelace and Charles Babbage to Steve Jobs and Steve Wozniak, the most significant breakthroughs came from collaborative partnerships that combined technical and visionary skills."},
            {"title": "Standing on Shoulders of Giants", "text": "Every major innovation in computing built upon previous work. The transistor led to the microchip, which enabled personal computers, which made the internet accessible. Understanding this chain of innovation helps us see how progress really happens."},
            {"title": "Creativity Meets Technology", "text": "The most transformative innovations happened when humanities and sciences intersected. People like Ada Lovelace, who combined poetic imagination with mathematical reasoning, saw possibilities that pure technologists missed."},
            {"title": "Persistent Vision", "text": "Many ideas that now seem obvious were considered impossible at their inception. Pioneers like Alan Turing and Grace Hopper persisted through skepticism because they could envision possibilities others couldn't see."}
        ],
        "quotes": [
            "Innovation comes from teams more often than from the lightbulb moments of lone geniuses.",
            "Creativity is connecting things.",
            "The truest geniuses typically have the ability to collaborate."
        ],
        "action_steps": [
            "Build a diverse team combining technical and creative perspectives",
            "Study the history of your field to understand how past innovations enable future ones",
            "Create environments that encourage cross-disciplinary collaboration",
            "Document and share your innovations to enable others to build upon them"
        ]
    },
    {
        "title": "Einstein: His Life and Universe",
        "takeaways": [
            {"title": "Question the Obvious", "text": "Einstein's genius lay in questioning assumptions others took for granted. He wondered what it would be like to ride on a beam of light—a question that seemed childish but led to special relativity. Great discoveries often come from revisiting 'obvious' truths."},
            {"title": "Thought Experiments", "text": "Einstein did his most revolutionary work through gedankenexperimente (thought experiments). He visualized physical scenarios and followed their logical implications. This imaginative approach allowed him to see what mathematical analysis alone could not reveal."},
            {"title": "Independence of Mind", "text": "Einstein valued non-conformity and independent thinking above all. He resisted authority, questioned established doctrines, and maintained his own course even when isolated from mainstream physics. This independence was essential to his breakthroughs."},
            {"title": "Creativity Requires Freedom", "text": "Einstein believed that imagination was more important than knowledge. He advocated for intellectual freedom and playful exploration. His work at the patent office, away from academic pressure, gave him the freedom to think originally."}
        ],
        "quotes": [
            "Imagination is more important than knowledge.",
            "The important thing is not to stop questioning.",
            "If you can't explain it simply, you don't understand it well enough.",
            "A person who never made a mistake never tried anything new."
        ],
        "action_steps": [
            "Schedule time for unstructured thinking and wondering",
            "Question one assumption in your field that everyone accepts",
            "Use thought experiments to explore problems before diving into details",
            "Seek out perspectives from outside your field"
        ]
    },
    {
        "title": "Benjamin Franklin: An American Life",
        "takeaways": [
            {"title": "Perpetual Self-Improvement", "text": "Franklin created a systematic approach to personal development, tracking 13 virtues and evaluating himself weekly. He believed character could be developed through conscious practice and wasn't fixed at birth."},
            {"title": "Pragmatic Problem Solver", "text": "Franklin approached both personal and civic problems with practical creativity. From lightning rods to bifocals to the lending library, he saw problems as opportunities for innovation that could benefit everyone."},
            {"title": "Building Networks of Mutual Aid", "text": "Franklin founded clubs, societies, and institutions that brought together people with shared interests to achieve common goals. He understood that individuals working together could accomplish what none could do alone."},
            {"title": "The Power of Reputation", "text": "Franklin carefully cultivated his public image as a hardworking, humble, and wise figure. He understood that reputation was a form of capital that could be invested to achieve larger goals."}
        ],
        "quotes": [
            "An investment in knowledge pays the best interest.",
            "By failing to prepare, you are preparing to fail.",
            "Well done is better than well said.",
            "Energy and persistence conquer all things."
        ],
        "action_steps": [
            "Create your own virtue list and track progress weekly",
            "Form or join a group focused on mutual improvement",
            "Look for practical solutions that could benefit your community",
            "Consider how your daily actions shape your reputation"
        ]
    },
    {
        "title": "Elon Musk",
        "takeaways": [
            {"title": "First Principles Thinking", "text": "Musk approaches problems by breaking them down to fundamental truths rather than reasoning by analogy. When told something was impossible or too expensive, he would examine the basic physics and economics to find innovative solutions others missed."},
            {"title": "Audacious Goal Setting", "text": "Musk sets goals that others consider impossible—colonizing Mars, making electric cars mainstream, revolutionizing transportation. These massive ambitions attract talent and create the urgency needed for breakthrough innovation."},
            {"title": "Extreme Risk Tolerance", "text": "Musk invested his entire PayPal fortune into SpaceX and Tesla when both were on the verge of failure. He accepts personal risk that most entrepreneurs would consider insane, betting everything on his vision."},
            {"title": "Vertical Integration", "text": "Both SpaceX and Tesla build their own components in-house rather than relying on suppliers. This control allows for rapid iteration, cost reduction, and innovations that wouldn't be possible with traditional supply chains."}
        ],
        "quotes": [
            "When something is important enough, you do it even if the odds are not in your favor.",
            "I think it's important to reason from first principles rather than by analogy.",
            "Failure is an option here. If things are not failing, you are not innovating enough."
        ],
        "action_steps": [
            "Break down one 'impossible' challenge to its fundamental components",
            "Set one goal that feels almost too ambitious",
            "Identify where you can gain more control over critical processes",
            "Build tolerance for failure by attempting smaller experiments"
        ]
    },
    {
        "title": "Alexander Hamilton",
        "takeaways": [
            {"title": "Write Your Way to Power", "text": "Hamilton wrote his way from obscure orphan to Founding Father. His essays, reports, and letters shaped American institutions and policy. He understood that ideas, articulated persuasively, could change the world."},
            {"title": "Build Lasting Institutions", "text": "Hamilton's financial system—the national bank, assumption of state debts, the mint—created the foundation for American economic power. He thought in terms of institutions that would outlast any individual."},
            {"title": "Energy in the Executive", "text": "Hamilton argued for a strong executive branch when others feared concentrated power. He believed effective government required energetic leadership, not just checks and balances."},
            {"title": "Never-ending Work Ethic", "text": "Hamilton's output was staggering—he wrote most of the Federalist Papers, created the Treasury Department from scratch, and worked relentlessly. He believed there was no accomplishment without effort."}
        ],
        "quotes": [
            "Those who stand for nothing fall for anything.",
            "The sacred rights of mankind are not to be rummaged for among old parchments.",
            "I never expect to see a perfect work from imperfect man."
        ],
        "action_steps": [
            "Write regularly to develop and communicate your ideas",
            "Think about what institutions you could create or improve",
            "Find ways to be more energetic in your leadership",
            "Commit to outworking everyone else in your field"
        ]
    },
    {
        "title": "Leonardo da Vinci",
        "takeaways": [
            {"title": "Insatiable Curiosity", "text": "Leonardo asked questions about everything—why the sky is blue, how a woodpecker's tongue works, what makes people yawn. This curiosity across disciplines was the source of his genius."},
            {"title": "Observe with Intensity", "text": "Leonardo spent hours watching birds fly, water flow, and faces express emotion. He drew what he saw not as he thought it should be, but as it actually was. This careful observation was the foundation of both his art and his science."},
            {"title": "Connect Across Disciplines", "text": "Leonardo saw connections between anatomy and architecture, between military engineering and fine art. He moved fluidly between fields, bringing insights from one domain to another."},
            {"title": "Embrace Procrastination", "text": "Leonardo left many works unfinished, returning to them over years or decades. This 'procrastination' allowed ideas to develop and connections to emerge that wouldn't have appeared if he had rushed to completion."}
        ],
        "quotes": [
            "Learning never exhausts the mind.",
            "Simplicity is the ultimate sophistication.",
            "I have been impressed with the urgency of doing. Knowing is not enough; we must apply."
        ],
        "action_steps": [
            "Keep a curious journal like Leonardo's notebooks",
            "Spend time observing something closely—without your phone",
            "Learn something from an unrelated field this week",
            "Return to an unfinished project with fresh eyes"
        ]
    }
]

def fix_biography_content():
    """Update biography books with rich content."""
    db = get_session()
    
    updated_count = 0
    
    for book_data in BIOGRAPHY_BOOKS:
        # Find the book
        book = db.query(Book).filter(Book.title == book_data["title"]).first()
        
        if not book:
            print(f"⚠️ Book not found: {book_data['title']}")
            continue
        
        # Find the summary
        summary = db.query(Summary).filter(Summary.book_id == book.id).first()
        
        if not summary:
            print(f"⚠️ Summary not found for: {book_data['title']}")
            continue
        
        # Update the summary
        summary.key_takeaways = json.dumps(book_data["takeaways"])
        summary.quotes = json.dumps(book_data.get("quotes", []))
        summary.action_steps = json.dumps(book_data.get("action_steps", []))
        summary.quote_of_the_book = book_data["quotes"][0] if book_data.get("quotes") else ""
        
        db.commit()
        updated_count += 1
        print(f"✅ Updated: {book_data['title']}")
    
    db.close()
    print(f"\n🎉 Done! Updated {updated_count} books.")

if __name__ == "__main__":
    fix_biography_content()
