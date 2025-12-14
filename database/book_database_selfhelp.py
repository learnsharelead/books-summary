"""
Self-Help Books Database - Top 30 with Expert Content
Each entry contains actual book frameworks, concepts, and visual maps
"""

SELFHELP_BOOKS = {
    "The 7 Habits of Highly Effective People": {
        "author": "Stephen Covey",
        "genre": "self-help",
        "year": 1989,
        "rating": 4.8,
        "time": 22,
        "cover": "https://m.media-amazon.com/images/I/81MYMV9r7OL._SL1500_.jpg",
        "overview": "Covey's timeless framework for personal and interpersonal effectiveness through character-based principles.",
        "executive": """**The 7 Habits** presents a principle-centered approach to personal and interpersonal effectiveness. Stephen Covey argues that sustainable success comes from aligning with universal principles, not personality ethics or quick fixes.

The book's framework moves from **Private Victory** (Habits 1-3: Be Proactive, Begin with the End in Mind, Put First Things First) to **Public Victory** (Habits 4-6: Think Win-Win, Seek First to Understand Then to Be Understood, Synergize) and culminates in **Renewal** (Habit 7: Sharpen the Saw).

Covey introduces the **Maturity Continuum** from dependence to independence to interdependence. True effectiveness requires moving beyond independence to interdependence—recognizing that the highest achievements require collaboration.""",
        "framework": "Private Victory → Public Victory → Renewal",
        "takeaways": [
            {"title": "Be Proactive (Habit 1)", "text": "Between stimulus and response lies your freedom to choose. Focus on your Circle of Influence, not your Circle of Concern. Take initiative and responsibility for your life."},
            {"title": "Begin with the End in Mind (Habit 2)", "text": "Create a personal mission statement based on principles and values. Live with the end in mind—imagine your own funeral. What do you want people to say about you?"},
            {"title": "Put First Things First (Habit 3)", "text": "Organize around priorities using the Time Management Matrix. Focus on Quadrant II (important but not urgent) activities like planning, relationship building, and prevention."},
            {"title": "Think Win-Win (Habit 4)", "text": "Seek mutual benefit in all interactions. Abundance mentality believes there's plenty for everyone. Win-Win or No Deal preserves relationships."},
            {"title": "Seek First to Understand (Habit 5)", "text": "Practice empathic listening before seeking to be understood. Diagnose before you prescribe. Listen with intent to understand, not intent to reply."}
        ],
        "quotes": [
            "Most people do not listen with the intent to understand; they listen with the intent to reply.",
            "I am not a product of my circumstances. I am a product of my decisions.",
            "The key is not to prioritize what's on your schedule, but to schedule your priorities."
        ],
        "actions": [
            "Write your personal mission statement",
            "Identify one Quadrant II activity to prioritize",
            "Practice empathic listening in your next conversation",
            "List three things in your Circle of Influence to act on",
            "Conduct a weekly review of your roles and goals"
        ],
        "analogies": [
            {"concept": "The Maturity Continuum", "analogy": "Like stages of child development", "explanation": "Dependence is infancy (relying on others), independence is adolescence (self-reliance), and interdependence is maturity (collaborative achievement)."}
        ],
        "visual_map": '''
        digraph "7 Habits" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            dependence [label="DEPENDENCE\\nYou take care of me", fillcolor="#FFB6C1"]
            
            private [label="PRIVATE VICTORY", fillcolor="#E8E8E8", shape=folder]
            h1 [label="1. Be Proactive", fillcolor="#98FB98"]
            h2 [label="2. Begin with End", fillcolor="#87CEEB"]
            h3 [label="3. First Things First", fillcolor="#FFE4B5"]
            
            independence [label="INDEPENDENCE\\nI take care of me", fillcolor="#DDA0DD"]
            
            public [label="PUBLIC VICTORY", fillcolor="#E8E8E8", shape=folder]
            h4 [label="4. Win-Win", fillcolor="#98FB98"]
            h5 [label="5. Understand First", fillcolor="#87CEEB"]
            h6 [label="6. Synergize", fillcolor="#FFE4B5"]
            
            interdependence [label="INTERDEPENDENCE\\nWe achieve together", fillcolor="#FFD700"]
            
            h7 [label="7. Sharpen the Saw\\n(Renewal)", fillcolor="#F0E68C"]
            
            dependence -> private
            private -> h1 -> h2 -> h3
            h3 -> independence
            independence -> public
            public -> h4 -> h5 -> h6
            h6 -> interdependence
            h7 -> h1 [style=dashed, label="continuous\\nimprovement"]
        }
        '''
    },
    
    "How to Win Friends and Influence People": {
        "author": "Dale Carnegie",
        "genre": "self-help",
        "year": 1936,
        "rating": 4.7,
        "time": 15,
        "cover": "https://m.media-amazon.com/images/I/71vK0WVQ4rL._SL1500_.jpg",
        "overview": "Carnegie's timeless principles for improving relationships and influencing people through genuine interest and appreciation.",
        "executive": """**How to Win Friends and Influence People** is the original people skills handbook. Dale Carnegie presents fundamental techniques for handling people, making them like you, winning them to your way of thinking, and changing their behavior without arousing resentment.

The core principle: **People crave genuine appreciation and importance**. They want to feel valued. The fundamental technique is to become genuinely interested in other people, see things from their perspective, and make them feel important—sincerely.

Carnegie teaches that criticism is futile because it puts people on the defensive and wounds their pride. Instead, use indirect methods: call attention to mistakes indirectly, let the other person save face, and praise improvements.""",
        "framework": "Techniques for Handling People",
        "takeaways": [
            {"title": "Don't Criticize, Condemn or Complain", "text": "Criticism is futile because it puts people on the defensive and makes them strive to justify themselves. It wounds pride, hurts sense of importance, and arouses resentment."},
            {"title": "Give Honest and Sincere Appreciation", "text": "The deepest principle in human nature is the craving to be appreciated. Give honest, sincere appreciation. Make the other person feel important—and do it sincerely."},
            {"title": "Arouse in the Other Person an Eager Want", "text": "The only way to influence others is to talk about what they want and show them how to get it. See things from their perspective."},
            {"title": "Remember Names", "text": "A person's name is the sweetest sound to them. Remember it and use it frequently. It makes people feel valued and important."},
            {"title": "Be a Good Listener", "text": "Encourage others to talk about themselves. Ask questions. Be genuinely interested. People will like you for listening more than for talking."}
        ],
        "quotes": [
            "You can make more friends in two months by becoming interested in other people than you can in two years by trying to get other people interested in you.",
            "People rarely succeed unless they have fun in what they are doing.",
            "Any fool can criticize, complain, and condemn—and most fools do. But it takes character and self-control to be understanding and forgiving."
        ],
        "actions": [
            "Compliment three people sincerely today",
            "Ask someone about their interests and truly listen",
            "Practice remembering and using people's names",
            "Find one thing to appreciate in a difficult person",
            "Smile more—it's contagious"
        ],
        "analogies": [
            {"concept": "Appreciation vs Flattery", "analogy": "Like food vs candy", "explanation": "Appreciation is nourishing and comes from the heart. Flattery is sweet but shallow, coming only from the mouth. One is valued, the other arouses suspicion."}
        ],
        "visual_map": '''
        digraph "Win Friends" {
            rankdir=LR
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            you [label="YOU", fillcolor="#E8E8E8"]
            
            techniques [label="CARNEGIE'S\\nTECHNIQUES", shape=folder, fillcolor="#FFE4B5"]
            
            appreciate [label="Sincere\\nAppreciation", fillcolor="#98FB98"]
            listen [label="Active\\nListening", fillcolor="#87CEEB"]
            names [label="Remember\\nNames", fillcolor="#DDA0DD"]
            perspective [label="Their\\nPerspective", fillcolor="#FFB6C1"]
            smile [label="Smile\\nGenuinely", fillcolor="#F0E68C"]
            
            results [label="RESULTS\\nInfluence\\nFriendships\\nSuccess", fillcolor="#FFD700"]
            
            you -> techniques
            techniques -> appreciate
            techniques -> listen
            techniques -> names
            techniques -> perspective
            techniques -> smile
            appreciate -> results
            listen -> results
            names -> results
            perspective -> results
            smile -> results
        }
        '''
    },
    
    "The Power of Now": {
        "author": "Eckhart Tolle",
        "genre": "self-help",
        "year": 1997,
        "rating": 4.6,
        "time": 14,
        "cover": "https://m.media-amazon.com/images/I/71QY6z2gcVL._SL1500_.jpg",
        "overview": "A spiritual guide to transcending the ego and living fully in the present moment.",
        "executive": """**The Power of Now** teaches that the present moment is all we ever have. Psychological time—dwelling on the past or worrying about the future—is the source of suffering. The **ego** thrives on psychological time and creates a false sense of self.

Tolle argues that we are not our thoughts. We are the awareness behind thoughts. By observing the mind without judgment, we can break identification with the thinking mind and access **Presence**—a state of intense alertness and consciousness.

The book provides practical teachings for accessing the Now: observe the breath, feel the inner body, create gaps in the stream of thinking, and accept the present moment as if you had chosen it.""",
        "framework": "Presence Over Ego",
        "takeaways": [
            {"title": "You Are Not Your Mind", "text": "The greatest obstacle to enlightenment is identification with the mind. You are not your thoughts—you are the awareness that observes thoughts. Create gaps in thinking to access Presence."},
            {"title": "The Present Moment is All There Is", "text": "Past and future are mental constructs. Only the Now is real. All negativity is caused by an accumulation of psychological time and denial of the present."},
            {"title": "The Pain-Body", "text": "Old emotional pain lives on in the form of a pain-body. It feeds on negative thinking and drama. Observe it without judgment to dissolve it."},
            {"title": "Acceptance vs Resistance", "text": "Whatever the present moment contains, accept it as if you had chosen it. Resistance creates suffering. Surrender doesn't mean passive—it means wise action from acceptance."},
            {"title": "The Inner Body", "text": "Feel the aliveness within your body. This anchors you in the Now and creates a portal out of thinking into Being."}
        ],
        "quotes": [
            "Realize deeply that the present moment is all you ever have.",
            "The primary cause of unhappiness is never the situation but your thoughts about it.",
            "You are not your mind."
        ],
        "actions": [
            "Practice observing your thoughts for 5 minutes daily",
            "Feel your breath—it's always in the Now",
            "Accept one situation today without mental resistance",
            "Feel the aliveness in your hands for 30 seconds",
            "Create gaps in thinking throughout the day"
        ],
        "analogies": [
            {"concept": "Consciousness vs Mind", "analogy": "Like the sky vs clouds", "explanation": "Consciousness is the vast sky—always present, always peaceful. Thoughts are clouds passing through. You are the sky, not the clouds."}
        ],
        "visual_map": '''
        digraph "Power of Now" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            ego [label="🎭 EGO\\nFalse self\\nPsychological time\\nIdentified with mind", fillcolor="#FFB6C1"]
            
            suffering [label="SUFFERING\\nResistance\\nPain-body\\nCompulsive thinking", fillcolor="#FF6B6B"]
            
            awareness [label="👁️ AWARENESS\\nObserve thoughts\\nCreate gaps\\nFeel inner body", fillcolor="#FFE4B5"]
            
            now [label="⏰ THE NOW\\nPresent moment\\nAcceptance\\nSurrender", fillcolor="#98FB98"]
            
            presence [label="✨ PRESENCE\\nInner peace\\nBeing\\nEnlightenment", fillcolor="#FFD700"]
            
            ego -> suffering
            suffering -> awareness [label="observe", style=dashed]
            awareness -> now
            now -> presence
            presence -> awareness [label="deepens", style=dashed]
        }
        '''
    },
    
    "Man's Search for Meaning": {
        "author": "Viktor Frankl",
        "genre": "self-help",
        "year": 1946,
        "rating": 4.8,
        "time": 12,
        "cover": "https://m.media-amazon.com/images/I/81dDwAzxByL._SL1500_.jpg",
        "overview": "Frankl's profound account of his Holocaust experience and his psychotherapeutic method of finding meaning in all forms of existence.",
        "executive": """**Man's Search for Meaning** chronicles psychiatrist Viktor Frankl's experiences as a concentration camp inmate and describes his psychotherapeutic method of finding meaning in all forms of existence, even the most brutal.

Frankl observed that those who survived the camps were not necessarily the physically strongest, but those who had **meaning** to live for—a task, a mission, someone to love. This led to his therapeutic approach: **Logotherapy**, which holds that the primary motivational force in humans is the search for meaning.

The book teaches that we cannot avoid suffering, but we can choose how to cope with it, find meaning in it, and move forward. Between stimulus and response lies our freedom to choose our attitude.""",
        "framework": "Logotherapy - The Search for Meaning",
        "takeaways": [
            {"title": "Life Has Meaning Under All Circumstances", "text": "Even in suffering, meaning can be found. The last of human freedoms is to choose one's attitude in any given set of circumstances."},
            {"title": "Our Main Motivation is Meaning", "text": "The primary drive in humans is not pleasure (Freud) or power (Adler) but the search for meaning. A person with a why can bear almost any how."},
            {"title": "We Detect Meaning, We Don't Create It", "text": "Meaning is discovered, not invented. It exists objectively and must be detected through conscience. Each person's meaning is unique and specific."},
            {"title": "The Attitude We Take Matters Most", "text": "When we can't change a situation, we must change ourselves. Suffering ceases to be suffering the moment it finds meaning, such as sacrifice."},
            {"title": "Three Sources of Meaning", "text": "Meaning can be found in: (1) creating work or doing a deed, (2) experiencing something or loving someone, (3) the attitude we take toward unavoidable suffering."}
        ],
        "quotes": [
            "When we are no longer able to change a situation, we are challenged to change ourselves.",
            "Those who have a 'why' to live, can bear with almost any 'how'.",
            "Everything can be taken from a man but one thing: the last of the human freedoms—to choose one's attitude in any given set of circumstances."
        ],
        "actions": [
            "Identify your unique life purpose or mission",
            "Find meaning in a current challenge you're facing",
            "Connect with someone you love deeply",
            "Pursue a worthy goal that serves others",
            "Reflect on what gives your life meaning"
        ],
        "analogies": [
            {"concept": "Freedom to Choose", "analogy": "Like the space between stimulus and response", "explanation": "No matter what happens to you (stimulus), there's a space before you react (response). In that space lies your power to choose your attitude and meaning."}
        ],
        "visual_map": '''
        digraph "Search for Meaning" {
            rankdir=TB
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            suffering [label="💔 SUFFERING\\nInevitable\\nUnavoidable", fillcolor="#FFB6C1"]
            
            freedom [label="🔓 FREEDOM\\nChoose attitude\\nFind meaning", fillcolor="#FFE4B5"]
            
            sources [label="SOURCES OF\\nMEANING", shape=folder, fillcolor="#E8E8E8"]
            
            creative [label="Creative Work\\nDoing a deed", fillcolor="#98FB98"]
            experiential [label="Love & Beauty\\nExperiencing", fillcolor="#87CEEB"]
            attitudinal [label="Attitude\\nSuffering with dignity", fillcolor="#DDA0DD"]
            
            purpose [label="🎯 PURPOSE\\nReason to live\\nWhy to endure", fillcolor="#FFD700"]
            
            suffering -> freedom
            freedom -> sources
            sources -> creative
            sources -> experiential
            sources -> attitudinal
            creative -> purpose
            experiential -> purpose
            attitudinal -> purpose
        }
        '''
    },
    
    "Mindset": {
        "author": "Carol Dweck",
        "genre": "self-help",
        "year": 2006,
        "rating": 4.6,
        "time": 16,
        "cover": "https://m.media-amazon.com/images/I/71KvP+sDKZL._SL1500_.jpg",
        "overview": "Dweck's research on the power of our beliefs and how changing mindsets can transform our lives.",
        "executive": """**Mindset** reveals how success in school, work, sports, arts, and relationships depends on understanding a simple concept: your view of yourself can determine everything. Psychologist Carol Dweck discovered that people have either a **fixed mindset** or a **growth mindset**.

Those with a **fixed mindset** believe intelligence and talent are fixed traits. They avoid challenges, give up easily, see effort as fruitless, ignore criticism, and feel threatened by others' success. This limits achievement.

Those with a **growth mindset** believe abilities can be developed through dedication and hard work. They embrace challenges, persist through setbacks, see effort as mastery's path, learn from criticism, and find inspiration in others' success. This leads to higher achievement.""",
        "framework": "Fixed vs Growth Mindset",
        "takeaways": [
            {"title": "Fixed Mindset Limits Potential", "text": "Believing intelligence is fixed creates urgency to prove yourself. Challenges become threats. Failure becomes identity. This mindset says: 'If I fail, I am a failure.'"},
            {"title": "Growth Mindset Enables Development", "text": "Believing abilities can grow through effort creates desire to learn. Challenges become opportunities. Setbacks become feedback. This mindset says: 'Failure is a chance to grow.'"},
            {"title": "Effort is the Path to Mastery", "text": "In a fixed mindset, needing effort means lack of talent. In a growth mindset, effort ignites ability and turns it into accomplishment. Effort creates ability."},
            {"title": "The Power of 'Yet'", "text": "Adding 'yet' to statements transforms mindset: 'I can't do this... yet.' It acknowledges current reality while affirming future potential through learning."},
            {"title": "Praise Process, Not Traits", "text": "Praising intelligence ('You're so smart!') creates fixed mindset. Praising process ('You tried hard!') creates growth mindset. Focus on effort, strategy, and progress."}
        ],
        "quotes": [
            "Becoming is better than being.",
            "The view you adopt for yourself profoundly affects the way you lead your life.",
            "In a growth mindset, challenges are exciting rather than threatening."
        ],
       "actions": [
            "Identify one area where you have a fixed mindset",
            "Replace 'I can't' with 'I can't yet' this week",
            "Choose a challenge you've been avoiding and tackle it",
            "Learn from someone who succeeded where you struggled",
            "Praise effort and strategy, not just results"
        ],
        "analogies": [
            {"concept": "Brain Plasticity", "analogy": "Like a muscle that grows", "explanation": "The brain is like a muscle—the more you use it and challenge it, the stronger and more capable it becomes. Intelligence isn't fixed; it expands with effort."}
        ],
        "visual_map": '''
        digraph "Mindset" {
            rankdir=LR
            node [shape=box, style="rounded,filled", fontname="Arial"]
            
            challenge [label="CHALLENGE", fillcolor="#E8E8E8"]
            
            fixed [label="FIXED MINDSET\\nIntelligence is static", fillcolor="#FFB6C1", shape=ellipse]
            growth [label="GROWTH MINDSET\\nIntelligence develops", fillcolor="#98FB98", shape=ellipse]
            
            fixed_path [label="❌ Avoid Challenges\\n❌ Give Up Easily\\n❌ Effort = Fruitless\\n❌ Ignore Feedback\\n❌ Threatened by Success", fillcolor="#FF6B6B"]
            
            growth_path [label="✅ Embrace Challenges\\n✅ Persist\\n✅ Effort = Mastery\\n✅ Learn from Criticism\\n✅ Inspired by Others", fillcolor="#4ECDC4"]
            
            plateau [label="PLATEAU\\nLimited achievement", fillcolor="#CCCCCC"]
            success [label="SUCCESS\\nHigher achievement", fillcolor="#FFD700"]
            
            challenge -> fixed
            challenge -> growth
            fixed -> fixed_path -> plateau
            growth -> growth_path -> success
        }
        '''
    }
}
