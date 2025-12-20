"""
Complete Biography Books Content Fix
Updates all biography books with comprehensive rich content.
Run with: python -m database.fix_all_biography_content
"""

import json
from database.connection import get_session
from database.models import Genre, Book, Summary

# Complete biography books with full rich content
BIOGRAPHY_BOOKS_COMPLETE = [
    {
        "title": "Steve Jobs",
        "executive_summary": """Steve Jobs, the legendary co-founder of Apple, was one of the most transformative figures in modern business history. Walter Isaacson's biography draws from over forty interviews with Jobs, as well as hundreds of interviews with family, friends, adversaries, and colleagues.

Jobs was a study in contradictions—a Zen Buddhist who threw tantrums, a college dropout who built the world's most valuable company, and a demanding perfectionist who created products beloved by billions. His intensity, passion for design, and ability to envision products before they existed made Apple the most innovative company of its era.

The book chronicles Jobs's journey from his adoption, through his founding of Apple in a garage, his ousting from the company, his wilderness years at NeXT and Pixar, and his triumphant return to Apple where he launched the iMac, iPod, iPhone, and iPad. Most importantly, it reveals the principles that drove him: simplicity, end-to-end control, and the intersection of technology and liberal arts.""",
        "main_content": """### The Reality Distortion Field

Jobs possessed an almost supernatural ability to bend reality to his will. When engineers said something was impossible, he would simply refuse to accept it, pushing them to achieve what they didn't think they could. This "reality distortion field" was both his greatest strength and his most frustrating quality.

### Design Philosophy

For Jobs, design was not about decoration—it was about how a product worked at its core. He obsessed over details that most executives would ignore: the internal layout of circuit boards, the feel of buttons, the typography on screens. He believed that truly great products came from caring about every element, even the ones users would never see.

### End-to-End Integration

Jobs insisted on controlling both hardware and software because he believed this was the only way to create truly excellent user experiences. This philosophy contrasted sharply with the open model of competitors like Microsoft and Google, but it produced products of remarkable elegance and simplicity.

### The Intersection of Technology and Liberal Arts

Jobs saw Apple as standing at the intersection of technology and the humanities. He believed that purely technical people could not create products that changed the world—you needed the sensibility of artists, the understanding of psychology, and appreciation for design.""",
        "takeaways": [
            {"title": "Reality Distortion Field", "text": "Jobs could convince people that seemingly impossible things were achievable through sheer force of will. He believed that ordinary rules didn't apply to him, and this mindset often led to extraordinary achievements. When his engineers said something couldn't be done, he would simply reject reality and demand they find a way."},
            {"title": "Simplicity is the Ultimate Sophistication", "text": "Jobs obsessed over creating products that were elegantly simple. He believed that truly understanding a problem meant you could distill it to its essence. Every Apple product went through countless iterations to remove unnecessary complexity and achieve perfect simplicity."},
            {"title": "End-to-End Control", "text": "Jobs insisted on controlling both hardware and software to create seamless user experiences. He believed that integrated systems, where every component was designed to work together, produced superior products compared to open platforms with mix-and-match components."},
            {"title": "Focus Means Saying No", "text": "When Jobs returned to Apple in 1997, he cut the product line from dozens of products to just four. He believed that deciding what not to do was as important as deciding what to do. Focus was essential to achieving excellence."},
            {"title": "Design is How it Works", "text": "For Jobs, design wasn't just about aesthetics—it was about function. Beautiful products that didn't work well were failures. He pushed teams to create products where form followed function, but both were executed with extreme attention to detail."}
        ],
        "quotes": [
            "Stay hungry, stay foolish.",
            "Design is not just what it looks like. Design is how it works.",
            "Innovation distinguishes between a leader and a follower.",
            "The people who are crazy enough to think they can change the world are the ones who do.",
            "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose.",
            "Quality is more important than quantity. One home run is much better than two doubles."
        ],
        "action_steps": [
            "Identify one area in your work where you can simplify dramatically",
            "Challenge a 'limitation' that others have accepted as unchangeable",
            "Focus on the complete experience, not just individual features",
            "Say no to a hundred things to focus on what truly matters",
            "Ask yourself: Would I be proud of this if it were the last thing I ever created?"
        ],
        "who_should_read": "Entrepreneurs, designers, product managers, anyone interested in leadership, innovation, and building world-changing companies. Also valuable for those seeking to understand the trade-offs between perfectionism and personal relationships."
    },
    {
        "title": "The Innovators",
        "executive_summary": """Walter Isaacson's sweeping history of the digital revolution traces the brilliant minds who created the computer and the internet. From Ada Lovelace, who wrote the first computer program in the 1840s, to Alan Turing, who decoded Nazi messages and conceived of the modern computer, to the entrepreneurs of Silicon Valley—Steve Jobs, Bill Gates, and Larry Page—this is the story of how their minds worked and what made them so creative.

Unlike his biography of Steve Jobs, The Innovators is a group portrait. Isaacson argues that innovation is almost always a collaborative process. The lone genius working in isolation is a myth. From the development of the transistor to the creation of Google, the greatest innovations came from teams of people building on each other's ideas.

The book also emphasizes the importance of the humanities in technological innovation. The most creative innovators were those who combined technical skills with artistic sensibility—people who understood both engineering and human needs.""",
        "main_content": """### Collaboration Over Lone Genius

The myth of the lone inventor working in a garage has some truth—but not much. Almost every major innovation in computing came from collaborative partnerships: Babbage and Lovelace, Watson and Crick, Jobs and Wozniak. The ability to work effectively with others was as important as raw intelligence.

### Building On Previous Work

Every major innovation in the digital age built upon previous work. The transistor led to the microchip, which enabled personal computers, which made the internet accessible to everyone. Understanding this chain of innovation reveals how progress actually happens.

### The Humanities Matter

Ada Lovelace, the world's first programmer, was the daughter of the poet Lord Byron. Steve Jobs studied calligraphy. The most transformative innovations happened when technology and humanities intersected. Pure technologists often missed possibilities that those with broader perspectives could see.

### Persistent Vision

Many ideas that now seem obvious were considered impossible when first proposed. Alan Turing's concept of a universal computing machine, Grace Hopper's compiler, Tim Berners-Lee's World Wide Web—all were initially met with skepticism. Their creators succeeded because they could see possibilities others couldn't imagine.""",
        "takeaways": [
            {"title": "Collaboration Drives Innovation", "text": "The digital revolution was not created by lone geniuses but by teams of creative people. From Ada Lovelace and Charles Babbage to Steve Jobs and Steve Wozniak, the most significant breakthroughs came from collaborative partnerships that combined technical and visionary skills."},
            {"title": "Standing on Shoulders of Giants", "text": "Every major innovation in computing built upon previous work. The transistor led to the microchip, which enabled personal computers, which made the internet accessible. Understanding this chain of innovation helps us see how progress really happens."},
            {"title": "Creativity Meets Technology", "text": "The most transformative innovations happened when humanities and sciences intersected. People like Ada Lovelace, who combined poetic imagination with mathematical reasoning, saw possibilities that pure technologists missed."},
            {"title": "Implementation Matters", "text": "Having a great idea is only the beginning. The history of computing is littered with brilliant concepts that went nowhere because they weren't implemented well or at the right time. Successful innovators combined vision with execution."},
            {"title": "Persistent Vision", "text": "Many ideas that now seem obvious were considered impossible at their inception. Pioneers like Alan Turing and Grace Hopper persisted through skepticism because they could envision possibilities others couldn't see."}
        ],
        "quotes": [
            "Innovation comes from teams more often than from the lightbulb moments of lone geniuses.",
            "Creativity is connecting things.",
            "The truest geniuses typically have the ability to collaborate.",
            "The tale of how computers and the internet were developed is not just a story of vision and genius but a tale of the way innovators built on each other's ideas.",
            "Ada saw the beauty in math that her mother had tried to make her avoid."
        ],
        "action_steps": [
            "Build a diverse team combining technical and creative perspectives",
            "Study the history of your field to understand how past innovations enable future ones",
            "Create environments that encourage cross-disciplinary collaboration",
            "Document and share your innovations to enable others to build upon them",
            "Read widely outside your specialty to find unexpected connections"
        ],
        "who_should_read": "Technologists, entrepreneurs, students of innovation, and anyone interested in understanding how the digital world was created. Particularly valuable for those who want to understand the collaborative nature of breakthrough innovation."
    },
    {
        "title": "Elon Musk",
        "executive_summary": """Ashlee Vance's biography of Elon Musk reveals the extraordinary ambition and relentless drive of one of the most controversial entrepreneurs of our time. Musk has taken on industries that most considered impossible to disrupt: space travel with SpaceX, automobiles with Tesla, and energy with SolarCity.

The book traces Musk's journey from his difficult childhood in South Africa, through his early internet ventures (Zip2 and PayPal), to his bet-everything approach to building companies that could change humanity's future. Vance gained unprecedented access to Musk, his family, and his employees, painting a portrait of a man who sets impossible goals and then drives himself and everyone around him to achieve them.

What emerges is a picture of someone willing to accept personal risk that would terrify most entrepreneurs, who reasons from first principles rather than analogy, and who genuinely believes in missions—like making humanity a multi-planetary species—that others consider delusional.""",
        "main_content": """### First Principles Thinking

Musk approaches problems differently than most entrepreneurs. Instead of reasoning by analogy ("This is how it's always been done"), he breaks down problems to their fundamental truths and reasons up from there. When told that rockets were prohibitively expensive, he looked at the raw materials cost and realized that existing prices were inflated by orders of magnitude.

### Audacious Goal Setting

SpaceX's goal is to colonize Mars. Tesla's goal is to accelerate the transition to sustainable energy. These aren't marketing slogans—they're organizing principles that drive every decision. Such ambitious goals attract exceptional talent and create the urgency needed for breakthrough innovation.

### Vertical Integration

Both SpaceX and Tesla build a remarkable amount of their components in-house. SpaceX manufactures about 80% of its rockets internally. This control allows for rapid iteration, cost reduction, and innovations that wouldn't be possible working with traditional supply chains.

### Personal Risk Tolerance

In 2008, both SpaceX and Tesla were on the verge of bankruptcy. Musk put his last $40 million into keeping them alive. His willingness to risk everything—including money from his PayPal sale that most people would have used to retire—distinguishes him from conventional entrepreneurs.""",
        "takeaways": [
            {"title": "First Principles Thinking", "text": "Musk approaches problems by breaking them down to fundamental truths rather than reasoning by analogy. When told something was impossible or too expensive, he would examine the basic physics and economics to find innovative solutions others missed."},
            {"title": "Audacious Goal Setting", "text": "Musk sets goals that others consider impossible—colonizing Mars, making electric cars mainstream, revolutionizing transportation. These massive ambitions attract talent and create the urgency needed for breakthrough innovation."},
            {"title": "Extreme Risk Tolerance", "text": "Musk invested his entire PayPal fortune into SpaceX and Tesla when both were on the verge of failure. He accepts personal risk that most entrepreneurs would consider insane, betting everything on his vision."},
            {"title": "Vertical Integration", "text": "Both SpaceX and Tesla build their own components in-house rather than relying on suppliers. This control allows for rapid iteration, cost reduction, and innovations that wouldn't be possible with traditional supply chains."},
            {"title": "Mission-Driven Leadership", "text": "Musk's companies are organized around missions that matter: sustainable energy, multi-planetary life. These purposes attract idealistic talent and justify the extreme effort required to achieve seemingly impossible goals."}
        ],
        "quotes": [
            "When something is important enough, you do it even if the odds are not in your favor.",
            "I think it's important to reason from first principles rather than by analogy.",
            "Failure is an option here. If things are not failing, you are not innovating enough.",
            "I would like to die on Mars. Just not on impact.",
            "If you get up in the morning and think the future is going to be better, it is a bright day.",
            "Persistence is very important. You should not give up unless you are forced to give up."
        ],
        "action_steps": [
            "Break down one 'impossible' challenge to its fundamental components",
            "Set one goal that feels almost too ambitious",
            "Identify where you can gain more control over critical processes",
            "Build tolerance for failure by attempting smaller experiments",
            "Connect your work to a purpose larger than profit"
        ],
        "who_should_read": "Entrepreneurs, innovators, and anyone curious about what it takes to build companies that change the world. Valuable for understanding the costs and trade-offs of extreme ambition."
    },
    {
        "title": "Becoming",
        "executive_summary": """Michelle Obama's memoir is an intimate look at the life of the former First Lady of the United States. From her childhood on the South Side of Chicago, through her years at Princeton and Harvard Law School, her career as a lawyer, her marriage to Barack Obama, and her eight years in the White House—Becoming is both a deeply personal reflection and an inspiring guide to finding your voice.

The book is remarkable for its honesty about the challenges Obama faced: feeling like an outsider at Princeton, questioning whether to give up her legal career for her husband's political ambitions, navigating the scrutiny of being the first Black First Lady, and raising two daughters in the most public fishbowl in the world.

At its core, Becoming is about the ongoing process of self-discovery. Obama argues that we are never finished becoming who we are—that growth is continuous, and our stories are never complete. It's a message of hope, resilience, and the power of authenticity.""",
        "main_content": """### South Side Values

Michelle Robinson grew up in a working-class family in Chicago, where hard work, education, and family were paramount. Her parents, especially her father who worked despite his multiple sclerosis, modeled perseverance and dignity. These values shaped everything that followed.

### Finding Her Voice

At Princeton and Harvard, Obama often felt like an outsider—one of few Black students, constantly aware of how she was perceived. Learning to speak up despite imposter syndrome became essential to her growth. She discovered that her perspective was not a weakness but a strength.

### Partnership and Sacrifice

The book is candid about the challenges of marriage to an ambitious politician. Obama gave up a thriving legal career and faced long periods as effectively a single parent. The partnership with Barack required constant negotiation and mutual sacrifice.

### Platform and Purpose

As First Lady, Obama found her voice through initiatives like Let's Move! and Let Girls Learn. She used her unprecedented platform to advocate for causes she believed in, showing that any position can become a vehicle for positive change.

### The Ongoing Journey

The title reflects Obama's core message: we are always in the process of becoming. There is no final destination, no moment when we have "arrived." Growth is continuous, and embracing that process is what makes life meaningful.""",
        "takeaways": [
            {"title": "Becoming is Continuous", "text": "There is no final destination in personal growth. We are always in the process of becoming who we are. Embracing this journey—rather than waiting to 'arrive'—is what makes life meaningful and fulfilling."},
            {"title": "Your Story Matters", "text": "Obama felt like an outsider at Princeton and Harvard, but learned that her unique perspective was a strength. Your background and experiences give you insights that others lack. Don't hide them—share them."},
            {"title": "Find Your Voice", "text": "Speaking up despite imposter syndrome and fear is essential to growth. Obama learned to advocate for herself and others, discovering that silence serves no one."},
            {"title": "Swerving is Okay", "text": "Obama's career took many unexpected turns—from law firm to city hall to nonprofit to the White House. These 'swerves' weren't failures but opportunities for growth and discovery."},
            {"title": "Use Your Platform", "text": "Whatever position you hold, you have a platform to create positive change. Obama used her role as First Lady to advocate for children's health and girls' education globally."}
        ],
        "quotes": [
            "There is no limit to what we, as women, can accomplish.",
            "When they go low, we go high.",
            "Your story is what you have, what you will always have. It is something to own.",
            "Failure is a feeling long before it's an actual result.",
            "Do we settle for the world as it is, or do we work for the world as it should be?",
            "I have learned that as long as I hold fast to my beliefs and values, and follow my own moral compass, then the only expectations I need to live up to are my own."
        ],
        "action_steps": [
            "Write down three defining moments from your childhood that shaped who you are",
            "Identify one area where you've been silencing your authentic voice",
            "Embrace a 'swerve' in your career as an opportunity rather than a setback",
            "Find one way to use your current platform—however small—for positive change",
            "Mentor someone who reminds you of yourself at an earlier stage"
        ],
        "who_should_read": "Women seeking inspiration and practical wisdom, leaders navigating complex careers, parents balancing family and ambition, and anyone interested in the personal side of public figures. Especially powerful for those who have ever felt like outsiders."
    },
    {
        "title": "Leonardo da Vinci",
        "executive_summary": """Walter Isaacson's biography of Leonardo da Vinci reveals the genius who was perhaps the most creative person in history. Leonardo was not only the painter of the Mona Lisa and The Last Supper but also an anatomist, engineer, scientist, and philosopher. Isaacson draws from Leonardo's legendary notebooks—7,200 pages of his notes and drawings—to paint a portrait of a mind unlike any other.

What made Leonardo genius was not superhuman intelligence but superhuman curiosity. He made to-do lists that included items like "Describe the tongue of the woodpecker" and spent hours observing water, light, and human expressions. His genius grew from the combination of intense observation, creative imagination, and the ability to see connections across vastly different fields.

The book also reveals Leonardo's relatable qualities: his procrastination, his unfinished projects, his playful personality. He was gay, vegetarian, left-handed, illegitimate, and easily distracted—yet he produced some of the greatest works of art and science in human history.""",
        "main_content": """### Insatiable Curiosity

Leonardo asked questions about everything—why the sky is blue, how a woodpecker's tongue works, what makes people yawn. He filled notebook after notebook with observations and questions. This curiosity was not means to an end; it was joy in itself.

### Observation as Foundation

Leonardo spent countless hours watching birds fly, water flow, and faces express emotion. He drew what he saw not as he assumed it should be, but as it actually was. This intense observation was the foundation of both his art and his science.

### Cross-Disciplinary Thinking

Leonardo moved fluidly between fields—from anatomy to architecture, from engineering to painting. He saw connections that specialists missed: the swirling of water resembled the curling of hair; the branching of trees mirrored the branching of blood vessels.

### Productive Procrastination

Leonardo left many works unfinished, including several major paintings. While this frustrated his patrons, it allowed ideas to develop over years. The Mona Lisa was worked on for more than a decade. Sometimes delay leads to depth.

### Theory and Practice Together

Leonardo believed in combining theory (reasoning from principles) with experience (observation and experiment). Neither alone was sufficient. The greatest insights came from their intersection.""",
        "takeaways": [
            {"title": "Insatiable Curiosity", "text": "Leonardo asked questions about everything—why the sky is blue, how a woodpecker's tongue works, what makes people yawn. This curiosity across disciplines was the source of his genius. Being curious about things for their own sake leads to unexpected discoveries."},
            {"title": "Observe with Intensity", "text": "Leonardo spent hours watching birds fly, water flow, and faces express emotion. He drew what he saw not as he thought it should be, but as it actually was. This careful observation was the foundation of both his art and his science."},
            {"title": "Connect Across Disciplines", "text": "Leonardo saw connections between anatomy and architecture, between military engineering and fine art. He moved fluidly between fields, bringing insights from one domain to another. The most creative thinking happens at intersections."},
            {"title": "Embrace Mystery", "text": "Leonardo was comfortable with ambiguity and mystery—the Mona Lisa's enigmatic smile, the sfumato technique that blurs boundaries. He understood that not everything needs to be resolved; sometimes mystery is the point."},
            {"title": "Be Willing to Be Different", "text": "Leonardo was illegitimate, gay, vegetarian, left-handed, and easily distracted. He didn't try to fit in. His willingness to be different was not separate from his genius—it was part of it."}
        ],
        "quotes": [
            "Learning never exhausts the mind.",
            "Simplicity is the ultimate sophistication.",
            "I have been impressed with the urgency of doing. Knowing is not enough; we must apply.",
            "The noblest pleasure is the joy of understanding.",
            "Study without desire spoils the memory, and it retains nothing that it takes in.",
            "The painter who draws by practice and judgment of the eye without the use of reason is like a mirror that reproduces whatever is placed before it without knowledge of the same."
        ],
        "action_steps": [
            "Keep a curious journal like Leonardo's notebooks—ask questions, sketch observations",
            "Spend time observing something closely—really looking—without your phone",
            "Learn something from an unrelated field this week",
            "Return to an unfinished project with fresh eyes—delay might add depth",
            "Ask 'why' about something obvious that everyone takes for granted"
        ],
        "who_should_read": "Creative professionals, scientists, artists, and anyone curious about how genius works. Particularly valuable for those who feel they lack focus—Leonardo shows that following diverse interests can be a strength."
    }
]

def fix_all_biography_content():
    """Update all biography books with comprehensive rich content."""
    db = get_session()
    
    updated_count = 0
    
    for book_data in BIOGRAPHY_BOOKS_COMPLETE:
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
        
        # Update all fields of the summary
        summary.executive_summary = book_data["executive_summary"]
        summary.main_content = book_data["main_content"]
        summary.key_takeaways = json.dumps(book_data["takeaways"])
        summary.quotes = json.dumps(book_data["quotes"])
        summary.action_steps = json.dumps(book_data["action_steps"])
        summary.who_should_read = book_data["who_should_read"]
        summary.quote_of_the_book = book_data["quotes"][0] if book_data.get("quotes") else ""
        
        db.commit()
        updated_count += 1
        print(f"✅ Updated: {book_data['title']}")
    
    db.close()
    print(f"\n🎉 Done! Updated {updated_count} biography books with comprehensive content.")

if __name__ == "__main__":
    fix_all_biography_content()
