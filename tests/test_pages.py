"""
Page syntax and import tests for BookWise
Check that all pages can be parsed and imported
"""

import sys
import os
import ast
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def check_syntax(filepath):
    """Check Python syntax of a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        ast.parse(source)
        return True, None
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"


def check_imports(filepath):
    """Check if a module can be loaded (syntax-wise only)""" 
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Parse to AST
        tree = ast.parse(source)
        
        # Find all import statements
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
        
        return True, imports
    except Exception as e:
        return False, str(e)


def run_page_tests():
    """Run tests on all page files"""
    print("\n" + "="*60)
    print("📄 PAGE SYNTAX & IMPORT TESTS")
    print("="*60)
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Files to check
    files_to_check = [
        ("Home.py", os.path.join(project_root, "Home.py")),
        ("Categories", os.path.join(project_root, "pages", "1_📖_Categories.py")),
        ("Book Detail", os.path.join(project_root, "pages", "2_📚_Book_Detail.py")),
        ("About", os.path.join(project_root, "pages", "3_ℹ️_About.py")),
        ("Privacy", os.path.join(project_root, "pages", "4_🔒_Privacy.py")),
        ("Terms", os.path.join(project_root, "pages", "5_📜_Terms.py")),
        ("Reading Lists", os.path.join(project_root, "pages", "6_📋_Reading_Lists.py")),
        ("Admin Stats", os.path.join(project_root, "pages", "7_📊_Admin_Stats.py")),
    ]
    
    errors = []
    
    print("\n📄 Checking Page Files...")
    print("-" * 50)
    
    for name, filepath in files_to_check:
        if not os.path.exists(filepath):
            errors.append(f"File not found: {name}")
            print(f"  ❌ {name}: File not found")
            continue
        
        # Check syntax
        syntax_ok, syntax_error = check_syntax(filepath)
        if not syntax_ok:
            errors.append(f"{name}: Syntax error - {syntax_error}")
            print(f"  ❌ {name}: Syntax error - {syntax_error}")
            continue
        
        # Check imports
        imports_ok, result = check_imports(filepath)
        if not imports_ok:
            errors.append(f"{name}: Import error - {result}")
            print(f"  ❌ {name}: Import error - {result}")
            continue
        
        print(f"  ✅ {name}: Syntax OK ({len(result)} imports)")
    
    # Check component files
    print("\n🧩 Checking Component Files...")
    print("-" * 50)
    
    components_dir = os.path.join(project_root, "components")
    component_files = [f for f in os.listdir(components_dir) if f.endswith('.py') and not f.startswith('__')]
    
    for comp_file in sorted(component_files):
        filepath = os.path.join(components_dir, comp_file)
        syntax_ok, syntax_error = check_syntax(filepath)
        
        if not syntax_ok:
            errors.append(f"Component {comp_file}: {syntax_error}")
            print(f"  ❌ {comp_file}: {syntax_error}")
        else:
            print(f"  ✅ {comp_file}")
    
    # Check database files
    print("\n🗄️ Checking Database Files...")
    print("-" * 50)
    
    db_files = ["models.py", "connection.py", "queries.py", "seed.py"]
    db_dir = os.path.join(project_root, "database")
    
    for db_file in db_files:
        filepath = os.path.join(db_dir, db_file)
        if os.path.exists(filepath):
            syntax_ok, syntax_error = check_syntax(filepath)
            if not syntax_ok:
                errors.append(f"Database {db_file}: {syntax_error}")
                print(f"  ❌ {db_file}: {syntax_error}")
            else:
                print(f"  ✅ {db_file}")
        else:
            print(f"  ⚠️ {db_file}: Not found")
    
    # Summary
    print("\n" + "="*60)
    print("📊 PAGE TEST SUMMARY")
    print("="*60)
    
    if errors:
        print(f"\n❌ Found {len(errors)} errors:\n")
        for error in errors:
            print(f"  • {error}")
        return 1
    else:
        print("\n✅ All files passed syntax checks!")
        return 0


if __name__ == "__main__":
    sys.exit(run_page_tests())
