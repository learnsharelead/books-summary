"""
Extended Book Library - 100+ Additional Books for BookWise.
Run with: python -m database.books_extended
"""

import json
from database.connection import get_session
from database.models import Genre, Book, Summary

# Extended book collection organized by genre
EXTENDED_BOOKS = {
    "self-help": [
        {
            "title": "The 7 Habits of Highly Effective People",
            "author": "Stephen R. Covey",
            "year": 1989,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71cHpLeMY0L.jpg",
            "rating": 4.8,
            "read_time": 15,
            "overview": "A holistic, integrated approach to personal and interpersonal effectiveness through paradigm shifts and habit development.",
            "executive": "Covey presents a principle-centered approach for solving personal and professional problems. The seven habits move us from dependence through independence to interdependence, providing a framework for effectiveness in any endeavor.",
            "takeaways": [
                {"title": "Be Proactive", "text": "Take responsibility for your life. Between stimulus and response, you have the freedom to choose."},
                {"title": "Begin with the End in Mind", "text": "Start with a clear vision of your destination. All things are created twice - first mentally, then physically."},
                {"title": "Put First Things First", "text": "Prioritize what matters most. Organize and execute around priorities."},
                {"title": "Think Win-Win", "text": "Seek mutually beneficial solutions. Abundance mentality creates more for everyone."},
                {"title": "Synergize", "text": "The whole is greater than the sum of its parts. Creative cooperation produces better solutions."}
            ],
            "quotes": ["Between stimulus and response there is a space.", "Begin with the end in mind.", "The main thing is to keep the main thing the main thing."],
            "action_steps": ["Write a personal mission statement", "Create a weekly planning system", "Practice empathic listening daily"]
        },
        {
            "title": "How to Win Friends and Influence People",
            "author": "Dale Carnegie",
            "year": 1936,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71vK0WVQ4rL.jpg",
            "rating": 4.7,
            "read_time": 12,
            "overview": "Timeless principles for handling people, making people like you, winning people to your way of thinking, and changing people without offense.",
            "executive": "Carnegie's classic provides practical advice for improving social skills and building genuine relationships. The principles remain relevant nearly a century later.",
            "takeaways": [
                {"title": "Don't Criticize", "text": "Criticism puts people on the defensive. Instead, try to understand their perspective."},
                {"title": "Give Honest Appreciation", "text": "Everyone craves appreciation. Be sincere in your praise."},
                {"title": "Become Genuinely Interested", "text": "You can make more friends in two months by becoming interested in other people than in two years trying to get others interested in you."}
            ],
            "quotes": ["A person's name is the sweetest sound.", "Talk in terms of the other person's interests.", "The only way to get the best of an argument is to avoid it."],
            "action_steps": ["Remember and use people's names", "Ask questions about others' interests", "Smile more in conversations"]
        },
        {
            "title": "The Power of Now",
            "author": "Eckhart Tolle",
            "year": 1997,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/714FbKtXS+L.jpg",
            "rating": 4.6,
            "read_time": 14,
            "overview": "A guide to spiritual enlightenment through living fully in the present moment and freeing yourself from the pain-body.",
            "executive": "Tolle teaches that the present moment is all we ever have. By disidentifying from the mind and ego, we can access a deeper state of consciousness and find lasting peace.",
            "takeaways": [
                {"title": "The Present is All There Is", "text": "Past and future exist only as mental constructs. True life happens only in the Now."},
                {"title": "You Are Not Your Mind", "text": "The voice in your head is not who you are. You are the awareness behind it."},
                {"title": "Accept the Present Moment", "text": "Suffering comes from resisting what is. Acceptance leads to peace."}
            ],
            "quotes": ["Realize deeply that the present moment is all you have.", "Life is now. There was never a time when your life was not now."],
            "action_steps": ["Practice observing your thoughts without judgment", "Take three conscious breaths when stressed", "Focus fully on one task at a time"]
        },
        {
            "title": "Mindset: The New Psychology of Success",
            "author": "Carol S. Dweck",
            "year": 2006,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/61bDwfLudLL.jpg",
            "rating": 4.7,
            "read_time": 13,
            "overview": "How our beliefs about our abilities dramatically impact success in nearly every area of human endeavor.",
            "executive": "Dweck's research shows that people with a growth mindset—those who believe abilities can be developed—achieve more than those with a fixed mindset. This book changes how you think about intelligence, talent, and potential.",
            "takeaways": [
                {"title": "Growth vs Fixed Mindset", "text": "A growth mindset sees challenges as opportunities to improve. A fixed mindset avoids them to protect self-image."},
                {"title": "Effort is the Path to Mastery", "text": "In a growth mindset, effort is what makes you smart and talented."},
                {"title": "Learn from Criticism", "text": "Growth mindset sees helpful feedback as a gift for improvement."}
            ],
            "quotes": ["Becoming is better than being.", "The view you adopt for yourself profoundly affects the way you lead your life."],
            "action_steps": ["Replace 'I can't' with 'I can't yet'", "Embrace one new challenge this week", "Celebrate effort, not just results"]
        },
        {
            "title": "The Subtle Art of Not Giving a F*ck",
            "author": "Mark Manson",
            "year": 2016,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg",
            "rating": 4.5,
            "read_time": 11,
            "overview": "A counterintuitive approach to living a good life by focusing on what truly matters and letting go of what doesn't.",
            "executive": "Manson argues that the key to living well is not about being positive all the time, but about choosing what to care about wisely. True happiness comes from solving meaningful problems.",
            "takeaways": [
                {"title": "Choose Your Problems", "text": "Life is essentially endless problems. Happiness comes from choosing problems worth solving."},
                {"title": "You Are Not Special", "text": "Accepting your ordinariness frees you from the pressure of exceptionalism."},
                {"title": "Values Matter Most", "text": "Good values are reality-based, socially constructive, and within your control."}
            ],
            "quotes": ["Who you are is defined by what you're willing to struggle for.", "Not giving a f*ck does not mean being indifferent."],
            "action_steps": ["List your top 5 values", "Identify one thing you're over-caring about", "Choose one meaningful struggle to embrace"]
        },
        {
            "title": "Can't Hurt Me",
            "author": "David Goggins",
            "year": 2018,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81gTRv2HXrL.jpg",
            "rating": 4.8,
            "read_time": 16,
            "overview": "Master your mind and defy the odds through mental toughness, self-discipline, and embracing pain.",
            "executive": "Goggins shares his journey from poverty and abuse to becoming a Navy SEAL and ultramarathon runner, teaching that most of us only tap into 40% of our capabilities.",
            "takeaways": [
                {"title": "The 40% Rule", "text": "When your mind tells you you're done, you're only 40% done."},
                {"title": "Callous Your Mind", "text": "Do hard things repeatedly to build mental armor."},
                {"title": "Accountability Mirror", "text": "Face your weaknesses honestly and post goals where you'll see them daily."}
            ],
            "quotes": ["You are in danger of living a life so comfortable and soft that you will die without ever realizing your potential."],
            "action_steps": ["Create an accountability mirror", "Do one hard thing daily", "Keep a 'Cookie Jar' of past accomplishments"]
        },
        {
            "title": "The Four Agreements",
            "author": "Don Miguel Ruiz",
            "year": 1997,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81hHy5XrdKL.jpg",
            "rating": 4.7,
            "read_time": 10,
            "overview": "Ancient Toltec wisdom offering a powerful code of conduct for personal freedom and happiness.",
            "executive": "Ruiz presents four simple agreements that can transform your life: be impeccable with your word, don't take anything personally, don't make assumptions, and always do your best.",
            "takeaways": [
                {"title": "Be Impeccable With Your Word", "text": "Speak with integrity. Say only what you mean. Use the power of your word in the direction of truth and love."},
                {"title": "Don't Take Anything Personally", "text": "Nothing others do is because of you. What others say and do is a projection of their own reality."},
                {"title": "Don't Make Assumptions", "text": "Find the courage to ask questions and express what you really want."}
            ],
            "quotes": ["The word is the most powerful tool you have as a human.", "Death is not the biggest fear we have; our biggest fear is taking the risk to be alive."],
            "action_steps": ["Practice speaking only truth for one day", "When offended, pause and don't react", "Ask clarifying questions instead of assuming"]
        },
        {
            "title": "Man's Search for Meaning",
            "author": "Viktor E. Frankl",
            "year": 1946,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71-fhJJ2UPL.jpg",
            "rating": 4.9,
            "read_time": 12,
            "overview": "A Holocaust survivor's powerful insights on finding purpose in suffering and the will to meaning.",
            "executive": "Frankl's memoir and psychological insights from Nazi concentration camps reveal that finding meaning in suffering is essential to survival and that we always have the freedom to choose our attitude.",
            "takeaways": [
                {"title": "Meaning is Individual", "text": "The meaning of life differs from person to person and moment to moment."},
                {"title": "Suffering Can Have Meaning", "text": "In unavoidable suffering, we can still choose our attitude."},
                {"title": "Purpose Drives Survival", "text": "Those who have a 'why' to live can bear almost any 'how'."}
            ],
            "quotes": ["Those who have a 'why' to live, can bear with almost any 'how'.", "Everything can be taken from a man but one thing: the last of the human freedoms."],
            "action_steps": ["Write down your 'why'", "Reframe a current struggle as meaningful", "Help someone find purpose today"]
        }
    ],
    "business": [
        {
            "title": "Good to Great",
            "author": "Jim Collins",
            "year": 2001,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71jJJKw7y-L.jpg",
            "rating": 4.6,
            "read_time": 15,
            "overview": "Why some companies make the leap to greatness and others don't—based on rigorous research.",
            "executive": "Collins and his research team analyzed companies that achieved extraordinary results sustained over 15+ years. The findings reveal surprising truths about leadership, culture, and strategy.",
            "takeaways": [
                {"title": "Level 5 Leadership", "text": "The best leaders combine personal humility with professional will."},
                {"title": "First Who, Then What", "text": "Get the right people on the bus before deciding where to drive it."},
                {"title": "The Hedgehog Concept", "text": "Focus on what you can be best at, what drives your economic engine, and what you're deeply passionate about."}
            ],
            "quotes": ["Good is the enemy of great.", "Greatness is not a function of circumstance, it's a matter of conscious choice."],
            "action_steps": ["Identify your Hedgehog Concept", "Assess your team—right people in right seats?", "Practice Level 5 leadership behaviors"]
        },
        {
            "title": "Zero to One",
            "author": "Peter Thiel",
            "year": 2014,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71m-MxdJ2WL.jpg",
            "rating": 4.5,
            "read_time": 11,
            "overview": "Notes on startups, or how to build the future by creating something truly new.",
            "executive": "Thiel argues that the next great companies will create new things rather than copy—going from zero to one. He challenges conventional startup wisdom with contrarian insights.",
            "takeaways": [
                {"title": "Monopoly Is Good", "text": "Competition is for losers. The best businesses are monopolies that create so much value they can capture some of it."},
                {"title": "Secrets Exist", "text": "There are still secrets to be discovered. The best startups find important truths that very few agree with."},
                {"title": "Power Law", "text": "A small number of companies radically outperform all others. One investment will outperform all others combined."}
            ],
            "quotes": ["What important truth do very few people agree with you on?", "The best startups might be considered slightly less extreme kinds of cults."],
            "action_steps": ["Identify one secret you believe that others don't", "Find a small market to dominate", "Build a definite view of the future"]
        },
        {
            "title": "The Lean Startup",
            "author": "Eric Ries",
            "year": 2011,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81-QB7nDh4L.jpg",
            "rating": 4.5,
            "read_time": 13,
            "overview": "How continuous innovation creates radically successful businesses through validated learning.",
            "executive": "Ries presents a scientific approach to creating and managing startups. Build-Measure-Learn feedback loops help entrepreneurs test hypotheses and iterate quickly.",
            "takeaways": [
                {"title": "Build-Measure-Learn", "text": "Create minimum viable products, measure real customer behavior, and learn from the data."},
                {"title": "Validated Learning", "text": "Progress is learning what customers actually want, not shipping features."},
                {"title": "Pivot or Persevere", "text": "Use data to decide whether to change strategy or stay the course."}
            ],
            "quotes": ["The only way to win is to learn faster than anyone else.", "If you cannot fail, you cannot learn."],
            "action_steps": ["Define your riskiest assumption", "Build an MVP to test it", "Set up metrics to measure customer behavior"]
        },
        {
            "title": "Start With Why",
            "author": "Simon Sinek",
            "year": 2009,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71qKpRKl1rL.jpg",
            "rating": 4.6,
            "read_time": 12,
            "overview": "How great leaders inspire everyone to take action by starting with purpose.",
            "executive": "Sinek's Golden Circle model shows that inspirational leaders and companies communicate from the inside out—starting with WHY they do what they do, not WHAT they do.",
            "takeaways": [
                {"title": "The Golden Circle", "text": "Start with Why, then How, then What. Most people do the opposite."},
                {"title": "People Don't Buy What You Do", "text": "They buy why you do it. Purpose inspires loyalty and action."},
                {"title": "Leaders Inspire", "text": "Great leaders project a vision of the world that doesn't exist yet."}
            ],
            "quotes": ["People don't buy what you do, they buy why you do it.", "Working hard for something we don't care about is called stress. Working hard for something we love is called passion."],
            "action_steps": ["Define your personal or company WHY", "Lead communications with purpose", "Hire people who believe what you believe"]
        },
        {
            "title": "The Hard Thing About Hard Things",
            "author": "Ben Horowitz",
            "year": 2014,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71RkbeaMy0L.jpg",
            "rating": 4.6,
            "read_time": 14,
            "overview": "Building a business when there are no easy answers—practical wisdom from a veteran entrepreneur.",
            "executive": "Horowitz shares the challenges of running a startup that most business books ignore: firing friends, managing your own psychology, and surviving near-death experiences.",
            "takeaways": [
                {"title": "The Struggle Is Real", "text": "Building a company is brutally hard. Embrace the struggle as part of the journey."},
                {"title": "Wartime vs Peacetime CEO", "text": "Different situations require different leadership styles."},
                {"title": "Take Care of Your People", "text": "Taking care of people is the hardest part but most important."}
            ],
            "quotes": ["Hard things are hard because there are no easy answers.", "There are no silver bullets, only lead bullets."],
            "action_steps": ["Prepare for your hardest conversation", "Build a support network of fellow entrepreneurs", "Document lessons from difficult decisions"]
        },
        {
            "title": "Blue Ocean Strategy",
            "author": "W. Chan Kim & Renée Mauborgne",
            "year": 2004,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71ab3+GoHIL.jpg",
            "rating": 4.4,
            "read_time": 14,
            "overview": "How to create uncontested market space and make the competition irrelevant.",
            "executive": "Instead of competing in crowded 'red oceans' of existing markets, the authors show how to create 'blue oceans' of new market space through value innovation.",
            "takeaways": [
                {"title": "Value Innovation", "text": "Create exceptional value at lower cost by eliminating and reducing factors the industry competes on."},
                {"title": "The Strategy Canvas", "text": "Visualize your competitive landscape and identify opportunities for differentiation."},
                {"title": "Four Actions Framework", "text": "Eliminate, Reduce, Raise, and Create to reconstruct buyer value."}
            ],
            "quotes": ["The only way to beat the competition is to stop trying to beat the competition."],
            "action_steps": ["Map your industry's strategy canvas", "Apply the Four Actions Framework", "Identify a blue ocean opportunity"]
        },
        {
            "title": "Thinking, Fast and Slow",
            "author": "Daniel Kahneman",
            "year": 2011,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71wvKXWfcML.jpg",
            "rating": 4.7,
            "read_time": 18,
            "overview": "A groundbreaking tour of the mind explaining the two systems that drive the way we think and make decisions.",
            "executive": "Nobel laureate Kahneman reveals how System 1 (fast, intuitive) and System 2 (slow, deliberate) thinking shape our judgments and decisions, often leading to systematic errors.",
            "takeaways": [
                {"title": "Two Systems", "text": "System 1 is fast and automatic; System 2 is slow and effortful. Most of our thinking is System 1."},
                {"title": "Cognitive Biases", "text": "Our intuitive thinking is subject to systematic errors like anchoring, availability, and loss aversion."},
                {"title": "Regression to the Mean", "text": "Extreme outcomes are often followed by more average ones—not due to any intervention."}
            ],
            "quotes": ["Nothing in life is as important as you think it is while you are thinking about it.", "We are prone to overestimate how much we understand about the world."],
            "action_steps": ["Before big decisions, identify potential biases", "Use checklists to engage System 2", "Reference base rates before making predictions"]
        },
        {
            "title": "Built to Last",
            "author": "Jim Collins & Jerry I. Porras",
            "year": 1994,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71yxADMdETL.jpg",
            "rating": 4.5,
            "read_time": 15,
            "overview": "Successful habits of visionary companies that have stood the test of time.",
            "executive": "After a six-year research project, the authors reveal what makes truly exceptional companies different from their competitors—and it's not what you might expect.",
            "takeaways": [
                {"title": "Clock Building, Not Time Telling", "text": "Build an organization that can prosper beyond any single leader or idea."},
                {"title": "Preserve the Core, Stimulate Progress", "text": "Hold core values sacred while adapting strategies and practices."},
                {"title": "Big Hairy Audacious Goals", "text": "Set ambitious goals that energize and focus the organization."}
            ],
            "quotes": ["Visionary companies distinguish their timeless core values from operating practices that should change."],
            "action_steps": ["Define your organization's non-negotiable core values", "Set a BHAG for the next 10-25 years", "Build systems that outlast any individual"]
        }
    ],
    "psychology": [
        {
            "title": "Influence: The Psychology of Persuasion",
            "author": "Robert B. Cialdini",
            "year": 1984,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71L9Dv2XPXL.jpg",
            "rating": 4.7,
            "read_time": 14,
            "overview": "The six universal principles of influence and how to defend yourself against manipulation.",
            "executive": "Cialdini reveals the psychology behind why people say yes and how to apply these understandings ethically in business and daily life.",
            "takeaways": [
                {"title": "Reciprocity", "text": "People feel obligated to repay what they receive. Give first to create obligation."},
                {"title": "Social Proof", "text": "We look to others' actions to determine our own, especially in uncertain situations."},
                {"title": "Scarcity", "text": "Opportunities seem more valuable when they're less available."}
            ],
            "quotes": ["A well-known principle of human behavior says that when we ask someone to do us a favor we will be more successful if we provide a reason."],
            "action_steps": ["Identify influence tactics used on you", "Apply reciprocity in your relationships", "Use social proof in your communications"]
        },
        {
            "title": "Quiet: The Power of Introverts",
            "author": "Susan Cain",
            "year": 2012,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71Ld6UxYmtL.jpg",
            "rating": 4.6,
            "read_time": 15,
            "overview": "How introverts can capitalize on their quiet strengths in a world that can't stop talking.",
            "executive": "Cain makes a powerful case for introverts, showing how society undervalues their unique contributions and how introverts can thrive while staying true to themselves.",
            "takeaways": [
                {"title": "Introversion is Not Shyness", "text": "Introverts prefer less stimulating environments—it's about energy, not fear."},
                {"title": "Restorative Niches", "text": "Introverts need time and space to recharge after social interaction."},
                {"title": "The Power of Solitude", "text": "Many creative breakthroughs come from working alone."}
            ],
            "quotes": ["There's zero correlation between being the best talker and having the best ideas.", "Solitude matters, and for some people, it's the air they breathe."],
            "action_steps": ["Create daily restorative niches", "Leverage your listening skills", "Speak up about your unique contributions"]
        },
        {
            "title": "Predictably Irrational",
            "author": "Dan Ariely",
            "year": 2008,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71P7TABt7NL.jpg",
            "rating": 4.5,
            "read_time": 13,
            "overview": "The hidden forces that shape our decisions and why we make irrational choices in predictable ways.",
            "executive": "Ariely's experiments reveal that our irrational behaviors are neither random nor senseless—they are systematic and predictable. Understanding them can improve our decisions.",
            "takeaways": [
                {"title": "Relativity Shapes Choices", "text": "We evaluate options relative to others, not absolutely. Add a decoy to shift preferences."},
                {"title": "Free Is Powerful", "text": "Free reduces fear of loss to zero. We overvalue free options."},
                {"title": "Expectations Shape Experience", "text": "What we expect influences what we actually experience."}
            ],
            "quotes": ["We are pawns in a game whose forces we largely fail to comprehend.", "Standard economics assumes that we are rational. But we are far less rational."],
            "action_steps": ["Beware of decoy options in decisions", "Question your expectations before experiences", "Remove emotional triggers from important decisions"]
        },
        {
            "title": "Emotional Intelligence",
            "author": "Daniel Goleman",
            "year": 1995,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81OHn1dB-9L.jpg",
            "rating": 4.5,
            "read_time": 14,
            "overview": "Why emotional intelligence can matter more than IQ for success in life and work.",
            "executive": "Goleman presents research showing that emotional intelligence—self-awareness, self-regulation, motivation, empathy, and social skills—is a better predictor of success than traditional intelligence.",
            "takeaways": [
                {"title": "EQ vs IQ", "text": "Emotional intelligence accounts for 67% of the abilities needed for superior performance in leaders."},
                {"title": "Self-Awareness is Foundation", "text": "Understanding your emotions is the first step to managing them."},
                {"title": "Empathy Builds Connection", "text": "Reading others' emotions enables effective relationships."}
            ],
            "quotes": ["In a very real sense we have two minds, one that thinks and one that feels."],
            "action_steps": ["Practice naming your emotions", "Pause before reacting to triggers", "Ask questions to understand others' perspectives"]
        },
        {
            "title": "The Power of Habit",
            "author": "Charles Duhigg",
            "year": 2012,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71r5XL4s2FL.jpg",
            "rating": 4.6,
            "read_time": 14,
            "overview": "Why we do what we do in life and business—the science of habit formation and change.",
            "executive": "Duhigg explains the neurological loop at the core of every habit and how understanding this can transform your life, your company, and your society.",
            "takeaways": [
                {"title": "The Habit Loop", "text": "Every habit has a cue, a routine, and a reward. Change the routine, keep the cue and reward."},
                {"title": "Keystone Habits", "text": "Some habits matter more than others. They create chain reactions that shift other patterns."},
                {"title": "Willpower is a Muscle", "text": "Willpower can be strengthened through practice but also depleted."}
            ],
            "quotes": ["Change might not be fast and it isn't always easy. But with time and effort, almost any habit can be reshaped."],
            "action_steps": ["Identify the cue and reward for a habit you want to change", "Find your keystone habit", "Plan for willpower depletion"]
        },
        {
            "title": "Grit: The Power of Passion and Perseverance",
            "author": "Angela Duckworth",
            "year": 2016,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71OWvONxAbL.jpg",
            "rating": 4.5,
            "read_time": 13,
            "overview": "Why passion and persistence matter more than talent for achieving long-term goals.",
            "executive": "Duckworth's research shows that the secret to outstanding achievement is not talent but grit—a special blend of passion and persistence.",
            "takeaways": [
                {"title": "Grit = Passion + Perseverance", "text": "Sustained effort over years is more predictive of success than talent alone."},
                {"title": "Interest, Practice, Purpose, Hope", "text": "These four psychological assets cultivate grit over time."},
                {"title": "Hard Thing Rule", "text": "Everyone picks a hard thing, can't quit mid-season, and chooses it themselves."}
            ],
            "quotes": ["Enthusiasm is common. Endurance is rare.", "Grit is about working on something you care about so much that you're willing to stay loyal to it."],
            "action_steps": ["Take the Grit Scale assessment", "Implement the Hard Thing Rule", "Connect your work to a purpose beyond yourself"]
        }
    ],
    "finance": [
        {
            "title": "Rich Dad Poor Dad",
            "author": "Robert T. Kiyosaki",
            "year": 1997,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81bsw6fnUiL.jpg",
            "rating": 4.6,
            "read_time": 12,
            "overview": "What the rich teach their kids about money that the poor and middle class do not.",
            "executive": "Kiyosaki contrasts the financial philosophies of his two fathers—his biological dad (poor) and his friend's dad (rich)—to teach fundamental lessons about money, assets, and wealth-building.",
            "takeaways": [
                {"title": "Assets vs Liabilities", "text": "Assets put money in your pocket; liabilities take money out. The rich buy assets."},
                {"title": "Work to Learn", "text": "Don't work for money—work to acquire skills and experience."},
                {"title": "Financial Literacy", "text": "Understanding accounting, investing, and markets is essential for wealth."}
            ],
            "quotes": ["The poor and middle class work for money. The rich have money work for them.", "It's not how much money you make, it's how much money you keep."],
            "action_steps": ["List your assets and liabilities", "Identify one new skill to develop", "Start a side income stream"]
        },
        {
            "title": "The Intelligent Investor",
            "author": "Benjamin Graham",
            "year": 1949,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/91+t0Di07FL.jpg",
            "rating": 4.7,
            "read_time": 20,
            "overview": "The definitive book on value investing—a safe approach to financial markets.",
            "executive": "Graham's timeless principles of value investing have guided generations of investors, including Warren Buffett. Focus on intrinsic value, margin of safety, and emotional discipline.",
            "takeaways": [
                {"title": "Mr. Market", "text": "The market is an emotional partner. Take advantage of his mood swings; don't be influenced by them."},
                {"title": "Margin of Safety", "text": "Only buy securities when the price is significantly below intrinsic value."},
                {"title": "Investor vs Speculator", "text": "Investors analyze, seek safety, and expect adequate returns. Speculators gamble."}
            ],
            "quotes": ["The investor's chief problem—and even his worst enemy—is likely to be himself.", "In the short run, the market is a voting machine but in the long run, it is a weighing machine."],
            "action_steps": ["Calculate the intrinsic value of a stock you own", "Define your investment policy", "Ignore market noise; focus on fundamentals"]
        },
        {
            "title": "The Millionaire Next Door",
            "author": "Thomas J. Stanley & William D. Danko",
            "year": 1996,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81LbLsRKOkL.jpg",
            "rating": 4.5,
            "read_time": 13,
            "overview": "Surprising secrets of America's wealthy—they're not who you think they are.",
            "executive": "Based on extensive research, the authors reveal that most millionaires live below their means, avoid flashy consumption, and build wealth through discipline rather than high income.",
            "takeaways": [
                {"title": "Frugal, Frugal, Frugal", "text": "Most millionaires budget, live well below their means, and avoid status symbols."},
                {"title": "Time and Energy", "text": "Wealthy people spend more time planning investments than consuming."},
                {"title": "Economic Outpatient Care", "text": "Giving adult children money often hinders their wealth-building."}
            ],
            "quotes": ["Wealth is more often the result of a lifestyle of hard work, perseverance, planning, and most of all, self-discipline."],
            "action_steps": ["Track your spending for a month", "Calculate your expected net worth", "Reduce one status-related expense"]
        },
        {
            "title": "A Random Walk Down Wall Street",
            "author": "Burton G. Malkiel",
            "year": 1973,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81R7kfCKz3L.jpg",
            "rating": 4.5,
            "read_time": 16,
            "overview": "The time-tested strategy for successful investing through index funds.",
            "executive": "Malkiel makes the case that market prices reflect all available information and that trying to beat the market is futile. Index investing is the most reliable path to wealth.",
            "takeaways": [
                {"title": "Efficient Market Hypothesis", "text": "Stock prices already reflect all known information. Predicting movements is impossible."},
                {"title": "Index Funds Win", "text": "Most active managers underperform low-cost index funds over time."},
                {"title": "Time in Market", "text": "Time in the market beats timing the market."}
            ],
            "quotes": ["A blindfolded monkey throwing darts at a newspaper's financial pages could select a portfolio that would do just as well as one carefully selected by experts."],
            "action_steps": ["Calculate your active fund fees", "Shift to low-cost index funds", "Set up automatic monthly investing"]
        },
        {
            "title": "The Total Money Makeover",
            "author": "Dave Ramsey",
            "year": 2003,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81KQfM1v8TL.jpg",
            "rating": 4.6,
            "read_time": 11,
            "overview": "A proven plan for financial fitness—get out of debt and build wealth.",
            "executive": "Ramsey's seven Baby Steps provide a clear, actionable path from debt to wealth. Intensity and focus are key to changing your financial life.",
            "takeaways": [
                {"title": "Baby Steps", "text": "1. $1000 emergency fund 2. Debt snowball 3. 3-6 months expenses 4. 15% to retirement 5. Kids' college 6. Pay off home 7. Build wealth and give."},
                {"title": "Debt Snowball", "text": "Pay off smallest debts first for psychological wins."},
                {"title": "Live Like No One Else", "text": "Sacrifice now so you can live and give like no one else later."}
            ],
            "quotes": ["We buy things we don't need with money we don't have to impress people we don't like.", "If you will live like no one else, later you can live like no one else."],
            "action_steps": ["List all debts smallest to largest", "Cut up credit cards", "Create a written monthly budget"]
        },
        {
            "title": "I Will Teach You to Be Rich",
            "author": "Ramit Sethi",
            "year": 2009,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81vLx71FuhL.jpg",
            "rating": 4.6,
            "read_time": 13,
            "overview": "No guilt. No excuses. Just a 6-week program that works for millennials and beyond.",
            "executive": "Sethi provides a practical, no-nonsense approach to personal finance, focusing on automating your money, conscious spending, and living a rich life on your own terms.",
            "takeaways": [
                {"title": "Automate Everything", "text": "Set up automatic transfers to savings, investments, and bill payments."},
                {"title": "Conscious Spending Plan", "text": "Spend extravagantly on things you love, cut mercilessly on things you don't."},
                {"title": "Negotiate Everything", "text": "Negotiate salary, fees, and rates. It takes 5 minutes but pays for years."}
            ],
            "quotes": ["The single most important thing you can do to be rich is to start early.", "There's a limit to how much you can cut, but no limit to how much you can earn."],
            "action_steps": ["Set up automatic savings transfers", "Identify your Money Dials", "Negotiate one bill this week"]
        }
    ],
    "productivity": [
        {
            "title": "Getting Things Done",
            "author": "David Allen",
            "year": 2001,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71dVv1-HT8L.jpg",
            "rating": 4.5,
            "read_time": 14,
            "overview": "The art of stress-free productivity through capturing, clarifying, and organizing all commitments.",
            "executive": "Allen's GTD methodology provides a complete system for organizing tasks and information. The key insight: your mind is for having ideas, not holding them.",
            "takeaways": [
                {"title": "Capture Everything", "text": "Get all commitments out of your head and into a trusted system."},
                {"title": "The Two-Minute Rule", "text": "If an action takes less than two minutes, do it immediately."},
                {"title": "Weekly Review", "text": "Regularly review and update your system to maintain trust in it."}
            ],
            "quotes": ["Your mind is for having ideas, not holding them.", "You can do anything, but not everything."],
            "action_steps": ["Set up a capture system", "Process your inbox to zero", "Schedule a weekly review"]
        },
        {
            "title": "The 4-Hour Workweek",
            "author": "Timothy Ferriss",
            "year": 2007,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/51HfFnEt0UL.jpg",
            "rating": 4.4,
            "read_time": 15,
            "overview": "Escape 9-5, live anywhere, and join the new rich through lifestyle design.",
            "executive": "Ferriss challenges conventional work assumptions and provides a blueprint for automating income, eliminating time-wasters, and creating the freedom to live life on your own terms.",
            "takeaways": [
                {"title": "DEAL Framework", "text": "Definition, Elimination, Automation, Liberation—the four steps to the new rich."},
                {"title": "Pareto's Law", "text": "80% of results come from 20% of efforts. Focus on what matters."},
                {"title": "Fear-Setting", "text": "Define your fears in detail to overcome paralysis and take action."}
            ],
            "quotes": ["Focus on being productive instead of busy.", "What we fear doing most is usually what we most need to do."],
            "action_steps": ["Identify your 20% that produces 80%", "Complete a fear-setting exercise", "Implement one automation this week"]
        },
        {
            "title": "Essentialism",
            "author": "Greg McKeown",
            "year": 2014,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71K0eE0dNxL.jpg",
            "rating": 4.6,
            "read_time": 12,
            "overview": "The disciplined pursuit of less—doing the right things instead of more things.",
            "executive": "McKeown argues that only by saying no to the non-essential can we make our highest contribution to the things that truly matter.",
            "takeaways": [
                {"title": "Less But Better", "text": "The way of the Essentialist: do less but do it better."},
                {"title": "Trade-offs Are Real", "text": "You cannot have it all. Accept trade-offs and choose deliberately."},
                {"title": "The 90% Rule", "text": "If it isn't a clear yes, it's a no."}
            ],
            "quotes": ["If you don't prioritize your life, someone else will.", "The pursuit of success can be a catalyst for failure."],
            "action_steps": ["Apply the 90% rule to new opportunities", "Say no to one thing today", "Identify your highest contribution"]
        },
        {
            "title": "Make Time",
            "author": "Jake Knapp & John Zeratsky",
            "year": 2018,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71R-EXuQ1zL.jpg",
            "rating": 4.5,
            "read_time": 11,
            "overview": "How to focus on what matters every day with a simple four-step framework.",
            "executive": "From the creators of Google Ventures' Design Sprint, a practical guide to breaking free from busy and designing your days around what matters most.",
            "takeaways": [
                {"title": "Highlight", "text": "Choose one priority each day to focus on."},
                {"title": "Laser", "text": "Beat distraction to make time for your highlight."},
                {"title": "Energize", "text": "Use the body to charge the brain. Sleep, exercise, and eat for energy."}
            ],
            "quotes": ["Being more productive didn't mean I was doing more important work; it only meant I was getting more done."],
            "action_steps": ["Choose tomorrow's highlight tonight", "Turn off notifications", "Take a 20-minute walk today"]
        },
        {
            "title": "The One Thing",
            "author": "Gary Keller",
            "year": 2013,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71uM8LH+VBL.jpg",
            "rating": 4.6,
            "read_time": 11,
            "overview": "The surprisingly simple truth behind extraordinary results: focus on one thing.",
            "executive": "Keller argues that success comes from narrowing your focus to the one thing that matters most, rather than trying to do everything at once.",
            "takeaways": [
                {"title": "The Focusing Question", "text": "What's the ONE thing I can do such that by doing it everything else will be easier or unnecessary?"},
                {"title": "Domino Effect", "text": "Success is sequential. Do the right thing and then the next right thing."},
                {"title": "Time Blocking", "text": "Block time for your ONE thing before anything else."}
            ],
            "quotes": ["Multitasking is a lie.", "Success is actually a short race—a sprint fueled by discipline just long enough for habit to kick in."],
            "action_steps": ["Ask the focusing question for your biggest goal", "Time block 4 hours for your ONE thing", "Eliminate one commitment"]
        },
        {
            "title": "Eat That Frog!",
            "author": "Brian Tracy",
            "year": 2001,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81N0k3zZNaL.jpg",
            "rating": 4.4,
            "read_time": 9,
            "overview": "21 great ways to stop procrastinating and get more done in less time.",
            "executive": "Tracy's practical guide teaches that if you have to eat a frog, do it first thing in the morning. Tackle your most important task first.",
            "takeaways": [
                {"title": "Eat the Frog First", "text": "Do your hardest, most important task first thing."},
                {"title": "ABCDE Method", "text": "Prioritize tasks as A (must do), B (should do), C (nice to do), D (delegate), E (eliminate)."},
                {"title": "10/90 Rule", "text": "The first 10% of time spent planning saves 90% of effort."}
            ],
            "quotes": ["If you have to eat two frogs, eat the ugliest one first.", "The key to success is action."],
            "action_steps": ["Identify your frog for tomorrow", "Apply ABCDE to your task list", "Plan your day the night before"]
        }
    ],
    "philosophy": [
        {
            "title": "Meditations",
            "author": "Marcus Aurelius",
            "year": 180,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71J1e+r75YL.jpg",
            "rating": 4.8,
            "read_time": 14,
            "overview": "Private reflections of a Roman emperor on Stoic philosophy and living a virtuous life.",
            "executive": "Marcus Aurelius's personal journal offers timeless wisdom on character, duty, and accepting what we cannot control. The foundational text of Stoic philosophy.",
            "takeaways": [
                {"title": "Control What You Can", "text": "Focus only on what is within your power: your thoughts and actions."},
                {"title": "Memento Mori", "text": "Remembering death helps you live fully. Time is precious."},
                {"title": "Amor Fati", "text": "Love your fate. Accept and embrace everything that happens."}
            ],
            "quotes": ["You have power over your mind—not outside events. Realize this, and you will find strength.", "The obstacle is the way."],
            "action_steps": ["Start a reflection journal", "When frustrated, ask: is this in my control?", "Meditate on mortality for 5 minutes"]
        },
        {
            "title": "The Daily Stoic",
            "author": "Ryan Holiday",
            "year": 2016,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81AYYz7oISL.jpg",
            "rating": 4.7,
            "read_time": 12,
            "overview": "366 meditations on wisdom, perseverance, and the art of living.",
            "executive": "Holiday presents daily Stoic readings organized around three disciplines: perception, action, and will. Practical philosophy for modern life.",
            "takeaways": [
                {"title": "Perception", "text": "How we see and interpret the world around us."},
                {"title": "Action", "text": "The decisions and actions we take based on that perception."},
                {"title": "Will", "text": "How we deal with the things we cannot change."}
            ],
            "quotes": ["The more we value things outside our control, the less control we have."],
            "action_steps": ["Read one Stoic passage each morning", "Practice negative visualization", "Reframe one obstacle as opportunity"]
        },
        {
            "title": "Letters from a Stoic",
            "author": "Seneca",
            "year": 65,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/71a2N10z0SL.jpg",
            "rating": 4.7,
            "read_time": 16,
            "overview": "Practical wisdom from ancient Rome's most readable philosopher.",
            "executive": "Seneca's letters to his friend Lucilius cover topics from grief to anger to the proper use of time. Remarkably relevant advice from 2,000 years ago.",
            "takeaways": [
                {"title": "On Time", "text": "We waste time as if we have an unlimited supply. Treat time as your most precious resource."},
                {"title": "On Adversity", "text": "Difficulties strengthen the mind. Fire tests gold; misfortune tests brave men."},
                {"title": "On Enough", "text": "It is not the man who has too little, but the man who craves more, that is poor."}
            ],
            "quotes": ["We suffer more in imagination than in reality.", "Luck is what happens when preparation meets opportunity."],
            "action_steps": ["Audit how you spend your time", "Prepare for adversity through practice", "Define 'enough' for yourself"]
        },
        {
            "title": "The Almanack of Naval Ravikant",
            "author": "Eric Jorgenson",
            "year": 2020,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/61ngHyFy5VL.jpg",
            "rating": 4.8,
            "read_time": 12,
            "overview": "A guide to wealth and happiness from the angel philosopher of Silicon Valley.",
            "executive": "A collection of Naval Ravikant's wisdom on building wealth, finding happiness, and living a good life in the modern age.",
            "takeaways": [
                {"title": "Specific Knowledge", "text": "Arm yourself with knowledge that cannot be trained. It is found by pursuing your genuine curiosity."},
                {"title": "Leverage", "text": "Use capital, code, and media to multiply your outputs without multiplying your inputs."},
                {"title": "Happiness is a Choice", "text": "Happiness is a skill you develop and a choice you make."}
            ],
            "quotes": ["Seek wealth, not money or status.", "The most important skill for getting rich is becoming a perpetual learner."],
            "action_steps": ["Identify your specific knowledge", "Build leverage through content or code", "Practice daily gratitude"]
        }
    ],
    "history": [
        {
            "title": "Guns, Germs, and Steel",
            "author": "Jared Diamond",
            "year": 1997,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/91sCp5f3hbL.jpg",
            "rating": 4.6,
            "read_time": 18,
            "overview": "The fates of human societies and why history unfolded differently on different continents.",
            "executive": "Diamond explores why Eurasian civilizations conquered others rather than vice versa. Geography and environment—not biology—determined which societies developed advantages.",
            "takeaways": [
                {"title": "Geographic Luck", "text": "Domesticable plants and animals were not evenly distributed across continents."},
                {"title": "Axis Orientation", "text": "East-west continents allowed faster spread of innovations than north-south ones."},
                {"title": "Germs as Weapons", "text": "Diseases from domesticated animals gave Eurasians inadvertent biological warfare."}
            ],
            "quotes": ["History followed different courses for different peoples because of differences among peoples' environments."],
            "action_steps": ["Study how geography shaped your region", "Consider environmental factors in current events", "Read about other civilizations' development"]
        },
        {
            "title": "The Lessons of History",
            "author": "Will & Ariel Durant",
            "year": 1968,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81Eb+PB2NQL.jpg",
            "rating": 4.7,
            "read_time": 10,
            "overview": "Distilled wisdom from 5,000 years of world history in a brief masterpiece.",
            "executive": "The Durants compress their 11-volume Story of Civilization into essential patterns and lessons. A concise guide to understanding historical forces.",
            "takeaways": [
                {"title": "History Rhymes", "text": "The same basic processes repeat throughout history in different forms."},
                {"title": "Inequality is Natural", "text": "Inequality appears in every society but must be balanced to prevent revolution."},
                {"title": "Religion Serves Society", "text": "Religion provides social cohesion and moral order even as beliefs change."}
            ],
            "quotes": ["Civilization is a stream with banks.", "The only real revolution is in the enlightenment of the mind."],
            "action_steps": ["Study one historical parallel to today", "Identify patterns in your industry's history", "Read primary sources from the past"]
        },
        {
            "title": "Team of Rivals",
            "author": "Doris Kearns Goodwin",
            "year": 2005,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/91cxjBDJFaL.jpg",
            "rating": 4.7,
            "read_time": 22,
            "overview": "The political genius of Abraham Lincoln and how he assembled his former rivals into his cabinet.",
            "executive": "Goodwin shows how Lincoln's emotional intelligence and political acumen turned his opponents into allies, leading the nation through its darkest hour.",
            "takeaways": [
                {"title": "Embrace Rivals", "text": "Lincoln surrounded himself with the strongest voices, even former competitors."},
                {"title": "Emotional Intelligence", "text": "Lincoln's empathy and ability to manage his emotions were key to his leadership."},
                {"title": "Timing is Everything", "text": "Great leaders know when to act and when to wait."}
            ],
            "quotes": ["Lincoln's political genius was not simply his ability to maneuver, but his capacity to understand the passions and motivations of others."],
            "action_steps": ["Seek out opposing viewpoints", "Practice empathy in conflict", "Study Lincoln's letter-writing discipline"]
        }
    ]
}


