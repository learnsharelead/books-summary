"""
Database connection management for BookWise.
Provides session management and database initialization.
"""

import os
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from database.models import Base

# Database file path
DB_DIR = Path(__file__).parent.parent / "data"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "bookwise.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Create engine with SQLite-specific settings
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL debugging
    connect_args={"check_same_thread": False}  # Required for SQLite + threading
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """
    Initialize the database by creating all tables.
    
    This function should be called once during application startup
    or when running the seed script.
    """
    Base.metadata.create_all(bind=engine)


def drop_db() -> None:
    """
    Drop all database tables.
    
    WARNING: This will delete all data. Use with caution.
    """
    Base.metadata.drop_all(bind=engine)


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """
    Context manager for database sessions.
    
    Provides automatic session management with commit on success
    and rollback on failure.
    
    Usage:
        with get_db_session() as session:
            genres = session.query(Genre).all()
    
    Yields:
        Session: SQLAlchemy session object
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_session() -> Session:
    """
    Get a new database session.
    
    Note: Caller is responsible for closing the session.
    Prefer using get_db_session() context manager instead.
    
    Returns:
        Session: New SQLAlchemy session
    """
    return SessionLocal()
