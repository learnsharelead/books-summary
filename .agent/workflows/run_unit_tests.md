---
description: How to run the comprehensive unit test suite
---
1. Navigate to the project root directory:
   ```bash
   cd c:\Workspace\books-summary
   ```

2. Run the custom test runner script:
   ```bash
   python tests/run_all_tests.py
   ```
   This script runs all test modules and provides a summary report.

3. To run specific test subsets:
   - **Quick Run** (Database & Components only):
     ```bash
     python tests/run_all_tests.py --quick
     ```
   - **Coverage Report**:
     ```bash
     python tests/run_all_tests.py --coverage
     ```
   - **Specific Test File**:
     ```bash
     python tests/run_all_tests.py test_services_detailed.py
     ```

4. Alternatively, you can use `pytest` directly:
   ```bash
   python -m pytest tests/ -v
   ```

## Test Files Structure

- `tests/test_database_queries.py`: Tests for `database/queries.py`
- `tests/test_database_models.py`: Tests for `database/models.py`
- `tests/test_components_detailed.py`: Tests for UI components
- `tests/test_services_detailed.py`: Tests for AI, TTS, and Recommendation services
- `tests/test_utilities_detailed.py`: Tests for helper utility functions
- `tests/test_pwa_theme_pagination.py`: Tests for PWA, Theme, Pagination, and SEO
- `tests/test_integration.py`: High-level integration tests

## Key Features

- **Mocking**: External services (Gemini AI, Streamlit Session State) are mocked to ensure tests are fast and reliable.
- **Data Integrity**: Tests verify that database models and relationships are correctly defined.
- **Edge Cases**: Special characters, empty lists, and invalid inputs are tested.
