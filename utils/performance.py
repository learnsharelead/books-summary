"""
Performance Optimization Utilities for BookWise.
Includes caching, lazy loading, and query optimization helpers.
"""

import streamlit as st
from functools import wraps
from typing import Any, Callable, Optional
import time
import hashlib


# ============================================================================
# ADVANCED CACHING
# ============================================================================

def cached_component(ttl: int = 300, key_prefix: str = ""):
    """
    Decorator for caching component outputs.
    
    Args:
        ttl: Time to live in seconds
        key_prefix: Prefix for cache key
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key from function name and arguments
            key_parts = [key_prefix, func.__name__, str(args), str(sorted(kwargs.items()))]
            cache_key = hashlib.md5("".join(key_parts).encode()).hexdigest()
            
            # Check if cached
            cache_attr = f"_cache_{cache_key}"
            time_attr = f"_cache_time_{cache_key}"
            
            if hasattr(st.session_state, cache_attr):
                cached_time = getattr(st.session_state, time_attr, 0)
                if time.time() - cached_time < ttl:
                    return getattr(st.session_state, cache_attr)
            
            # Execute and cache
            result = func(*args, **kwargs)
            setattr(st.session_state, cache_attr, result)
            setattr(st.session_state, time_attr, time.time())
            
            return result
        return wrapper
    return decorator


def clear_component_cache(key_prefix: str = "") -> int:
    """Clear cached components with given prefix. Returns count cleared."""
    cleared = 0
    keys_to_delete = []
    
    for key in st.session_state.keys():
        if key.startswith(f"_cache_{key_prefix}"):
            keys_to_delete.append(key)
            cleared += 1
    
    for key in keys_to_delete:
        del st.session_state[key]
    
    return cleared


# ============================================================================
# LAZY LOADING
# ============================================================================

def lazy_load_section(section_id: str, placeholder_height: int = 200) -> bool:
    """
    Implement lazy loading for a section using Intersection Observer.
    Returns True if section should be rendered.
    
    Args:
        section_id: Unique ID for the section
        placeholder_height: Height of placeholder in pixels
    """
    state_key = f"lazy_loaded_{section_id}"
    
    if state_key not in st.session_state:
        st.session_state[state_key] = False
    
    if not st.session_state[state_key]:
        # Render placeholder with intersection observer
        st.markdown(f"""
        <div id="{section_id}" style="min-height: {placeholder_height}px; display: flex; align-items: center; justify-content: center; background: #f8fafc; border-radius: 8px; margin: 8px 0;">
            <div style="text-align: center; color: #94a3b8;">
                <div style="font-size: 24px; margin-bottom: 8px;">⏳</div>
                <div style="font-size: 13px;">Loading...</div>
            </div>
        </div>
        <script>
            (function() {{
                const observer = new IntersectionObserver((entries) => {{
                    entries.forEach(entry => {{
                        if (entry.isIntersecting) {{
                            // Trigger Streamlit rerun to load content
                            const element = entry.target;
                            element.innerHTML = '<div style="text-align: center; padding: 20px; color: #667eea;">Content loading...</div>';
                            // Mark as loaded for next render
                            if (window.parent && window.parent.postMessage) {{
                                window.parent.postMessage({{type: 'streamlit:setComponentValue', value: true}}, '*');
                            }}
                            observer.unobserve(element);
                        }}
                    }});
                }}, {{threshold: 0.1}});
                
                const element = document.getElementById('{section_id}');
                if (element) observer.observe(element);
            }})();
        </script>
        """, unsafe_allow_html=True)
        
        # For now, always return True to render (full lazy loading requires JS integration)
        st.session_state[state_key] = True
        return True
    
    return True


# ============================================================================
# IMAGE OPTIMIZATION
# ============================================================================

def get_optimized_image_url(url: str, width: int = 300, quality: int = 80) -> str:
    """
    Generate optimized image URL using common CDN patterns.
    Works with Unsplash, Imgix, and other services.
    
    Args:
        url: Original image URL
        width: Target width
        quality: JPEG quality (1-100)
    """
    if not url:
        return ""
    
    # Unsplash optimization
    if "unsplash.com" in url:
        # Remove existing params
        base_url = url.split("?")[0]
        return f"{base_url}?w={width}&q={quality}&auto=format"
    
    # Already has optimization params
    if "w=" in url or "width=" in url:
        return url
    
    # Generic: add width param if URL-like
    if "?" in url:
        return f"{url}&w={width}"
    
    return url


def generate_srcset(url: str, sizes: list = None) -> str:
    """
    Generate srcset attribute for responsive images.
    
    Args:
        url: Base image URL
        sizes: List of widths to generate
    """
    if sizes is None:
        sizes = [320, 480, 640, 960, 1280]
    
    srcset_parts = []
    for size in sizes:
        optimized_url = get_optimized_image_url(url, width=size)
        srcset_parts.append(f"{optimized_url} {size}w")
    
    return ", ".join(srcset_parts)


# ============================================================================
# QUERY OPTIMIZATION
# ============================================================================

class QueryTimer:
    """Context manager for timing database queries."""
    
    def __init__(self, query_name: str = "Query"):
        self.query_name = query_name
        self.start_time = None
        self.end_time = None
        self.duration = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.duration = (self.end_time - self.start_time) * 1000  # ms
        
        # Store in session state for analytics
        if "query_times" not in st.session_state:
            st.session_state.query_times = []
        
        st.session_state.query_times.append({
            "name": self.query_name,
            "duration_ms": round(self.duration, 2),
            "timestamp": time.time()
        })
        
        # Keep only last 100 queries
        st.session_state.query_times = st.session_state.query_times[-100:]


def get_query_stats() -> dict:
    """Get query performance statistics."""
    if "query_times" not in st.session_state:
        return {"total": 0, "avg_ms": 0, "max_ms": 0, "min_ms": 0}
    
    queries = st.session_state.query_times
    if not queries:
        return {"total": 0, "avg_ms": 0, "max_ms": 0, "min_ms": 0}
    
    durations = [q["duration_ms"] for q in queries]
    
    return {
        "total": len(queries),
        "avg_ms": round(sum(durations) / len(durations), 2),
        "max_ms": round(max(durations), 2),
        "min_ms": round(min(durations), 2)
    }


# ============================================================================
# PREFETCHING
# ============================================================================

def prefetch_data(*data_funcs: Callable) -> None:
    """
    Prefetch data in parallel for anticipated user navigation.
    
    Args:
        data_funcs: Functions to call for prefetching
    """
    for func in data_funcs:
        try:
            func()
        except Exception:
            pass  # Silently fail prefetch


# ============================================================================
# RENDER OPTIMIZATION
# ============================================================================

def render_virtual_list(items: list, render_func: Callable, items_per_page: int = 20) -> None:
    """
    Render a virtualized list for large datasets.
    
    Args:
        items: List of items to render
        render_func: Function to render each item
        items_per_page: Number of visible items
    """
    state_key = "virtual_list_offset"
    
    if state_key not in st.session_state:
        st.session_state[state_key] = 0
    
    offset = st.session_state[state_key]
    visible_items = items[offset:offset + items_per_page]
    
    # Render visible items
    for item in visible_items:
        render_func(item)
    
    # Load more button
    if offset + items_per_page < len(items):
        if st.button("Load More", key=f"load_more_{offset}"):
            st.session_state[state_key] = offset + items_per_page
            st.rerun()


# ============================================================================
# PERFORMANCE MONITORING
# ============================================================================

def render_performance_debug() -> None:
    """Render performance debugging info (for development)."""
    stats = get_query_stats()
    
    st.sidebar.markdown("### ⚡ Performance")
    st.sidebar.markdown(f"""
    - **Queries:** {stats['total']}
    - **Avg Time:** {stats['avg_ms']}ms
    - **Max Time:** {stats['max_ms']}ms
    """)


def get_page_load_time() -> float:
    """Get approximate page load time."""
    if "page_start_time" not in st.session_state:
        st.session_state.page_start_time = time.time()
        return 0
    
    return (time.time() - st.session_state.page_start_time) * 1000


# ============================================================================
# MEMORY OPTIMIZATION
# ============================================================================

def limit_session_state_size(max_keys: int = 1000) -> None:
    """Limit session state size to prevent memory issues."""
    if len(st.session_state) > max_keys:
        # Remove old cache entries
        cache_keys = [k for k in st.session_state.keys() if k.startswith("_cache_")]
        for key in cache_keys[:len(cache_keys) // 2]:
            del st.session_state[key]