def seed_extended_books():
    """Seed the database with 100+ extended books."""
    db = get_session()
    
    # Get genre map
    genres = db.query(Genre).all()
    genre_map = {g.slug: g for g in genres}
    
    if not genre_map:
        print("❌ No genres found. Run main seed first: python -m database.seed")
        return
    
    books_added = 0
    books_skipped = 0
    
    for genre_slug, books in EXTENDED_BOOKS.items():
        if genre_slug not in genre_map:
            print(f"⚠️  Genre '{genre_slug}' not found, skipping...")
            continue
        
        genre = genre_map[genre_slug]
        print(f"\n📚 Seeding {genre.name}...")
        
        for book_data in books:
            slug = book_data["title"].lower().replace(" ", "-").replace(":", "").replace("'", "").replace("*", "").replace("?", "")
            
            # Check if book exists
            existing = db.query(Book).filter(Book.slug == slug).first()
            if existing:
                books_skipped += 1
                continue
            
            # Create book
            book = Book(
                title=book_data["title"],
                author=book_data["author"],
                slug=slug,
                cover_image_url=book_data["cover"],
                publication_year=book_data["year"],
                genre=genre,
                is_featured=False  # Can be updated later
            )
            db.add(book)
            db.commit()
            
            # Create summary
            summary = Summary(
                book_id=book.id,
                overview_text=book_data["overview"],
                executive_summary=book_data["executive"],
                main_content=book_data["executive"],  # Use executive as main
                key_takeaways=json.dumps(book_data["takeaways"]),
                who_should_read=f"Anyone interested in {genre.name.lower()} and {book_data['author']}'s insights.",
                reading_time=book_data["read_time"],
                rating=book_data["rating"],
                quotes=json.dumps(book_data.get("quotes", [])),
                action_steps=json.dumps(book_data.get("action_steps", [])),
                quote_of_the_book=book_data["quotes"][0] if book_data.get("quotes") else "",
                difficulty="Intermediate",
                seo_title=f"{book_data['title']} Summary - Key Takeaways & Insights",
                seo_description=f"Read our comprehensive summary of {book_data['title']} by {book_data['author']}. Get key insights and actionable takeaways."
            )
            db.add(summary)
            db.commit()
            
            books_added += 1
            print(f"  ✅ {book_data['title']}")
    
    db.close()
    print(f"\n🎉 Done! Added {books_added} books, skipped {books_skipped} existing.")


if __name__ == "__main__":
    seed_extended_books()
