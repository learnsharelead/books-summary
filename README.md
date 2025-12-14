# 📚 BookWise - Curated Book Summary Platform

A production-ready, SEO-optimized book summary website built with Streamlit.

![BookWise Banner](https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1200&h=400&fit=crop)

## ✨ Features

- **11 Major Genres** with 50+ famous books pre-loaded
- **SEO-Optimized Pages** with meta tags and structured data
- **Rich Visual Experience** with book covers and concept images
- **Expert-Written Summaries** with key takeaways
- **Responsive Design** optimized for all devices
- **Production-Ready** code with type hints and docstrings

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/bookwise.git
cd bookwise

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database with seed data
python -m database.seed

# Run the application
streamlit run Home.py
```

## 📁 Project Structure

```
books-summary/
├── Home.py                     # Main entry point
├── requirements.txt            # Dependencies
├── .streamlit/
│   └── config.toml            # Streamlit configuration
├── assets/
│   └── css/
│       └── styles.css         # Custom styling
├── components/
│   ├── __init__.py
│   ├── seo.py                 # SEO meta components
│   ├── book_card.py           # Book display cards
│   ├── genre_card.py          # Genre display cards
│   └── image_handler.py       # Image loading utilities
├── database/
│   ├── __init__.py
│   ├── models.py              # SQLAlchemy models
│   ├── connection.py          # Database connection
│   ├── seed.py                # Seed data loader
│   └── queries.py             # Database queries
├── pages/
│   ├── 1_📖_Categories.py     # Genre listing page
│   ├── 2_📚_Book_Detail.py    # Individual book page
│   ├── 3_ℹ️_About.py          # About page
│   ├── 4_🔒_Privacy.py        # Privacy policy
│   └── 5_📜_Terms.py          # Terms of service
└── utils/
    ├── __init__.py
    ├── helpers.py             # Utility functions
    └── seo_content.py         # SEO text content
```

## 🎨 Design Features

- **Dark Mode** with vibrant accent colors
- **Glassmorphism** card effects
- **Smooth Animations** on hover and load
- **Responsive Grid** layouts
- **Lazy Loading** for images

## 📊 Database Schema

- **Genre**: Categories with SEO descriptions
- **Book**: Titles with cover images
- **Summary**: Structured content sections
- **SummaryImage**: Visual aids for concepts

## 🔍 SEO Implementation

- Dynamic page titles
- Meta descriptions
- Open Graph tags
- JSON-LD structured data
- Clean URL structure

## ☁️ Deployment

### Streamlit Community Cloud

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set `Home.py` as main file
5. Deploy!

### Docker

```bash
docker build -t bookwise .
docker run -p 8501:8501 bookwise
```

## 📄 License

MIT License - See LICENSE file
