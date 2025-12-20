"""
Pagination Component for BookWise.
Provides reusable pagination for book lists and categories.
"""

import streamlit as st
from typing import List, Any, Tuple, Optional
from dataclasses import dataclass
import math


@dataclass
class PaginationConfig:
    """Configuration for pagination."""
    items_per_page: int = 12
    max_visible_pages: int = 5
    show_first_last: bool = True
    show_page_size_selector: bool = False
    page_size_options: List[int] = None
    
    def __post_init__(self):
        if self.page_size_options is None:
            self.page_size_options = [6, 12, 24, 48]


def get_pagination_state(key: str) -> dict:
    """Get pagination state for a specific key."""
    state_key = f"pagination_{key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "current_page": 1,
            "items_per_page": 12
        }
    return st.session_state[state_key]


def set_page(key: str, page: int) -> None:
    """Set current page for a pagination key."""
    state = get_pagination_state(key)
    state["current_page"] = page


def set_items_per_page(key: str, items_per_page: int) -> None:
    """Set items per page and reset to page 1."""
    state = get_pagination_state(key)
    state["items_per_page"] = items_per_page
    state["current_page"] = 1


def paginate_items(
    items: List[Any],
    key: str,
    config: PaginationConfig = None
) -> Tuple[List[Any], int, int]:
    """
    Paginate a list of items.
    
    Args:
        items: Full list of items
        key: Unique key for pagination state
        config: Pagination configuration
        
    Returns:
        Tuple of (paginated_items, current_page, total_pages)
    """
    if config is None:
        config = PaginationConfig()
    
    state = get_pagination_state(key)
    items_per_page = state.get("items_per_page", config.items_per_page)
    current_page = state.get("current_page", 1)
    
    total_items = len(items)
    total_pages = max(1, math.ceil(total_items / items_per_page))
    
    # Ensure current page is valid
    current_page = max(1, min(current_page, total_pages))
    state["current_page"] = current_page
    
    # Calculate slice
    start_idx = (current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    paginated_items = items[start_idx:end_idx]
    
    return paginated_items, current_page, total_pages


def render_pagination(
    key: str,
    total_items: int,
    config: PaginationConfig = None,
    show_info: bool = True
) -> None:
    """
    Render pagination controls.
    
    Args:
        key: Unique key for pagination state
        total_items: Total number of items
        config: Pagination configuration
        show_info: Whether to show "Showing X-Y of Z" text
    """
    if config is None:
        config = PaginationConfig()
    
    state = get_pagination_state(key)
    items_per_page = state.get("items_per_page", config.items_per_page)
    current_page = state.get("current_page", 1)
    
    total_pages = max(1, math.ceil(total_items / items_per_page))
    current_page = max(1, min(current_page, total_pages))
    
    # Calculate display range
    start_item = (current_page - 1) * items_per_page + 1
    end_item = min(current_page * items_per_page, total_items)
    
    # Container for pagination
    st.markdown("""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 16px;
        padding: 20px 0;
        flex-wrap: wrap;
    ">
    """, unsafe_allow_html=True)
    
    # Pagination layout
    cols = st.columns([2, 6, 2] if show_info else [1, 8, 1])
    
    # Left: Info text
    if show_info:
        with cols[0]:
            st.markdown(f"""
            <div style="
                font-size: 13px;
                color: #64748b;
                white-space: nowrap;
            ">
                Showing <strong>{start_item}-{end_item}</strong> of <strong>{total_items}</strong>
            </div>
            """, unsafe_allow_html=True)
    
    # Center: Page buttons
    with cols[1]:
        _render_page_buttons(key, current_page, total_pages, config)
    
    # Right: Page size selector
    if config.show_page_size_selector:
        with cols[2]:
            new_size = st.selectbox(
                "Per page",
                options=config.page_size_options,
                index=config.page_size_options.index(items_per_page) if items_per_page in config.page_size_options else 0,
                key=f"{key}_page_size",
                label_visibility="collapsed"
            )
            if new_size != items_per_page:
                set_items_per_page(key, new_size)
                st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)


def _render_page_buttons(
    key: str,
    current_page: int,
    total_pages: int,
    config: PaginationConfig
) -> None:
    """Render the page number buttons."""
    
    if total_pages <= 1:
        return
    
    # Calculate visible page range
    half_visible = config.max_visible_pages // 2
    start_page = max(1, current_page - half_visible)
    end_page = min(total_pages, start_page + config.max_visible_pages - 1)
    
    # Adjust if we're near the end
    if end_page - start_page < config.max_visible_pages - 1:
        start_page = max(1, end_page - config.max_visible_pages + 1)
    
    # Build button layout
    button_cols = []
    
    # Previous button
    if current_page > 1:
        button_cols.append(("←", current_page - 1, False))
    
    # First page + ellipsis
    if config.show_first_last and start_page > 1:
        button_cols.append(("1", 1, False))
        if start_page > 2:
            button_cols.append(("...", None, True))
    
    # Page numbers
    for page in range(start_page, end_page + 1):
        button_cols.append((str(page), page, page == current_page))
    
    # Last page + ellipsis
    if config.show_first_last and end_page < total_pages:
        if end_page < total_pages - 1:
            button_cols.append(("...", None, True))
        button_cols.append((str(total_pages), total_pages, False))
    
    # Next button
    if current_page < total_pages:
        button_cols.append(("→", current_page + 1, False))
    
    # Render buttons
    cols = st.columns(len(button_cols))
    
    for idx, (label, page, is_current) in enumerate(button_cols):
        with cols[idx]:
            if page is None:  # Ellipsis
                st.markdown(f"""
                <div style="
                    text-align: center;
                    padding: 8px;
                    color: #64748b;
                    font-size: 14px;
                ">{label}</div>
                """, unsafe_allow_html=True)
            else:
                button_style = """
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                """ if is_current else """
                    background: white;
                    color: #475569;
                    border: 1px solid #e2e8f0;
                """
                
                if st.button(
                    label,
                    key=f"{key}_page_{label}_{idx}",
                    use_container_width=True,
                    disabled=is_current
                ):
                    set_page(key, page)
                    st.rerun()


def render_compact_pagination(
    key: str,
    total_items: int,
    items_per_page: int = 12
) -> Tuple[int, int]:
    """
    Render a compact pagination (just prev/next).
    Returns (current_page, total_pages).
    """
    state = get_pagination_state(key)
    state["items_per_page"] = items_per_page
    current_page = state.get("current_page", 1)
    
    total_pages = max(1, math.ceil(total_items / items_per_page))
    current_page = max(1, min(current_page, total_pages))
    
    if total_pages <= 1:
        return current_page, total_pages
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if current_page > 1:
            if st.button("← Previous", key=f"{key}_prev", use_container_width=True):
                set_page(key, current_page - 1)
                st.rerun()
    
    with col2:
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 8px;
            font-size: 14px;
            font-weight: 600;
            color: #1e293b;
        ">
            Page {current_page} of {total_pages}
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if current_page < total_pages:
            if st.button("Next →", key=f"{key}_next", use_container_width=True):
                set_page(key, current_page + 1)
                st.rerun()
    
    return current_page, total_pages


def reset_pagination(key: str) -> None:
    """Reset pagination to page 1."""
    set_page(key, 1)
