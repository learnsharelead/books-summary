"""
Expert Book Database - Curated Book-Specific Content
Each book has unique frameworks, concepts, and visual models.
"""

BOOK_DATABASE = {
    "Atomic Habits": {
        "author": "James Clear",
        "genre": "self-help",
        "year": 2018,
        "rating": 4.9,
        "time": 18,
        "cover": "https://m.media-amazon.com/images/I/81F90H7hnML._SL1500_.jpg",
        "overview": "The definitive guide to building good habits and breaking bad ones using the framework of tiny changes.",
        "executive": """**Atomic Habits** presents a proven framework for improving every day. James Clear reveals how tiny changes in behavior compound into remarkable results through the power of the "aggregation of marginal gains."

The book introduces the **Four Laws of Behavior Change**: Make it Obvious, Make it Attractive, Make it Easy, and Make it Satisfying. Every habit follows this cycle: cue, craving, response, reward. By manipulating these levers, you can build good habits and break bad ones.

Clear argues that you don't rise to the level of your goals; you fall to the level of your systems. The book provides practical strategies for habit stacking, environment design, and identity-based change. True behavior change is identity change. The goal is not to read a book, but to become a reader.""",
        "framework": "The 4 Laws of Behavior Change",
        "takeaways": [
            {
                "title": "The 1% Rule", 
                "text": "Habits are the compound interest of self-improvement. Getting 1% better every day means you'll be 37 times better in a year. Small changes appear to make no difference until you cross a critical threshold."
            },
            {
                "title": "Identity-Based Habits", 
                "text": "The most effective way to change behavior is to focus on who you wish to become, not what you want to achieve. Every action is a vote for the type of person you want to be."
            },
            {
                "title": "The Four Laws", 
                "text": "To build a good habit: Make it Obvious (clear cue), Make it Attractive (enhance craving), Make it Easy (reduce friction), Make it Satisfying (immediate reward). Invert these for breaking bad habits."
            },
            {
                "title": "Habit Stacking", 
                "text": "The best way to form a new habit is to tie it to an existing one. Formula: 'After I [current habit], I will [new habit].' This leverages the momentum of existing routines."
            },
            {
                "title": "Environment Design", 
                "text": "The most powerful influences on behavior are invisible. Design your environment so the cues for good habits are obvious and the cues for bad habits are invisible."
            }
        ],
        "quotes": [
            "You do not rise to the level of your goals. You fall to the level of your systems.",
            "Every action you take is a vote for the type of person you wish to become.",
            "Habits are the compound interest of self-improvement."
        ],
        "actions": [
            "Use the 2-Minute Rule: Scale down habits to two-minute versions",
            "Write down your current habits and mark them as +, -, or =",
            "Stack a new habit onto an existing one using the formula",
            "Redesign your environment to make cues obvious",
            "Track your habits daily with a simple system"
        ],
        "analogies": [
            {
                "concept": "The Plateau of Latent Potential",
                "analogy": "Like an ice cube melting",
                "explanation": "You heat an ice cube from 25°F to 31°F and nothing happens. But at 32°F, a one-degree shift unleashes a phase change. Habits work the same way—breakthrough moments are the result of many previous actions building up potential."
            }
        ],
        "visual_map": '''
        digraph "Atomic Habits" {
            rankdir=LR
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            subgraph cluster_cycle {
                label="The Habit Loop"
                style=filled
                color=lightgrey
                
                cue [label="1️⃣ CUE\\nMake it Obvious", fillcolor="#FFE4B5"]
                craving [label="2️⃣ CRAVING\\nMake it Attractive", fillcolor="#98FB98"]
                response [label="3️⃣ RESPONSE\\nMake it Easy", fillcolor="#87CEEB"]
                reward [label="4️⃣ REWARD\\nMake it Satisfying", fillcolor="#DDA0DD"]
                
                cue -> craving -> response -> reward -> cue [style=bold]
            }
            
            identity [label="🎯 IDENTITY\\nBecome the person\\nyou want to be", fillcolor="#FFD700", shape=diamond]
            
            reward -> identity [label="reinforces", style=dashed]
            identity -> cue [label="motivates", style=dashed]
        }
        '''
    },
    
    "Thinking, Fast and Slow": {
        "author": "Daniel Kahneman",
        "genre": "psychology",
        "year": 2011,
        "rating": 4.7,
        "time": 22,
        "cover": "https://m.media-amazon.com/images/I/61fdrEuPJwL._SL1500_.jpg",
        "overview": "Nobel laureate Daniel Kahneman reveals the two systems that drive how we think and the biases that lead us astray.",
        "executive": """**Thinking, Fast and Slow** introduces Kahneman's groundbreaking research on the two systems of thought that govern our minds. **System 1** operates automatically, quickly, and with little conscious effort. **System 2** allocates attention to effortful mental activities requiring computation.

The book reveals systematic errors (biases) in our thinking: anchoring, availability heuristic, substitution, overconfidence, and loss aversion. These aren't random mistakes but predictable patterns in how we process information.

Kahneman demonstrates that our intuitive System 1 often makes mistakes when dealing with statistics and probability, while our System 2 is lazy and often defers to System 1 even when it shouldn't. Understanding these systems and their limitations is essential for better decision-making.""",
        "framework": "Two Systems of Thinking",
        "takeaways": [
            {
                "title": "System 1 vs System 2",
                "text": "System 1 is fast, automatic, frequent, emotional, stereotypic, and subconscious. System 2 is slow, effortful, infrequent, logical, calculating, and conscious. Most of our judgments and actions are guided by System 1."
            },
            {
                "title": "WYSIATI (What You See Is All There Is)",
                "text": "System 1 creates coherent stories based on limited information, ignoring what's missing. This leads to overconfidence and premature conclusions. The confidence we have in our beliefs is not a measure of quality of evidence."
            },
            {
                "title": "Loss Aversion",
                "text": "Losses loom larger than gains. The pain of losing $100 is more intense than the pleasure of gaining $100. This asymmetry drives irrational decisions and the endowment effect (overvaluing what we own)."
            },
            {
                "title": "Anchoring Effect",
                "text": "Our estimates are heavily influenced by arbitrary anchors. If asked whether Gandhi died before or after age 144, people subsequently guess a higher age than if asked about 35. The anchor 'pulls' estimates toward it."
            },
            {
                "title": "The Availability Heuristic",
                "text": "We judge probability by how easily examples come to mind, not actual frequency. Dramatic events (plane crashes) are overweighted because they're memorable, while common risks (car accidents) are underestimated."
            }
        ],
        "quotes": [
            "Nothing in life is as important as you think it is while you are thinking about it.",
            "A reliable way to make people believe in falsehoods is frequent repetition, because familiarity is not easily distinguished from truth.",
            "We can be blind to the obvious, and we are also blind to our blindness."
        ],
        "actions": [
            "Slow down and engage System 2 for important decisions",
            "Use checklists to prevent System 1 errors",
            "Conduct pre-mortems: Imagine failure and work backward",
            "Seek out disconfirming evidence for your beliefs",
            "Reframe decisions in terms of losses to reveal true preferences"
        ],
        "analogies": [
            {
                "concept": "System 1 and System 2",
                "analogy": "Like autopilot vs manual control",
                "explanation": "System 1 is the autopilot that handles routine operations efficiently. System 2 is manual control—you must take over for complex maneuvers, but it's exhausting to use continuously."
            }
        ],
        "visual_map": '''
        digraph "Thinking Fast and Slow" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            stimulus [label="📊 STIMULUS", fillcolor="#E8E8E8"]
            
            system1 [label="⚡ SYSTEM 1\\nFast, Automatic\\nIntuitive, Emotional\\nAlways On", fillcolor="#FFB6C1", shape=ellipse]
            system2 [label="🧠 SYSTEM 2\\nSlow, Effortful\\nRational, Calculating\\nLazy", fillcolor="#87CEEB", shape=ellipse]
            
            biases [label="⚠️ BIASES\\nAnchoring\\nAvailability\\nLoss Aversion\\nOverconfidence", fillcolor="#FFE4B5"]
            
            decision [label="🎯 DECISION", fillcolor="#98FB98"]
            
            stimulus -> system1
            stimulus -> system2
            system1 -> biases [label="often leads to"]
            biases -> decision
            system2 -> decision [label="monitors\\n(sometimes)"]
            system1 -> system2 [label="calls for help\\n(when stuck)", style=dashed]
        }
        '''
    },
    
    "Deep Work": {
        "author": "Cal Newport",
        "genre": "productivity",
        "year": 2016,
        "rating": 4.6,
        "time": 15,
        "cover": "https://m.media-amazon.com/images/I/71e9MYTEOTL._SL1500_.jpg",
        "overview": "Professional activities performed in a state of distraction-free concentration that push your cognitive abilities to their limit.",
        "executive": """**Deep Work** is the ability to focus without distraction on a cognitively demanding task. Cal Newport argues this skill is becoming increasingly rare at exactly the same time it's becoming increasingly valuable in our economy.

Newport identifies **shallow work**—logistical tasks performed while distracted—as the enemy of deep work. The modern workplace is biased toward shallow work through open offices, instant messaging, and email. This creates a culture of connectivity but destroys the ability to concentrate.

The book provides four philosophies for scheduling deep work (monastic, bimodal, rhythmic, journalistic) and practical strategies like attention residue management, productive meditation, and quitting social media. Newport argues that deep work is not just economically valuable but also deeply satisfying.""",
        "framework": "Deep Work vs Shallow Work",
        "takeaways": [
            {
                "title": "The Deep Work Hypothesis",
                "text": "The ability to perform deep work is becoming increasingly rare and valuable. Those who master deep work will thrive while those who don't will struggle. This creates massive competitive advantage."
            },
            {
                "title": "Attention Residue",
                "text": "When you switch from Task A to Task B, your attention doesn't immediately follow. A residue of attention remains stuck on the previous task. To maximize performance, eliminate task-switching."
            },
            {
                "title": "The Four Disciplines",
                "text": "1) Focus on the Wildly Important 2) Act on Lead Measures (time in deep work) not lag measures (output) 3) Keep a Compelling Scoreboard 4) Create Cadence of Accountability (weekly review)"
            },
            {
                "title": "Embrace Boredom",
                "text": "The ability to concentrate is a skill that must be trained. If you constantly seek stimulation, you won't be able to focus when needed. Schedule breaks from focus, not breaks from distraction."
            },
            {
                "title": "Quit Social Media",
                "text": "Apply the craftsman approach to tool selection: only use a tool if its positive impacts substantially outweigh negatives. For most knowledge workers, social media fails this test."
            }
        ],
        "quotes": [
            "Clarity about what matters provides clarity about what does not.",
            "High-Quality Work Produced = (Time Spent) × (Intensity of Focus)",
            "Deep work is so important that we might consider it the superpower of the 21st century."
        ],
        "actions": [
            "Schedule deep work blocks of at least 90 minutes",
            "Create a shutdown ritual to end your workday completely",
            "Practice productive meditation during physical activity",
            "Delete social media apps from your phone for 30 days",
            "Time-block every minute of your day in advance"
        ],
        "analogies": [
            {
                "concept": "Attention as Capital",
                "analogy": "Like a finite battery",
                "explanation": "Your daily capacity for deep concentration is limited, like a battery that depletes with use. Guard it jealously and direct it only toward your most valuable work."
            }
        ],
        "visual_map": '''
        digraph "Deep Work" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            deep [label="🎯 DEEP WORK\\nDistraction-free\\nCognitively demanding\\nValue-creating", fillcolor="#4169E1", fontcolor=white]
            
            shallow [label="📧 SHALLOW WORK\\nLogistical\\nDistracting\\nLow-value", fillcolor="#FFB6C1"]
            
            strategies [label="STRATEGIES", shape=folder, fillcolor="#E8E8E8"]
            
            rhythmic [label="Rhythmic\\nSame time daily", fillcolor="#98FB98"]
            ritual [label="Ritualize\\nShutdown complete", fillcolor="#87CEEB"]
            embrace [label="Embrace\\nBoredom", fillcolor="#FFE4B5"]
            quit [label="Quit\\nSocial Media", fillcolor="#DDA0DD"]
            
            results [label="⚡ RESULTS\\nRare skill\\nHigh value\\nMeaningful work", fillcolor="#FFD700"]
            
            deep -> strategies
            strategies -> rhythmic
            strategies -> ritual
            strategies -> embrace
            strategies -> quit
            rhythmic -> results
            ritual -> results
            embrace -> results
            quit -> results
            
            shallow -> deep [label="eliminate", style=dashed, color=red]
        }
        '''
    },
    
    "The Psychology of Money": {
        "author": "Morgan Housel",
        "genre": "finance",
        "year": 2020,
        "rating": 4.8,
        "time": 14,
        "cover": "https://m.media-amazon.com/images/I/715k1M+oWLL._SL1500_.jpg",
        "overview": "Timeless lessons on wealth, greed, and happiness told through 19 short stories.",
        "executive": """**The Psychology of Money** argues that doing well with money has little to do with how smart you are and a lot to do with how you behave. Soft skills matter more than technical knowledge in finance.

Housel presents 19 short stories teaching different lessons: compounding, getting vs staying wealthy, tails (outliers) drive everything, room for error, and the importance of defining "enough." The book emphasizes that what works for one person may not work for another because everyone's life experiences are different.

The key insight: **Wealth is what you don't see**—cars not purchased, watches not worn. Building wealth requires humility and frugality while staying wealthy requires maintaining both while avoiding the fatal error of letting one successful outcome lead to overconfidence.""",
        "framework": "Behavioral Finance",
        "takeaways": [
            {
                "title": "Never Enough",
                "text": "The hardest financial skill is getting the goalpost to stop moving. If you risk something you have and need for something you don't have and don't need, you're foolish, regardless of odds. Know when you have enough."
            },
            {
                "title": "Compounding",
                "text": "Warren Buffett's net worth is $84.5 billion. Of that, $84.2 billion was accumulated after his 50th birthday. His skill is investing, but his secret is time. Compounding only works if you can give assets years to grow."
            },
            {
                "title": "Getting vs Staying Wealthy",
                "text": "Getting money requires taking risks, being optimistic, and putting yourself out there. Keeping money requires humility, frugality, and acceptance that you've been lucky. Good investing is surviving."
            },
            {
                "title": "Tails Drive Everything",
                "text": "Long tails—rare events at the ends of distributions—drive disproportionate outcomes. Amazon lost money on most things it tried; it's huge because a few bets worked incredibly well. You can be wrong half the time and still make a fortune."
            },
            {
                "title": "Room for Error",
                "text": "The most important part of every plan is planning on your plan not going according to plan. Use room for error as a central feature of your strategy. Margin of safety is the only reliable way to endure black swan events."
            }
        ],
        "quotes": [
            "Spending money to show people how much money you have is the fastest way to have less money.",
            "Doing well with money has little to do with how smart you are and a lot to do with how you behave.",
            "The highest form of wealth is the ability to wake up every morning and say, 'I can do whatever I want today.'"
        ],
        "actions": [
            "Calculate your 'enough' number and write it down",
            "Increase your savings rate by 1% every month",
            "Build a financial cushion covering 6-12 months expenses",
            "Automate investments to take emotions out of the equation",
            "Define what financial independence means for you"
        ],
        "analogies": [
            {
                "concept": "Wealth vs Rich",
                "analogy": "Like an iceberg",
                "explanation": "What you see (expensive cars, houses) is just the tip—the 'rich' part. True wealth is the 90% hidden below the surface—savings and investments you never see."
            }
        ],
        "visual_map": '''
        digraph "Psychology of Money" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            income [label="💵 INCOME", fillcolor="#98FB98"]
            
            temptation [label="⚠️ TEMPTATION\\nLuxury purchases\\nKeeping up\\nShowing off", fillcolor="#FFB6C1"]
            
            save [label="🏦 SAVE\\n20-30%+\\nAutomate\\nInvisible", fillcolor="#FFE4B5"]
            
            invest [label="📈 INVEST\\nLow-cost index\\nStay invested\\nRoom for error", fillcolor="#87CEEB"]
            
            compound [label="⏰ TIME\\nCompounding\\n10+ years\\nPatience", fillcolor="#DDA0DD"]
            
            freedom [label="🏝️ FREEDOM\\nControl your time\\nDo what you want\\nTrue wealth", fillcolor="#FFD700"]
            
            income -> temptation [style=dashed, color=red, label="resist"]
            income -> save [style=bold]
            save -> invest
            invest -> compound
            compound -> freedom
            
            compound -> invest [style=dashed, label="reinvest"]
        }
        '''
    },
    
    "Meditations": {
        "author": "Marcus Aurelius",
        "genre": "philosophy",
        "year": 180,
        "rating": 4.8,
        "time": 12,
        "cover": "https://m.media-amazon.com/images/I/81K0sPpqgCL._SL1500_.jpg",
        "overview": "Personal writings by Roman Emperor Marcus Aurelius on Stoic philosophy and practical wisdom for life.",
        "executive": """**Meditations** are the private reflections of the most powerful man in the Roman Empire. Written as personal notes to himself, Marcus Aurelius explores Stoic philosophy and its practical application to daily life, leadership, and mortality.

The core Stoic principles emerge: the **Dichotomy of Control** (focus only on what you can control), **Amor Fati** (love your fate), **Memento Mori** (remember death), and virtue as the sole good. Marcus repeatedly reminds himself that external events are indifferent; only his character and responses matter.

Written nearly 2,000 years ago while leading military campaigns, these meditations remain remarkably relevant. The book teaches resilience, perspective, and inner peace through practicing Stoicism—seeing things as they truly are, accepting what we cannot change, and focusing energy on what we can control.""",
        "framework": "Stoic Philosophy",
        "takeaways": [
            {
                "title": "The Dichotomy of Control",
                "text": "Some things are within our control (our thoughts, actions, values) and some are not (others' opinions, outcomes, fate). Focus all energy on what you control. Accept what you don't. This is the foundation of tranquility."
            },
            {
                "title": "Amor Fati",
                "text": "Love your fate. Don't just accept what happens—embrace it. Every obstacle is an opportunity to practice virtue. The impediment to action advances action. What stands in the way becomes the way."
            },
            {
                "title": "Memento Mori",
                "text": "Remember you will die. This isn't morbid but liberating. Awareness of mortality provides urgency and perspective. It eliminates petty concerns and focusing on what truly matters. Live each day as if it were your last."
            },
            {
                "title": "Live in Accordance with Nature",
                "text": "Accept the natural order. Everything changes and passes away. Fighting this causes suffering. Align with reason and nature. What's good for the hive is good for the bee."
            },
            {
                "title": "Virtue as the Sole Good",
                "text": "External things (wealth, fame, comfort) are neither good nor bad—they're indifferent. Only virtue (wisdom, justice, courage, moderation) is truly good. Focus on being good, not having good things."
            }
        ],
        "quotes": [
            "You have power over your mind—not outside events. Realize this, and you will find strength.",
            "The obstacle is the way.",
            "Waste no more time arguing about what a good man should be. Be one."
        ],
        "actions": [
            "Practice morning meditation on the day ahead",
            "Journal before bed reviewing your day",
            "Ask: 'Is this within my control?' before reacting",
            "Practice voluntary discomfort weekly",
            "Read one passage from Meditations daily"
        ],
        "analogies": [
            {
                "concept": "The Mind as a Citadel",
                "analogy": "Like an inner fortress",
                "explanation": "Your mind is an impregnable citadel if properly defended. External events are like sieges—they can surround but never penetrate a well-fortified mind grounded in reason."
            }
        ],
        "visual_map": '''
        digraph "Meditations" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            event [label="🌊 EXTERNAL EVENT\\n(Out of Your Control)", fillcolor="#E8E8E8"]
            
            perception [label="👁️ YOUR PERCEPTION\\n(In Your Control)", fillcolor="#FFE4B5"]
            
            stoic [label="⚖️ STOIC PRINCIPLES", fillcolor="#D2B48C", shape=folder]
            
            dichotomy [label="Control what you can", fillcolor="#98FB98"]
            amor [label="Love your fate", fillcolor="#87CEEB"]
            memento [label="Remember death", fillcolor="#DDA0DD"]
            virtue [label="Practice virtue", fillcolor="#FFB6C1"]
            
            response [label="🎯 WISE RESPONSE", fillcolor="#98FB98"]
            
            tranquility [label="☮️ INNER PEACE\\nAtaraxia", fillcolor="#FFD700"]
            
            event -> perception
            perception -> stoic
            stoic -> dichotomy
            stoic -> amor
            stoic -> memento
            stoic -> virtue
            dichotomy -> response
            amor -> response
            memento -> response
            virtue -> response
            response -> tranquility
        }
        '''
    }
}
