"""
World-Class Content Database
Contains refined, expert-level summaries for top books.
"""

books_data = [
    # ==================== SELF-HELP ====================
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "self-help",
        "year": 2018,
        "cover": "https://m.media-amazon.com/images/I/81F90H7hnML._SL1500_.jpg",
        "rating": 4.9,
        "time": 18,
        "quote": "You do not rise to the level of your goals. You fall to the level of your systems.",
        "overview": "A comprehensive framework for improving every day by building good habits and breaking bad ones.",
        "executive": """**Atomic Habits** is the definitive guide to breaking bad behaviors and adopting good ones in four steps, showing that small, incremental everyday routines compound into massive, positive change over time.

James Clear argues that the problem isn't you; it's your system. Bad habits repeat themselves not because you don't want to change, but because you have the wrong system for change. This book focuses on the mechanics of habit formation: steps you can take to build good habits and break bad ones.""",
        "takeaways": [
            {"title": "The 1% Rule", "text": "Improving by just 1% every day results in being 37x better by the end of the year."},
            {"title": "Identity-Based Habits", "text": "Focus on who you wish to become, not just what you want to achieve. True behavior change is identity change."},
            {"title": "Systems > Goals", "text": "Winners and losers have the same goals. The difference is the system they implement to achieve them."}
        ],
        "actions": [
            "Use the 2-Minute Rule to start new habits",
            "Stack new habits onto existing ones (Habit Stacking)",
            "Design your environment to make cues obvious"
        ]
    },
    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "genre": "self-help",
        "year": 1989,
        "cover": "https://m.media-amazon.com/images/I/81MYMV9r7OL._SL1500_.jpg",
        "rating": 4.8,
        "time": 25,
        "quote": "Sow a thought, reap an action; sow an action, reap a habit; sow a habit, reap a character; sow a character, reap a destiny.",
        "overview": "A holistic approach to personal and professional effectiveness based on timeless principles.",
        "executive": """**The 7 Habits of Highly Effective People** presents an approach to being effective in attaining goals by aligning oneself to what Covey calls "true north" principles based on a character ethic that he presents as universal and timeless.

It moves from dependence to independence to interdependence. The first three habits surround moving from dependence to independence (Private Victory), and the next three surround moving to interdependence (Public Victory).""",
        "takeaways": [
            {"title": "Be Proactive", "text": "Take responsibility for your life. You are the programmer, not the program."},
            {"title": "Begin with the End in Mind", "text": "Define your mission and goals in life. All things are created twice: first mentally, then physically."},
            {"title": "Put First Things First", "text": "Prioritize what is important, not just what is urgent. Use the Eisenhower Matrix."}
        ],
        "actions": [
            "Draft a personal mission statement",
            "Identify your key roles in life and goals for each",
            "Practice empathetic listening"
        ]
    },
    {
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "genre": "self-help",
        "year": 1936,
        "cover": "https://m.media-amazon.com/images/I/71vK0WVQ4rL._SL1500_.jpg",
        "rating": 4.8,
        "time": 15,
        "quote": "You can make more friends in two months by becoming interested in other people than you can in two years by trying to get other people interested in you.",
        "overview": "The classic guide to improving social skills, communication, and influence.",
        "executive": """A timeless bestseller, **How to Win Friends and Influence People** teaches you how to handle people, win them over to your way of thinking, and change them without giving offense or arousing resentment.

Carnegie's core philosophy is that success is due 15% to professional knowledge and 85% to the ability to express ideas, to assume leadership, and to arouse enthusiasm among people.""",
        "takeaways": [
            {"title": "Don't Criticize", "text": "Criticism is futile because it puts a person on the defensive and usually makes them strive to justify themselves."},
            {"title": "Give Honest Appreciation", "text": "The deepest principle in human nature is the craving to be appreciated."},
            {"title": "Become Genuinely Interested", "text": "The only way to make a friend is to be one. Show genuine interest in others' lives."}
        ],
        "actions": [
            "Smile more often (it's the simplest way to make a good impression)",
            "Remember and use people's names",
            "Listen longer than you speak"
        ]
    },

    # ==================== BUSINESS ====================
    {
        "title": "Good to Great",
        "author": "Jim Collins",
        "genre": "business",
        "year": 2001,
        "cover": "https://m.media-amazon.com/images/I/61YfNZDzUWL._SL1500_.jpg",
        "rating": 4.6,
        "time": 16,
        "quote": "Good is the enemy of great.",
        "overview": "Why some companies make the leap ... and others don't.",
        "executive": """Based on a five-year research project, **Good to Great** identifies seven characteristics of companies that went from good to great. 

Collins argues that greatness is not a function of circumstance but largely a matter of conscious choice and discipline. The book introduces concepts like Level 5 Leadership, First Who... Then What, and the Hedgehog Concept.""",
        "takeaways": [
            {"title": "Level 5 Leadership", "text": "Great leaders display a powerful mixture of personal humility and indomitable will."},
            {"title": "The Hedgehog Concept", "text": "Focus on the intersection of what you are deeply passionate about, what you can be the best in the world at, and what drives your economic engine."},
            {"title": "First Who, Then What", "text": "Get the right people on the bus (and the wrong people off) before you figure out where to drive it."}
        ],
        "actions": [
            "Confront the brutal facts of your reality",
            "Identify your personal 'Hedgehog Concept'",
            "Practice disciplined thought and action"
        ]
    },
    {
        "title": "Zero to One",
        "author": "Peter Thiel",
        "genre": "business",
        "year": 2014,
        "cover": "https://m.media-amazon.com/images/I/71uAI28kJuL._SL1500_.jpg",
        "rating": 4.7,
        "time": 12,
        "quote": "The most important question is: What important truth do very few people agree with you on?",
        "overview": "Notes on startups, or how to build the future.",
        "executive": """**Zero to One** presents a philosophy of entrepreneurship. Thiel argues that progress comes from monopoly, not competition. If you do what has never been done and can do it better than anyone else, you have a monopoly - and every business is successful exactly to the extent that it does something others cannot.

Going from 0 to 1 means creating something entirely new (vertical progress), whereas going from 1 to n means adding more of something familiar (horizontal progress).""",
        "takeaways": [
            {"title": "Competition is for Losers", "text": "Under perfect competition, no one makes a profit. Monopolies drive progress and generate wealth."},
            {"title": "The Power Law", "text": "In venture capital, a few companies attain exponentially greater value than all others combined."},
            {"title": "Secrets", "text": "Great businesses are built on secrets—truths about the world that others don't see."}
        ],
        "actions": [
            "Identify a niche small enough to dominate",
            "Focus on sales as much as product",
            "Build a strong culture from day one"
        ]
    },

    # ==================== PSYCHOLOGY ====================
    {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "genre": "psychology",
        "year": 2011,
        "cover": "https://m.media-amazon.com/images/I/61fdrEuPJwL._SL1500_.jpg",
        "rating": 4.6,
        "time": 20,
        "quote": "Nothing in life is as important as you think it is, while you are thinking about it.",
        "overview": "A groundbreaking tour of the mind and the two systems that drive the way we think.",
        "executive": """Nobel laureate Daniel Kahneman explains the two systems that drive the way we think. **System 1** is fast, intuitive, and emotional; **System 2** is slower, more deliberative, and more logical.

The book reveals where we can and cannot trust our intuitions and how we can tap into the benefits of slow thinking. It offers practical and enlightening insights into how choices are made in both our business and our personal lives.""",
        "takeaways": [
            {"title": "Two Systems", "text": "We have two modes of thought: System 1 (Fast/Auto) and System 2 (Slow/Effortful). Mistakes often happen when System 1 acts where System 2 should."},
            {"title": "Loss Aversion", "text": "We fear losing $100 more than we value winning $100. Losses loom larger than gains."},
            {"title": "The Availability Heuristic", "text": "We judge the likelihood of events based on how easily examples come to mind, not statistical probability."}
        ],
        "actions": [
            "Pause when making high-stakes decisions",
            "Be aware of 'anchoring' in negotiations",
            "Pre-mortem: Imagine a project failed and ask why"
        ]
    },
    {
        "title": "Influence: The Psychology of Persuasion",
        "author": "Robert B. Cialdini",
        "genre": "psychology",
        "year": 1984,
        "cover": "https://m.media-amazon.com/images/I/71HZyYT+PEL._SL1500_.jpg",
        "rating": 4.8,
        "time": 14,
        "quote": "We all fool ourselves from time to time in order to keep our thoughts and beliefs consistent with what we have already done or decided.",
        "overview": "The classic book on persuasion, explaining the psychology of why people say 'yes'.",
        "executive": """Cialdini explains the six universal principles of influence, learned from decades of research and undercover work. These weapons of influence are useful for persuasion but can also be used against us.

Understanding these principles—**Reciprocity, Commitment, Social Proof, Authority, Liking, and Scarcity**—is essential for anyone who wants to persuade others or defend themselves against manipulation.""",
        "takeaways": [
            {"title": "Reciprocity", "text": "People feel obliged to give back to others who have given to them."},
            {"title": "Social Proof", "text": "We view a behavior as more correct in a given situation to the degree that we see others performing it."},
            {"title": "Scarcity", "text": "Opportunities seem more valuable to us when their availability is limited."}
        ],
        "actions": [
            "Use 'because' when making requests",
            "Give small gifts or concessions first",
            "Highlight what people stand to lose, not just gain"
        ]
    },

    # ==================== FINANCE ====================
    {
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "genre": "finance",
        "year": 2020,
        "cover": "https://m.media-amazon.com/images/I/715k1M+oWLL._SL1500_.jpg",
        "rating": 4.8,
        "time": 12,
        "quote": "Doing well with money has a little to do with how smart you are and a lot to do with how you behave.",
        "overview": "Timeless lessons on wealth, greed, and happiness.",
        "executive": """Doing well with money isn't necessarily about what you know. It's about how you behave. And behavior is hard to teach, even to really smart people.

Morgan Housel shares 19 short stories exploring the strange ways people think about money and teaches you how to make better sense of one of life's most important topics. He differentiates between getting wealthy (risk, optimism) and staying wealthy (humility, fear).""",
        "takeaways": [
            {"title": "Compounding", "text": "Warren Buffett's net worth is largely due to the fact that he's been investing since he was a child. Time is the most powerful force."},
            {"title": "Getting vs Staying Wealthy", "text": "Getting money requires taking risks. Staying wealthy requires avoiding ruin."},
            {"title": "Freedom", "text": "The highest dividend money pays is the ability to control your time."}
        ],
        "actions": [
            "Increase your savings rate",
            "Define your 'enough'",
            "Focus on survival/longevity in the market"
        ]
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "genre": "finance",
        "year": 1997,
        "cover": "https://m.media-amazon.com/images/I/81bsw6fnUiL._SL1500_.jpg",
        "rating": 4.7,
        "time": 10,
        "quote": "The poor and the middle class work for money. The rich have money work for them.",
        "overview": "What the rich teach their kids about money that the poor and middle class do not!",
        "executive": """**Rich Dad Poor Dad** tells the story of Robert Kiyosaki and his two dads—his real father (poor dad) and the father of his best friend (rich dad)—and the ways in which both men shaped his thoughts about money and investing.

The book explodes the myth that you need to earn a high income to become rich and explains the difference between working for money and having your money work for you.""",
        "takeaways": [
            {"title": "Assets vs Liabilities", "text": "An asset puts money in your pocket. A liability takes money out of your pocket. Know the difference."},
            {"title": "Financial Literacy", "text": "Intelligence solves problems and produces money. Money without financial intelligence is money soon gone."},
            {"title": "Mind Your Own Business", "text": "Keep your day job, but start buying real assets, not liabilities or personal effects."}
        ],
        "actions": [
            "Reduce personal liabilities",
            "Acquire income-generating assets",
            "Learn about taxes and corporate structures"
        ]
    }
]
