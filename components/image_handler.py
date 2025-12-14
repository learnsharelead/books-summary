"""
Image handling utilities for BookWise.
Provides safe image loading with fallbacks and browser-mimicking requests.
"""

import requests
from typing import Optional
from functools import lru_cache


PLACEHOLDER_IMAGES = {
    "book": "https://placehold.co/300x450/EEE/31343C?text=Book+Cover",
    "concept": "https://images.unsplash.com/photo-1456324504439-367cee3b3c32?w=800", # Open Book
    "takeaway": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
    "genre": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600",
}


@lru_cache(maxsize=100)
def check_image_url(url: str, timeout: int = 5) -> bool:
    """
    Check if an image URL is accessible using browser headers.
    
    Args:
        url: Image URL to check
        timeout: Request timeout in seconds
    
    Returns:
        bool: True if image is accessible
    """
    try:
        # Use browser headers to avoid 403 blocks from Amazon/firewalls
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.head(url, timeout=timeout, allow_redirects=True, headers=headers)
        return response.status_code == 200
    except Exception:
        # Fallback to simple GET if HEAD fails (some servers block HEAD)
        try:
             response = requests.get(url, timeout=timeout, stream=True, headers=headers)
             response.close()
             return response.status_code == 200
        except:
            return False


def load_image_safe(
    url: Optional[str],
    fallback_type: str = "book"
) -> str:
    """
    Load image URL with fallback.
    
    Args:
        url: Primary image URL
        fallback_type: Type of fallback image
    
    Returns:
        str: Valid image URL
    """
    if url and check_image_url(url):
        return url
    return get_placeholder_image(fallback_type)


def get_placeholder_image(image_type: str = "book") -> str:
    """
    Get placeholder image URL.
    
    Args:
        image_type: Type of placeholder needed
    
    Returns:
        str: Placeholder image URL
    """
    return PLACEHOLDER_IMAGES.get(image_type, PLACEHOLDER_IMAGES["book"])


def get_open_library_cover(isbn: str, size: str = "L") -> str:
    """
    Get book cover URL from Open Library.
    
    Args:
        isbn: Book ISBN
        size: Cover size (S, M, L)
    
    Returns:
        str: Open Library cover URL
    """
    return f"https://covers.openlibrary.org/b/isbn/{isbn}-{size}.jpg"


def get_unsplash_image(query: str, width: int = 800) -> str:
    """
    Get generic image URL for a concept (static reliable fallbacks).
    (Source.unsplash API is deprecated, so we use reliable static images)
    
    Args:
        query: Search query (unused in fallback)
        width: Image width
    
    Returns:
        str: Unsplash image URL
    """
    return "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=800"
