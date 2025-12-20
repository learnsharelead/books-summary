"""
Smart Recommendation Engine for BookWise.
Content-based filtering with genre, author, and keyword similarity.
"""

import json
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict
import streamlit as st


@dataclass
class BookScore:
    """Represents a book with its recommendation score."""
    book: any  # Book model
    score: float
    reasons: List[str]


class RecommendationEngine:
    """
    Smart recommendation engine using content-based filtering.
    Analyzes genre, author, keywords, and reading patterns.
    """
    
    # Keyword weights for different content types
    KEYWORD_WEIGHTS = {
        'title': 3.0,
        'takeaways': 2.5,
        'analogies': 2.0,
        'quotes': 1.5,
        'content': 1.0
    }
    
    def __init__(self):
        self._book_cache = {}
        self._keyword_index = defaultdict(list)
        self._author_index = defaultdict(list)
        self._genre_index = defaultdict(list)
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract meaningful keywords from text."""
        if not text:
            return []
        
        # Common stop words to filter
        stop_words = {
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare',
            'ought', 'used', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by',
            'from', 'up', 'about', 'into', 'over', 'after', 'and', 'but', 'or',
            'as', 'if', 'when', 'than', 'because', 'while', 'where', 'so', 'this',
            'that', 'these', 'those', 'it', 'its', 'you', 'your', 'we', 'our',
            'they', 'their', 'what', 'which', 'who', 'how', 'all', 'each', 'every',
            'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'not',
            'only', 'own', 'same', 'just', 'also', 'very', 'much', 'many'
        }
        
        # Extract words
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        
        # Filter and clean
        keywords = [w for w in words if w not in stop_words]
        
        # Get unique keywords while preserving order
        seen = set()
        unique = []
        for k in keywords:
            if k not in seen:
                seen.add(k)
                unique.append(k)
        
        return unique[:50]  # Limit to top 50 keywords
    
    def _calculate_keyword_similarity(
        self, 
        book1_keywords: List[str], 
        book2_keywords: List[str]
    ) -> float:
        """Calculate Jaccard similarity between keyword sets."""
        if not book1_keywords or not book2_keywords:
            return 0.0
        
        set1 = set(book1_keywords)
        set2 = set(book2_keywords)
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union if union > 0 else 0.0
    
    def get_book_keywords(self, book, summary) -> List[str]:
        """Extract all keywords from a book and its summary."""
        all_text = []
        
        # Title and author
        all_text.append(book.title)
        all_text.append(book.author)
        
        if summary:
            # Add summary content
            if summary.executive_summary:
                all_text.append(summary.executive_summary)
            if summary.main_content:
                all_text.append(summary.main_content)
            if summary.who_should_read:
                all_text.append(summary.who_should_read)
            
            # Parse JSON fields
            for field in ['key_takeaways', 'analogies', 'quotes', 'action_steps']:
                value = getattr(summary, field, None)
                if value:
                    try:
                        parsed = json.loads(value) if isinstance(value, str) else value
                        if isinstance(parsed, list):
                            for item in parsed:
                                if isinstance(item, dict):
                                    all_text.extend(str(v) for v in item.values())
                                else:
                                    all_text.append(str(item))
                    except:
                        all_text.append(str(value))
        
        combined = ' '.join(all_text)
        return self._extract_keywords(combined)
    
    def get_recommendations(
        self,
        current_book,
        current_summary,
        all_books: List,
        limit: int = 6
    ) -> List[BookScore]:
        """
        Get smart recommendations based on current book.
        
        Args:
            current_book: The book user is viewing
            current_summary: Summary of current book
            all_books: List of all available books
            limit: Maximum recommendations to return
            
        Returns:
            List of BookScore with scores and reasons
        """
        from database.queries import get_summary_for_book
        
        recommendations = []
        
        # Get current book's keywords and metadata
        current_keywords = self.get_book_keywords(current_book, current_summary)
        current_genre = current_book.genre.slug if hasattr(current_book, 'genre') and current_book.genre else None
        current_author = current_book.author.lower() if current_book.author else None
        
        for book in all_books:
            # Skip the current book
            if book.id == current_book.id:
                continue
            
            score = 0.0
            reasons = []
            
            # Same genre bonus (40% weight)
            try:
                if current_genre and hasattr(book, 'genre') and book.genre:
                    if book.genre.slug == current_genre:
                        score += 40.0
                        reasons.append(f"Same genre: {book.genre.name}")
            except Exception:
                pass
            
            # Same author bonus (30% weight)
            if current_author and book.author:
                if book.author.lower() == current_author:
                    score += 30.0
                    reasons.append(f"Same author: {book.author}")
                elif any(name in book.author.lower() for name in current_author.split()):
                    score += 15.0
                    reasons.append("Related author")
            
            # Keyword similarity (30% weight)
            # Get summary properly via query function
            try:
                book_summary = get_summary_for_book(book.id)
                if book_summary:
                    book_keywords = self.get_book_keywords(book, book_summary)
                    similarity = self._calculate_keyword_similarity(current_keywords, book_keywords)
                    keyword_score = similarity * 30.0
                    if keyword_score > 5:
                        score += keyword_score
                        if similarity > 0.2:
                            reasons.append("Similar themes")
                        elif similarity > 0.1:
                            reasons.append("Related topics")
            except Exception:
                pass
            
            # Publication year proximity bonus (small)
            try:
                if current_book.publication_year and book.publication_year:
                    year_diff = abs(current_book.publication_year - book.publication_year)
                    if year_diff <= 5:
                        score += 5.0
                        reasons.append("Similar era")
            except Exception:
                pass
            
            if score > 0:
                recommendations.append(BookScore(
                    book=book,
                    score=score,
                    reasons=reasons[:3]  # Top 3 reasons
                ))
        
        # Sort by score descending
        recommendations.sort(key=lambda x: x.score, reverse=True)
        
        return recommendations[:limit]
    
    def get_personalized_recommendations(
        self,
        user_history: List[str],  # List of book slugs user has read
        all_books: List,
        limit: int = 6
    ) -> List[BookScore]:
        """
        Get recommendations based on user's reading history.
        
        Args:
            user_history: Slugs of books user has read/liked
            all_books: All available books
            limit: Max recommendations
            
        Returns:
            List of recommended books
        """
        if not user_history:
            # Return top-rated books as fallback
            from database.queries import get_top_rated_books, get_summary_for_book
            top_books = get_top_rated_books(limit=limit)
            return [BookScore(book=b, score=100, reasons=["Top Rated"]) for b in top_books]
        
        from database.queries import get_summary_for_book
        
        # Aggregate preferences from reading history
        genre_counts = defaultdict(int)
        author_counts = defaultdict(int)
        all_keywords = []
        read_ids = set()
        
        for book in all_books:
            if book.slug in user_history:
                read_ids.add(book.id)
                try:
                    if hasattr(book, 'genre') and book.genre:
                        genre_counts[book.genre.slug] += 1
                except Exception:
                    pass
                if book.author:
                    author_counts[book.author.lower()] += 1
                try:
                    summary = get_summary_for_book(book.id)
                    if summary:
                        all_keywords.extend(self.get_book_keywords(book, summary))
                except Exception:
                    pass
        
        # Score all unread books
        recommendations = []
        
        for book in all_books:
            if book.id in read_ids:
                continue
            
            score = 0.0
            reasons = []
            
            # Genre preference
            try:
                if hasattr(book, 'genre') and book.genre:
                    genre_score = genre_counts.get(book.genre.slug, 0) * 20
                    if genre_score > 0:
                        score += genre_score
                        reasons.append(f"You like {book.genre.name}")
            except Exception:
                pass
            
            # Author preference
            if book.author and author_counts.get(book.author.lower(), 0) > 0:
                score += 25
                reasons.append(f"You've read {book.author}")
            
            # Keyword overlap
            if all_keywords:
                try:
                    book_summary = get_summary_for_book(book.id)
                    if book_summary:
                        book_keywords = self.get_book_keywords(book, book_summary)
                        overlap = len(set(all_keywords) & set(book_keywords))
                        if overlap > 5:
                            score += min(overlap * 2, 30)
                            reasons.append("Matches your interests")
                except Exception:
                    pass
            
            if score > 0:
                recommendations.append(BookScore(
                    book=book,
                    score=score,
                    reasons=reasons[:3]
                ))
        
        recommendations.sort(key=lambda x: x.score, reverse=True)
        return recommendations[:limit]


def render_smart_recommendations(
    current_book,
    current_summary,
    show_reasons: bool = True
) -> None:
    """
    Render smart recommendations UI component.
    
    Args:
        current_book: Currently viewed book
        current_summary: Summary of current book
        show_reasons: Whether to show recommendation reasons
    """
    from database.queries import get_all_books
    from components.image_handler import load_image_safe
    
    try:
        engine = RecommendationEngine()
        all_books = get_all_books()
        
        recommendations = engine.get_recommendations(
            current_book=current_book,
            current_summary=current_summary,
            all_books=all_books,
            limit=4
        )
        
        if not recommendations:
            st.info("No recommendations available yet. Check back as we add more books!")
            return
    except Exception as e:
        st.warning(f"Could not load recommendations. Please try again.")
        return
    
    st.markdown("""
    <div style="margin-top: 24px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
            <span style="font-size: 24px;">🎯</span>
            <span style="font-size: 18px; font-weight: 700; color: #1e293b;">
                Smart Recommendations
            </span>
            <span style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                font-size: 10px;
                padding: 2px 8px;
                border-radius: 10px;
                font-weight: 600;
            ">AI POWERED</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4, gap="small")
    for idx, rec in enumerate(recommendations):
        book = rec.book
        with cols[idx]:
            safe_image = load_image_safe(book.cover_image_url, "book")
            
            # Build reasons text (simpler approach)
            reasons_text = ""
            if show_reasons and rec.reasons:
                reasons_text = " • ".join(rec.reasons)
            
            # Card HTML
            st.markdown(f"""<div style="background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
<div style="position: relative; padding-top: 130%; background: #f8fafc;">
<img src="{safe_image}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
<div style="position: absolute; top: 8px; right: 8px; background: rgba(102, 126, 234, 0.95); color: white; font-size: 10px; padding: 3px 8px; border-radius: 10px; font-weight: 600;">{int(rec.score)}% match</div>
</div>
<div style="padding: 12px;">
<h4 style="font-size: 13px; font-weight: 700; color: #1e293b; line-height: 1.3; margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{book.title}</h4>
<p style="font-size: 11px; color: #64748b; margin: 4px 0 0 0;">{book.author}</p>
</div>
</div>""", unsafe_allow_html=True)
            
            # Reasons shown separately with simpler markup
            if reasons_text:
                st.caption(f"🎯 {reasons_text}")
            
            st.link_button("Read Summary", f"/Book_Detail?slug={book.slug}", use_container_width=True)
