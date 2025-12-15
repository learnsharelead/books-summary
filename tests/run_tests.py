"""
Master Test Runner for BookWise
Runs all test suites and generates a report
"""

import sys
import os
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    """Run all test suites"""
    print("=" * 70)
    print("🧪 BOOKWISE MASTER TEST RUNNER")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    start_time = time.time()
    all_passed = True
    
    # Import test modules
    from tests.test_all import run_all_tests as run_unit_tests
    from tests.test_integration import run_integration_tests
    from tests.test_pages import run_page_tests
    
    # Run unit tests
    print("\n" + "="*70)
    print("1️⃣ UNIT TESTS")
    print("="*70)
    results = run_unit_tests()
    if results["failed"] > 0:
        all_passed = False
    
    # Run integration tests  
    print("\n" + "="*70)
    print("2️⃣ INTEGRATION TESTS")
    print("="*70)
    errors = run_integration_tests()
    if errors:
        all_passed = False
    
    # Run page tests
    print("\n" + "="*70)
    print("3️⃣ PAGE SYNTAX TESTS")
    print("="*70)
    page_result = run_page_tests()
    if page_result != 0:
        all_passed = False
    
    # Final summary
    elapsed = time.time() - start_time
    
    print("\n" + "=" * 70)
    print("📊 FINAL TEST REPORT")
    print("=" * 70)
    print(f"\n⏱️ Total time: {elapsed:.2f} seconds")
    
    if all_passed:
        print("\n✅ ALL TESTS PASSED! 🎉")
        print("\nThe BookWise application is functioning correctly.")
    else:
        print("\n❌ SOME TESTS FAILED!")
        print("\nPlease review the errors above and fix them.")
    
    print("\n" + "=" * 70)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
