"""
Sitemap generator for BookWise.
Generates sitemap.xml for SEO optimization.
"""

import os
from datetime import datetime
from typing import Optional
from database.queries import get_all_genres, get_all_books
from database.connection import get_db_session


def generate_sitemap(
    base_url: str = "https://bookwise.app",
    output_path: Optional[str] = None
) -> str:
    """
    Generate sitemap.xml content.
    
    Args:
        base_url: Base URL of the website
        output_path: Optional path to save the sitemap file
    
    Returns:
        str: XML content of the sitemap
    """
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Start XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    
    # Static pages
    static_pages = [
        {"url": "/", "priority": "1.0", "changefreq": "daily"},
        {"url": "/Categories", "priority": "0.9", "changefreq": "weekly"},
        {"url": "/About", "priority": "0.6", "changefreq": "monthly"},
        {"url": "/Privacy", "priority": "0.3", "changefreq": "yearly"},
        {"url": "/Terms", "priority": "0.3", "changefreq": "yearly"},
    ]
    
    for page in static_pages:
        xml_lines.append(f"""  <url>
    <loc>{base_url}{page['url']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>""")
    
    # Genre pages
    genres = get_all_genres()
    for genre in genres:
        xml_lines.append(f"""  <url>
    <loc>{base_url}/Categories?name={genre.slug}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")
    
    # Book pages
    books = get_all_books()
    for book in books:
        xml_lines.append(f"""  <url>
    <loc>{base_url}/Book_Detail?slug={book.slug}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""")
    
    # Close XML
    xml_lines.append("</urlset>")
    
    sitemap_content = "\n".join(xml_lines)
    
    # Save to file if path provided
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print(f"✅ Sitemap saved to: {output_path}")
    
    return sitemap_content


def generate_robots_txt(
    base_url: str = "https://bookwise.app",
    output_path: Optional[str] = None
) -> str:
    """
    Generate robots.txt content.
    
    Args:
        base_url: Base URL of the website
        output_path: Optional path to save the robots.txt file
    
    Returns:
        str: Content of robots.txt
    """
    content = f"""# BookWise Robots.txt
# Generated: {datetime.now().strftime("%Y-%m-%d")}

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

# Sitemap
Sitemap: {base_url}/sitemap.xml

# Crawl-delay (optional, for polite crawling)
Crawl-delay: 1
"""
    
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Robots.txt saved to: {output_path}")
    
    return content


def get_sitemap_stats() -> dict:
    """
    Get statistics about sitemap content.
    
    Returns:
        dict: Statistics about URLs in the sitemap
    """
    genres = get_all_genres()
    books = get_all_books()
    
    return {
        "static_pages": 5,
        "genre_pages": len(genres),
        "book_pages": len(books),
        "total_urls": 5 + len(genres) + len(books)
    }


if __name__ == "__main__":
    # Generate and save sitemap
    import sys
    from pathlib import Path
    
    # Get project root
    project_root = Path(__file__).parent.parent
    
    # Generate sitemap
    sitemap_path = project_root / "sitemap.xml"
    generate_sitemap(output_path=str(sitemap_path))
    
    # Generate robots.txt
    robots_path = project_root / "robots.txt"
    generate_robots_txt(output_path=str(robots_path))
    
    # Print stats
    stats = get_sitemap_stats()
    print(f"\n📊 Sitemap Statistics:")
    print(f"   Static Pages: {stats['static_pages']}")
    print(f"   Genre Pages: {stats['genre_pages']}")
    print(f"   Book Pages: {stats['book_pages']}")
    print(f"   Total URLs: {stats['total_urls']}")
