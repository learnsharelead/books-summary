"""
Test Runner for BookWise Unit Tests
Runs all test modules and generates a comprehensive report.
"""

import pytest
import sys
import os
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    """Run all unit tests and display results"""
    print("\n" + "=" * 70)
    print("🧪 BOOKWISE COMPREHENSIVE UNIT TESTS")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Get test directory
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List of test modules to run
    test_modules = [
        "test_database_queries.py",
        "test_database_models.py",
        "test_components_detailed.py",
        "test_services_detailed.py",
        "test_utilities_detailed.py",
        "test_all.py",
        "test_services.py",
        "test_integration.py",
    ]
    
    # Filter to only existing files
    existing_tests = [
        os.path.join(test_dir, t)
        for t in test_modules
        if os.path.exists(os.path.join(test_dir, t))
    ]
    
    print(f"\n📝 Running {len(existing_tests)} test modules:\n")
    for test in existing_tests:
        print(f"   • {os.path.basename(test)}")
    
    print("\n" + "-" * 70 + "\n")
    
    # Run pytest with verbose output
    exit_code = pytest.main([
        *existing_tests,
        "-v",
        "--tb=short",
        "-x",  # Stop on first failure
        "--color=yes",
    ])
    
    print("\n" + "=" * 70)
    if exit_code == 0:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED!")
    print("=" * 70 + "\n")
    
    return exit_code


def run_quick_tests():
    """Run a quick subset of tests"""
    print("\n" + "=" * 70)
    print("🚀 BOOKWISE QUICK TEST RUN")
    print("=" * 70)
    
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Quick test modules
    quick_tests = [
        os.path.join(test_dir, "test_database_queries.py"),
        os.path.join(test_dir, "test_components_detailed.py"),
    ]
    
    existing_tests = [t for t in quick_tests if os.path.exists(t)]
    
    exit_code = pytest.main([
        *existing_tests,
        "-v",
        "--tb=line",
        "-q",
    ])
    
    return exit_code


def run_coverage_tests():
    """Run tests with coverage reporting"""
    print("\n" + "=" * 70)
    print("📊 BOOKWISE TEST COVERAGE")
    print("=" * 70)
    
    test_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(test_dir)
    
    exit_code = pytest.main([
        test_dir,
        "-v",
        "--cov=" + project_dir,
        "--cov-report=term-missing",
        "--cov-report=html",
    ])
    
    print("\n📁 Coverage HTML report generated in 'htmlcov' directory")
    
    return exit_code


def run_specific_test(test_name: str):
    """Run a specific test module"""
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(test_dir, test_name)
    
    if not os.path.exists(test_file):
        print(f"❌ Test file not found: {test_name}")
        return 1
    
    print(f"\n🧪 Running: {test_name}\n")
    
    return pytest.main([test_file, "-v", "--tb=short"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg == "--quick":
            exit_code = run_quick_tests()
        elif arg == "--coverage":
            exit_code = run_coverage_tests()
        elif arg.endswith(".py"):
            exit_code = run_specific_test(arg)
        else:
            print("Usage: python run_all_tests.py [--quick|--coverage|test_file.py]")
            exit_code = 1
    else:
        exit_code = run_all_tests()
    
    sys.exit(exit_code)
