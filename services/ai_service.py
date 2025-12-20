"""
AI Service for BookWise - Gemini-powered RAG Chat.
Enables conversational interaction with book content.
"""

import os
import json
import streamlit as st
from typing import Optional, List, Dict, Any
from dataclasses import dataclass


@dataclass
class ChatMessage:
    """Represents a chat message."""
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: Optional[str] = None


class AIService:
    """
    AI Service for book-related queries using Gemini.
    Implements RAG (Retrieval-Augmented Generation) for book chat.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize AI Service with optional API key."""
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
        self.model = None
        self._initialized = False
        
    def initialize(self) -> bool:
        """Initialize the Gemini model."""
        if self._initialized:
            return True
            
        if not self.api_key:
            return False
            
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            self._initialized = True
            return True
        except Exception as e:
            print(f"Failed to initialize Gemini: {e}")
            return False
    
    def create_book_context(self, book_data: Dict[str, Any]) -> str:
        """Create a rich context string from book data for RAG."""
        context_parts = []
        
        # Book metadata
        context_parts.append(f"BOOK TITLE: {book_data.get('title', 'Unknown')}")
        context_parts.append(f"AUTHOR: {book_data.get('author', 'Unknown')}")
        context_parts.append(f"GENRE: {book_data.get('genre', 'Unknown')}")
        context_parts.append(f"PUBLICATION YEAR: {book_data.get('year', 'Unknown')}")
        
        # Summary content
        if book_data.get('executive_summary'):
            context_parts.append(f"\nEXECUTIVE SUMMARY:\n{book_data['executive_summary']}")
        
        if book_data.get('main_content'):
            context_parts.append(f"\nMAIN CONTENT:\n{book_data['main_content']}")
        
        # Key takeaways
        if book_data.get('takeaways'):
            takeaways = book_data['takeaways']
            if isinstance(takeaways, str):
                try:
                    takeaways = json.loads(takeaways)
                except:
                    pass
            if isinstance(takeaways, list):
                context_parts.append("\nKEY TAKEAWAYS:")
                for i, t in enumerate(takeaways, 1):
                    if isinstance(t, dict):
                        context_parts.append(f"{i}. {t.get('title', '')}: {t.get('text', '')}")
                    else:
                        context_parts.append(f"{i}. {t}")
        
        # Analogies
        if book_data.get('analogies'):
            analogies = book_data['analogies']
            if isinstance(analogies, str):
                try:
                    analogies = json.loads(analogies)
                except:
                    pass
            if isinstance(analogies, list) and analogies:
                context_parts.append("\nANALOGIES & MENTAL MODELS:")
                for a in analogies:
                    if isinstance(a, dict):
                        context_parts.append(f"- {a.get('concept', '')}: {a.get('analogy', '')} - {a.get('explanation', '')}")
        
        # Quotes
        if book_data.get('quotes'):
            quotes = book_data['quotes']
            if isinstance(quotes, str):
                try:
                    quotes = json.loads(quotes)
                except:
                    pass
            if isinstance(quotes, list) and quotes:
                context_parts.append("\nNOTABLE QUOTES:")
                for q in quotes[:5]:
                    context_parts.append(f'- "{q}"')
        
        # Action steps
        if book_data.get('action_steps'):
            actions = book_data['action_steps']
            if isinstance(actions, str):
                try:
                    actions = json.loads(actions)
                except:
                    pass
            if isinstance(actions, list) and actions:
                context_parts.append("\nACTION STEPS:")
                for i, a in enumerate(actions, 1):
                    context_parts.append(f"{i}. {a}")
        
        # Who should read
        if book_data.get('who_should_read'):
            context_parts.append(f"\nWHO SHOULD READ:\n{book_data['who_should_read']}")
        
        return "\n".join(context_parts)
    
    def chat_with_book(
        self, 
        user_message: str, 
        book_data: Dict[str, Any],
        chat_history: List[ChatMessage] = None
    ) -> str:
        """
        Chat with a book using RAG.
        
        Args:
            user_message: The user's question
            book_data: Dictionary containing book and summary data
            chat_history: Previous messages in the conversation
            
        Returns:
            AI response string
        """
        if not self.initialize():
            return "⚠️ AI service not available. Please configure your GEMINI_API_KEY in environment variables or Streamlit secrets."
        
        # Create book context
        book_context = self.create_book_context(book_data)
        
        # Build conversation history
        history_text = ""
        if chat_history:
            history_text = "\n\nPREVIOUS CONVERSATION:\n"
            for msg in chat_history[-6:]:  # Last 6 messages for context
                history_text += f"{msg.role.upper()}: {msg.content}\n"
        
        # Create system prompt
        system_prompt = f"""You are BookWise AI, an expert assistant specialized in discussing books and their insights.

You have complete knowledge of the following book:

{book_context}

INSTRUCTIONS:
1. Answer questions ONLY based on the book content provided above
2. Be helpful, insightful, and engaging
3. Use specific examples, quotes, and concepts from the book
4. If asked about something not in the book, politely say so
5. Relate concepts to practical, real-world applications
6. Keep responses concise but informative (2-3 paragraphs max)
7. Use markdown formatting for better readability
{history_text}

USER QUESTION: {user_message}

Provide a helpful, accurate response based on the book content:"""

        try:
            response = self.model.generate_content(system_prompt)
            return response.text
        except Exception as e:
            return f"❌ Error generating response: {str(e)}"
    
    def generate_quiz(self, book_data: Dict[str, Any], num_questions: int = 5) -> List[Dict]:
        """Generate a quiz based on book content."""
        if not self.initialize():
            return []
        
        book_context = self.create_book_context(book_data)
        
        prompt = f"""Based on this book summary, generate {num_questions} multiple choice questions to test understanding.

BOOK CONTENT:
{book_context}

Generate questions in this JSON format:
[
  {{
    "question": "Question text here",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "correct": "A",
    "explanation": "Why this is correct"
  }}
]

Return ONLY valid JSON, no other text:"""

        try:
            response = self.model.generate_content(prompt)
            # Parse JSON from response
            text = response.text.strip()
            # Remove markdown code blocks if present
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            return json.loads(text)
        except Exception as e:
            print(f"Quiz generation error: {e}")
            return []
    
    def summarize_for_audio(self, book_data: Dict[str, Any]) -> str:
        """Generate a concise, audio-friendly summary."""
        if not self.initialize():
            # Fallback to executive summary
            return book_data.get('executive_summary', book_data.get('overview', ''))
        
        book_context = self.create_book_context(book_data)
        
        prompt = f"""Create a 2-minute audio-friendly summary of this book. 
The summary should:
- Be conversational and easy to listen to
- Cover the most important concepts
- Include 2-3 key takeaways
- End with a memorable insight

BOOK CONTENT:
{book_context}

Write the audio summary (about 300 words):"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except:
            return book_data.get('executive_summary', book_data.get('overview', ''))


def get_ai_service() -> AIService:
    """Get or create AI service instance."""
    if 'ai_service' not in st.session_state:
        st.session_state.ai_service = AIService()
    return st.session_state.ai_service
