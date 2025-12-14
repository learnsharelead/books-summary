"""
SQLAlchemy models for the BookWise database.
Defines Genre, Book, Summary, and SummaryImage models.
"""

from datetime import datetime
from typing import Optional, List
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean,
    Enum,
    create_engine,
)
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()


class DifficultyLevel(enum.Enum):
    """Difficulty levels for book summaries."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class SectionType(enum.Enum):
    """Types of sections for summary images."""
    CONCEPT = "concept"
    TAKEAWAY = "takeaway"
    OVERVIEW = "overview"


class Genre(Base):
    """
    Genre model representing book categories.
    
    Attributes:
        id: Unique identifier
        name: Display name of the genre
        slug: URL-friendly identifier
        description: SEO-optimized description
        image_url: Genre cover/icon image
        icon: Emoji icon for the genre
        books: Related books in this genre
    """
    __tablename__ = "genres"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100), nullable=False, unique=True)
    slug: str = Column(String(100), nullable=False, unique=True, index=True)
    description: str = Column(Text, nullable=False)
    image_url: Optional[str] = Column(String(500), nullable=True)
    icon: str = Column(String(10), default="📚")
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    books = relationship("Book", back_populates="genre", lazy="dynamic")
    
    def __repr__(self) -> str:
        return f"<Genre(name='{self.name}', slug='{self.slug}')>"
    
    @property
    def book_count(self) -> int:
        """Return the number of books in this genre."""
        return self.books.count()


class Book(Base):
    """
    Book model representing individual books.
    
    Attributes:
        id: Unique identifier
        title: Book title
        author: Book author name
        slug: URL-friendly identifier
        cover_image_url: Book cover image URL
        isbn: ISBN number (optional)
        publication_year: Year of publication
        genre_id: Foreign key to genre
        is_featured: Whether to feature on homepage
        summary: Related summary
    """
    __tablename__ = "books"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(300), nullable=False)
    author: str = Column(String(200), nullable=False)
    slug: str = Column(String(300), nullable=False, unique=True, index=True)
    cover_image_url: Optional[str] = Column(String(500), nullable=True)
    cover_image_fallback: Optional[str] = Column(String(500), nullable=True)
    isbn: Optional[str] = Column(String(20), nullable=True)
    publication_year: Optional[int] = Column(Integer, nullable=True)
    genre_id: int = Column(Integer, ForeignKey("genres.id"), nullable=False)
    is_featured: bool = Column(Boolean, default=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    genre = relationship("Genre", back_populates="books")
    summary = relationship("Summary", back_populates="book", uselist=False)
    
    def __repr__(self) -> str:
        return f"<Book(title='{self.title}', author='{self.author}')>"
    
    def get_cover_url(self) -> str:
        """Return cover image URL with fallback."""
        return self.cover_image_url or self.cover_image_fallback or "/assets/images/placeholder.png"


class Summary(Base):
    """
    Summary model representing book summaries.
    
    Attributes:
        id: Unique identifier
        book_id: Foreign key to book
        overview_text: Brief overview/intro
        main_content: Main summary content (markdown)
        key_takeaways: JSON/text list of key takeaways
        who_should_read: Target audience description
        difficulty: Reading difficulty level
        reading_time: Estimated reading time in minutes
        seo_title: SEO-optimized title
        seo_description: SEO meta description
        images: Related concept images
    """
    __tablename__ = "summaries"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    book_id: int = Column(Integer, ForeignKey("books.id"), nullable=False, unique=True)
    overview_text: str = Column(Text, nullable=False)
    main_content: str = Column(Text, nullable=False)
    key_takeaways: str = Column(Text, nullable=False)  # JSON string
    who_should_read: str = Column(Text, nullable=False)
    difficulty: str = Column(String(20), default="intermediate")
    reading_time: int = Column(Integer, default=10)  # minutes
    rating: float = Column(Integer, default=4.8) # 0.0 to 5.0
    
    # Rich Content Fields (JSON/Text)
    executive_summary: str = Column(Text, nullable=True) # The "60-second read"
    quote_of_the_book: str = Column(Text, nullable=True)
    analogies: str = Column(Text, nullable=True) # JSON: [{concept, analogy, explanation}]
    quotes: str = Column(Text, nullable=True) # JSON: [string]
    action_steps: str = Column(Text, nullable=True) # JSON: [string]
    
    seo_title: Optional[str] = Column(String(200), nullable=True)
    seo_description: Optional[str] = Column(String(500), nullable=True)
    workflow_data: Optional[str] = Column(Text, nullable=True)  # Graphviz DOT
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    book = relationship("Book", back_populates="summary")
    images = relationship("SummaryImage", back_populates="summary", lazy="dynamic")
    
    def __repr__(self) -> str:
        return f"<Summary(book_id={self.book_id}, reading_time={self.reading_time}min)>"


class SummaryImage(Base):
    """
    SummaryImage model for concept and takeaway images.
    
    Attributes:
        id: Unique identifier
        summary_id: Foreign key to summary
        image_url: Image URL
        section_type: Type of section (concept/takeaway)
        section_title: Title of the related section
        alt_text: Accessibility alt text
        caption: Image caption
        order: Display order
    """
    __tablename__ = "summary_images"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    summary_id: int = Column(Integer, ForeignKey("summaries.id"), nullable=False)
    image_url: str = Column(String(500), nullable=False)
    section_type: str = Column(String(20), nullable=False)  # concept, takeaway, overview
    section_title: str = Column(String(200), nullable=False)
    alt_text: Optional[str] = Column(String(300), nullable=True)
    caption: Optional[str] = Column(String(300), nullable=True)
    order: int = Column(Integer, default=0)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    summary = relationship("Summary", back_populates="images")
    
    def __repr__(self) -> str:
        return f"<SummaryImage(section='{self.section_title}', type='{self.section_type}')>"
