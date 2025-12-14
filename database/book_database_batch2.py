"""
Additional Top Books Database - Batch 2
Books 11-40: More Self-Help, Business, Productivity, Psychology
"""

BOOKS_BATCH_2 = {
    "Grit": {
        "author": "Angela Duckworth",
        "genre": "self-help",
        "year": 2016,
        "rating": 4.5,
        "time": 17,
        "cover": "https://m.media-amazon.com/images/I/71S0WHJL5OL._SL1500_.jpg",
        "overview": "Duckworth shows that achievement isn't just about talent—it's about sustained passion and perseverance.",
        "executive": """**Grit** reveals that the secret to outstanding achievement is not talent but a special blend of **passion and perseverance** Duckworth calls "grit." Her research shows that grit—sustained passion and effort toward long-term goals—is a better predictor of success than IQ or talent.

The **Grit Formula** = Passion + Perseverance. Passion means consistency of interests over time. Perseverance means resilience and hard work. Together, they compound into extraordinary achievement.

Duckworth introduces the concept of **deliberate practice**—focused, goal-oriented practice that pushes you beyond your comfort zone. She also shows how to develop a growth mindset, find purpose beyond yourself, and cultivate hope through optimistic self-talk.""",
        "framework": "Passion × Perseverance = Grit",
        "takeaways": [
            {"title": "Talent ≠ Achievement", "text": "Talent is how quickly skills improve with effort. Achievement is what happens when you apply effort to talent over time. Effort counts twice in the equation: Talent × Effort = Skill, then Skill × Effort = Achievement."},
            {"title": "The Four Psychological Assets", "text": "Gritty people have: 1) Interest (passion for what they do), 2) Practice (daily discipline to improve), 3) Purpose (conviction their work matters), 4) Hope (resilience to persevere through setbacks)."},
            {"title": "Deliberate Practice", "text": "Improvement requires purposeful practice with clear goals, full concentration, immediate feedback, and repetition with reflection. It's uncomfortable but essential for mastery."},
            {"title": "The Hard Thing Rule", "text": "Everyone in the family must do one hard thing that requires daily deliberate practice. You can quit, but only at a natural stopping point. As kids get older, they choose their own hard thing."},
            {"title": "Grit Can Be Grown", "text": "Grit isn't fixed. You can develop it from the inside out (through interest, practice, purpose, hope) and from the outside in (through parenting, coaching, culture)."}
        ],
        "quotes": [
            "Enthusiasm is common. Endurance is rare.",
            "Our potential is one thing. What we do with it is quite another.",
            "Without effort, your talent is nothing more than unmet potential."
        ],
        "actions": [
            "Identify your top-level goal and align daily actions to it",
            "Practice deliberately on one skill for 30 minutes today",
            "Find your purpose: How does your work serve others?",
            "Reframe one setback with optimistic self-talk",
            "Commit to a 'hard thing' for at least 1 year"
        ],
        "analogies": [
            {"concept": "Grit Development", "analogy": "Like building muscle", "explanation": "You can't develop powerful muscles without lifting progressively heavier weights. Similarly, you develop grit by deliberately challenging yourself beyond current capabilities."}
        ],
        "visual_map": '''
        digraph "Grit" {
            rankdir=LR
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            talent [label="💎 TALENT\\nHow quickly\\nyou learn", fillcolor="#E8E8E8"]
            
            effort1 [label="💪 EFFORT", fillcolor="#FFE4B5"]
            
            skill [label="🎯 SKILL\\nWhat you can do", fillcolor="#98FB98"]
            
            effort2 [label="💪 EFFORT\\n(counts twice)", fillcolor="#FFE4B5"]
            
            achievement [label="🏆 ACHIEVEMENT\\nWhat you\\naccomplish", fillcolor="#FFD700"]
            
            grit [label="✨ GRIT\\nPassion + Perseverance", fillcolor="#87CEEB", shape=ellipse]
            
            talent -> effort1 -> skill
            skill -> effort2 -> achievement
            grit -> effort1 [style=dashed]
            grit -> effort2 [style=dashed]
        }
        '''
    },
    
    "Can't Hurt Me": {
        "author": "David Goggins",
        "genre": "self-help",
        "year": 2018,
        "rating": 4.8,
        "time": 19,
        "cover": "https://m.media-amazon.com/images/I/81V4nVuaAuL._SL1500_.jpg",
        "overview": "Navy SEAL Goggins shares his story of transformation from depressed, overweight young man to ultra-endurance athlete through mental toughness.",
        "executive": """**Can't Hurt Me** is David Goggins' raw account of transforming from an abused, depressed, overweight young man into a Navy SEAL, Army Ranger, and ultramarathon athlete. His philosophy: most people tap into only 40% of their capabilities.

When your mind tells you you're done, you're only at **40%** of your actual capacity. Goggins calls this the **40% Rule**. By accepting discomfort and challenging yourself daily, you can access the remaining 60%.

The book introduces the **Accountability Mirror**—confronting yourself honestly about who you are and who you want to be. Goggins advocates creating a **Cookie Jar** of past victories to draw on during difficult moments, and **Callousing Your Mind** through voluntary suffering.""",
        "framework": "The 40% Rule & Mental Toughness",
        "takeaways": [
            {"title": "The 40% Rule", "text": "When your mind is telling you you're done, you're really only 40% done. The brain protects you from discomfort. Push past this mental governor to access your full potential."},
            {"title": "The Accountability Mirror", "text": "Post-it notes on your bathroom mirror with your goals, flaws, and what you need to do. Look yourself in the eye daily and hold yourself accountable. No lies, no excuses."},
            {"title": "The Cookie Jar", "text": "A mental bank of past accomplishments. When things get hard, reach into your cookie jar and remember times you overcame challenges. Use past victories to fuel current battles."},
            {"title": "Callous Your Mind", "text": "Like callouses on hands from hard work, your mind becomes tougher through voluntary hardship. Do things you hate. Embrace suffering. Build mental armor through discomfort."},
            {"title": "Taking Souls", "text": "In any competition or challenge, break your opponent's/obstacle's will. When they think you're done and you keep going, you take their soul—their belief in their superiority."}
        ],
        "quotes": [
            "The only way you're ever going to get to the other side of this journey is by suffering. You have to suffer in order to grow.",
            "We live in a world where mediocrity is often rewarded. Don't fall into that trap.",
            "You are in danger of living a life so comfortable and soft, that you will die without ever realizing your true potential."
        ],
        "actions": [
            "Write down 10 hard truths about yourself on sticky notes",
            "Do something uncomfortable every single day",
            "Create your Cookie Jar: List 10 times you overcame challenges",
            "When you want to quit, do 40% more",
            "Take a cold shower for mental toughness training"
        ],
        "analogies": [
            {"concept": "Mental Governor", "analogy": "Like a car's rev limiter", "explanation": "Your mind is like a rev limiter that cuts engine power to protect it. The 40% Rule is recognizing this limit exists and pushing past it when appropriate—there's more power available than your brain tells you."}
        ],
        "visual_map": '''
        digraph "Can't Hurt Me" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            comfortable [label="😴 COMFORTABLE\\nThe Trap\\n40% Capacity", fillcolor="#FFB6C1"]
            
            mirror [label="🪞 ACCOUNTABILITY\\nMIRROR\\nConfront truth", fillcolor="#FFE4B5"]
            
            action [label="💪 TAKE ACTION\\nDo hard things\\nEmbrace suffering", fillcolor="#98FB98"]
            
            jar [label="🍪 COOKIE JAR\\nPast victories\\nMental fuel", fillcolor="#87CEEB"]
            
            callous [label="🛡️ CALLOUSED MIND\\nMental toughness\\n100% Capacity", fillcolor="#DDA0DD"]
            
            potential [label="🚀 TRUE POTENTIAL\\nUnstoppable", fillcolor="#FFD700"]
            
            comfortable -> mirror [label="wake up"]
            mirror -> action
            action -> jar [label="creates"]
            jar -> action [label="fuels", style=dashed]
            action -> callous
            callous -> potential
        }
        '''
    },
    
    "The Alchemist": {
        "author": "Paulo Coelho",
        "genre": "self-help",
        "year": 1988,
        "rating": 4.7,
        "time": 11,
        "cover": "https://m.media-amazon.com/images/I/71aFt4+OTOL._SL1500_.jpg",
        "overview": "An allegorical novel about a shepherd boy's journey to find treasure, discovering his Personal Legend.",
        "executive": """**The Alchemist** follows Santiago, a shepherd boy who dreams of finding treasure near the Egyptian pyramids. His journey teaches that when you want something, the entire universe conspires to help you achieve it—if you follow your **Personal Legend**.

Your **Personal Legend** is what you've always wanted to accomplish. Everyone has one, but most abandon it due to fear, comfort, or others' opinions. The book teaches to follow omens, listen to your heart, and persist despite setbacks.

Coelho introduces the **Language of the World**—a universal language spoken through signs, symbols, and the Soul of the World. When you're aligned with your Personal Legend, you can read this language and the universe supports you.""",
        "framework": "Following Your Personal Legend",
        "takeaways": [
            {"title": "Everyone Has a Personal Legend", "text": "Your Personal Legend is what you've always wanted to do. When you're young, you know it, but as you age, fear and conformity make you forget. Discovering and pursuing it is the meaning of life."},
            {"title": "The Universe Conspires to Help", "text": "When you want something with all your heart, the entire universe conspires in helping you achieve it. Coincidences, omens, and opportunities appear when you're on the right path."},
            {"title": "Read the Omens", "text": "The world speaks a universal language through signs and symbols. Learn to read these omens—they guide you toward your Personal Legend. Trust intuition over logic."},
            {"title": "The Treasure is in the Journey", "text": "Often, we discover that the treasure we sought was within us all along. The journey transforms us into who we need to be to deserve the treasure."},
            {"title": "Fear is the Main Obstacle", "text": "Fear of failure and fear of success both prevent people from living their Personal Legend. Courage means acting despite fear, not the absence of fear."}
        ],
        "quotes": [
            "When you want something, all the universe conspires in helping you to achieve it.",
            "There is only one thing that makes a dream impossible to achieve: the fear of failure.",
            "The secret of life is to fall seven times and to get up eight."
        ],
        "actions": [
            "Identify your Personal Legend: What do you truly want?",
            "Notice one omen or sign today and follow it",
            "Take the first step toward your dream, no matter how small",
            "List three fears holding you back and face one",
            "Listen to your heart for 5 minutes in silence"
        ],
        "analogies": [
            {"concept": "Personal Legend", "analogy": "Like a compass pointing north", "explanation": "Your Personal Legend is your internal compass, constantly pulling you toward your true purpose. Ignore it and you'll feel lost; follow it and everything aligns."}
        ],
        "visual_map": '''
        digraph "The Alchemist" {
            rankdir=LR
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            dream [label="💭 THE DREAM\\nYour calling", fillcolor="#E8E8E8"]
            
            obstacles [label="⚠️ OBSTACLES\\nFear\\nComfort\\nOthers' opinions", fillcolor="#FFB6C1"]
            
            omens [label="🔮 OMENS\\nSigns\\nIntuition\\nCoincidences", fillcolor="#FFE4B5"]
            
            journey [label="🚶 THE JOURNEY\\nTransformation\\nLearning\\nGrowth", fillcolor="#98FB98"]
            
            legend [label="⭐ PERSONAL\\nLEGEND\\nYour destiny", fillcolor="#87CEEB"]
            
            treasure [label="💎 THE TREASURE\\nWithin you\\nall along", fillcolor="#FFD700"]
            
            dream -> obstacles
            obstacles -> omens [label="overcome\\nwith", style=dashed]
            omens -> journey
            journey -> legend
            legend -> treasure
        }
        '''
    },
    
    "Good to Great": {
        "author": "Jim Collins",
        "genre": "business",
        "year": 2001,
        "rating": 4.6,
        "time": 18,
        "cover": "https://m.media-amazon.com/images/I/61YfNZDzUWL._SL1500_.jpg",
        "overview": "Collins reveals why some companies make the leap to greatness while others don't, based on rigorous 5-year research.",
        "executive": """**Good to Great** identifies what distinguishes great companies from merely good ones. Through 5 years of research comparing 11 great companies to direct competitors, Collins discovered sustainable greatness follows a pattern.

**Level 5 Leadership** combines personal humility with professional will. These leaders channel ambition into the company, not themselves. They're self-effacing yet driven, modest yet results-oriented.

The **Hedgehog Concept** comes from focusing on the intersection of three circles: 1) What you can be best in the world at, 2) What drives your economic engine, 3) What you're deeply passionate about. Companies that found their Hedgehog Concept and stuck to it achieved greatness.""",
        "framework": "The Flywheel & Hedgehog Concept",
        "takeaways": [
            {"title": "Level 5 Leadership", "text": "Level 5 leaders are modest, self-effacing, understated—yet driven, ambitious for the company (not themselves). They display a paradoxical blend of personal humility and professional will."},
            {"title": "First Who, Then What", "text": "Get the right people on the bus, the wrong people off, and the right people in the right seats BEFORE deciding where to drive. Great vision without great people is irrelevant."},
            {"title": "The Hedgehog Concept", "text": "Greatness comes from focusing on the intersection of: 1) What you can be best at (not just good at), 2) What drives your economic engine, 3) What you're passionate about. Find this sweet spot."},
            {"title": "The Flywheel Effect", "text": "Greatness is not a single event but a process. Push the flywheel consistently in one direction. Momentum builds slowly, then suddenly, but only with persistent effort aligned with the Hedgehog Concept."},
            {"title": "Confront the Brutal Facts", "text": "Maintain unwavering faith that you can prevail (Stockdale Paradox) while simultaneously confronting the most brutal facts of your current reality. Never lose faith, and never ignore facts."}
        ],
        "quotes": [
            "Good is the enemy of great.",
            "Level 5 leaders channel their ego needs away from themselves and into the larger goal of building a great company.",
            "Greatness is not primarily a matter of circumstance; it is first and foremost a matter of conscious choice."
        ],
        "actions": [
            "Assess: Are you a Level 5 leader? (Humble + Driven for company)",
            "Audit your team: Right people on the bus?",
            "Define your Hedgehog Concept across the three circles",
            "Identify one brutal fact you've been avoiding",
            "Push your flywheel: What consistent action builds momentum?"
        ],
        "analogies": [
            {"concept": "The Flywheel", "analogy": "Like pushing a massive wheel", "explanation": "At first, pushing a 5,000-pound flywheel is exhausting with little movement. But persistent pushing builds momentum. Eventually it spins on its own—dramatic results from cumulative effort, not one push."}
        ],
        "visual_map": '''
        digraph "Good to Great" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            level5 [label="LEVEL 5\\nLEADERSHIP\\nHumility + Will", fillcolor="#E8E8E8"]
            
            who [label="FIRST WHO\\nRight people\\non the bus", fillcolor="#FFE4B5"]
            
            facts [label="BRUTAL FACTS\\nConfront reality\\n+ Keep faith", fillcolor="#FFB6C1"]
            
            hedgehog [label="🦔 HEDGEHOG\\nCONCEPT", fillcolor="#87CEEB", shape=ellipse]
            
            best [label="Best at", fillcolor="#98FB98"]
            passion [label="Passionate\\nabout", fillcolor="#DDA0DD"]
            economic [label="Economic\\nengine", fillcolor="#F0E68C"]
            
            flywheel [label="FLYWHEEL\\nMomentum builds", fillcolor="#98FB98"]
            
            great [label="🏆 GREATNESS\\nSustainable", fillcolor="#FFD700"]
            
            level5 -> who -> facts -> hedgehog
            hedgehog -> best
            hedgehog -> passion
            hedgehog -> economic
            best -> flywheel
            passion -> flywheel
            economic -> flywheel
            flywheel -> great
        }
        '''
    },
    
    "Zero to One": {
        "author": "Peter Thiel",
        "genre": "business",
        "year": 2014,
        "rating": 4.7,
        "time": 14,
        "cover": "https://m.media-amazon.com/images/I/71uAI28kJuL._SL1500_.jpg",
        "overview": "Thiel argues that true innovation means going from zero to one—creating something entirely new, not copying what works.",
        "executive": """**Zero to One** presents Peter Thiel's contrarian philosophy of innovation and startups. **Going from 0 → 1** means creating something new (vertical progress, technology). **Going from 1 → n** means copying what works (horizontal progress, globalization).

Thiel argues that competition is for losers. The best businesses are **monopolies**—not by cheating but by being so good at something unique that no one else can offer a close substitute. Monopolies can focus on employees, products, and impact on the world.

The book introduces the **Power Law**—in venture capital and startups, a small number of companies vastly outperform all others. Don't diversify; find the one thing that will work better than anything else and focus on it.""",
        "framework": "0 → 1: Creating the New",
        "takeaways": [
            {"title": "Zero to One vs One to N", "text": "Horizontal progress (1→n) is copying things that work—globalization. Vertical progress (0→1) is creating new things—technology. The future comes from vertical progress, not copying."},
            {"title": "Competition is for Losers", "text": "Perfect competition drives profits to zero. Creative monopoly—being uniquely good at something—lets you set prices, focus on non-monetary goals, and think long-term. Aim for monopoly, not competition."},
            {"title": "The Power Law", "text": "A small handful of companies vastly outperform all others. In VC, one investment often returns more than all others combined. Focus on the few things that will matter most, not diversification."},
            {"title": "Secrets: What Truths Do Few Believe?", "text": "Great companies are built on secrets—important truths unknown to most. Ask: What valuable company is nobody building? What do you believe that others think is crazy?"},
            {"title": "The Seven Questions", "text": "Every startup must answer: Engineering (10x better?), Timing (right now?), Monopoly (small market to dominate?), People (right team?), Distribution (path to customers?), Durability (10-20 year position?), Secret (unique opportunity?)."}
        ],
        "quotes": [
            "The best entrepreneurs know: every great business is built around a secret that's hidden from the outside.",
            "Competition is for losers.",
            "The most valuable businesses of coming decades will be built by entrepreneurs who seek to empower people rather than try to make them obsolete."
        ],
        "actions": [
            "Identify one secret/truth that few believe but you know is true",
            "Find a small market you can monopolize, not a large competitive one",
            "Focus: What one thing, if successful, makes everything else easier?",
            "Ask: Are you creating something 10x better, or copying?",
            "Answer the 7 questions for your venture/project"
        ],
        "analogies": [
            {"concept": "0→1 vs 1→n", "analogy": "Like invention vs production", "explanation": "Going 1→n is like building more factories to make more of the same product (horizontal). Going 0→1 is like inventing the product in the first place (vertical). Both have value, but only 0→1 creates the future."}
        ],
        "visual_map": '''
        digraph "Zero to One" {
            rankdir=LR
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            zero [label="0", fillcolor="#E8E8E8", shape=circle, fontsize=20]
            
            secret [label="🔐 SECRET\\nHidden truth\\nFew believe", fillcolor="#FFE4B5"]
            
            monopoly [label="👑 MONOPOLY\\nUniquely good\\nNo substitute\\n10x better", fillcolor="#87CEEB"]
            
            one [label="1", fillcolor="#98FB98", shape=circle, fontsize=20]
            
            value [label="💎 MASSIVE\\nVALUE\\nPower law\\nwinner", fillcolor="#FFD700"]
            
            competition [label="⚔️ COMPETITION\\n1→n copying\\nPerfect competition\\nZero profit", fillcolor="#FFB6C1"]
            
            mediocre [label="Mediocre\\noutcome", fillcolor="#CCCCCC"]
            
            zero -> secret [label="vertical\\nprogress", style=bold]
            secret -> monopoly
            monopoly -> one
            one -> value
            
            zero -> competition [label="horizontal\\nprogress", style=dashed]
            competition -> mediocre
        }
        '''
    }
}
