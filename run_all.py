"""
Run All Script - Climate Impact on Illinois Corn Production Analysis
Executes all Jupyter notebooks in the correct sequence

This script provides automated reproduction of the complete analysis workflow.
Works on Windows, macOS, and Linux without special configuration.

Usage:
    python run_all.py

Requirements:
    - Python 3.8+
    - pip install -r requirements.txt
    - NOAA API token set in 01_GSOM_Acquisition.ipynb
    - NASS data manually downloaded to data/raw/
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(message):
    """Print a formatted header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{message}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_step(step_num, message):
    """Print a step message"""
    print(f"{Colors.BOLD}{Colors.GREEN}[Step {step_num}]{Colors.END} {message}")

def print_success(message):
    """Print a success message"""
    print(f"{Colors.GREEN}Success: {message}{Colors.END}")

def print_warning(message):
    """Print a warning message"""
    print(f"{Colors.YELLOW}Warning: {message}{Colors.END}")

def print_error(message):
    """Print an error message"""
    print(f"{Colors.RED}Error: {message}{Colors.END}")

def check_python_version():
    """Check Python version"""
    if sys.version_info >= (3, 8):
        print_success(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        return True
    else:
        print_error(f"Python 3.8+ required. You have {sys.version_info.major}.{sys.version_info.minor}")
        return False

def check_packages():
    """Check if required packages are installed"""
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn',
        'scipy', 'sklearn', 'requests', 'nbconvert'
    ]
    
    missing = []
    for pkg in required_packages:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    
    if missing:
        print_error(f"Missing packages: {', '.join(missing)}")
        print_error("Install with: pip install -r requirements.txt")
        return False
    
    print_success("All required packages installed")
    return True

def check_jupyter():
    """Check if Jupyter is installed"""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'jupyter', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print_success("Jupyter installed")
            return True
        else:
            print_error("Jupyter command failed")
            return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print_error("Jupyter not found. Install with: pip install jupyter")
        return False

def check_nbconvert():
    """Check if nbconvert command works"""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'nbconvert', '--help'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print_success("nbconvert command works")
            return True
        else:
            print_error("nbconvert command failed")
            return False
    except Exception as e:
        print_error(f"Error testing nbconvert: {e}")
        return False

def check_file_structure():
    """Check if required files and directories exist"""
    required_items = [
        ("Notebooks", "dir"),
        ("Notebooks/01_GSOM_Acquisition.ipynb", "file"),
        ("Notebooks/02_NASS_Alteration.ipynb", "file"),
        ("Notebooks/03_GSOM_Alteration.ipynb", "file"),
        ("Notebooks/04_GSOM_Cleaning.ipynb", "file"),
        ("Notebooks/05_NASS_Cleaning.ipynb", "file"),
        ("Notebooks/06_Integration_Analysis.ipynb", "file"),
        ("data", "dir"),
        ("data/raw", "dir"),
    ]
    
    missing = []
    for item, item_type in required_items:
        path = Path(item)
        if item_type == "dir":
            exists = path.is_dir()
        else:
            exists = path.is_file()
        
        if not exists:
            missing.append(item)
    
    if missing:
        print_error("Missing files/directories:")
        for item in missing:
            print(f"  - {item}")
        return False
    
    print_success("All required files present")
    return True

def check_prerequisites():
    """Check if all prerequisites are met"""
    print_header("Checking Prerequisites")
    
    checks = [
        check_python_version(),
        check_packages(),
        check_jupyter(),
        check_nbconvert(),
        check_file_structure()
    ]
    
    return all(checks)

def check_manual_steps():
    """Check if manual prerequisite steps are complete"""
    print_header("Checking Manual Prerequisites")
    
    warnings = []
    
    # Check NASS data
    nass_file = Path("data/raw/nass_qs_1902_to_2025.csv")
    if not nass_file.exists():
        warnings.append("NASS data not found")
        print_warning("NASS data must be downloaded manually")
        print("   File: data/raw/nass_qs_1902_to_2025.csv")
        print("   Instructions: documentation/USDA_NASS_Data_Acquisition.md")
        print("   Direct link: https://quickstats.nass.usda.gov/results/18E1C479-6BCF-3726-A3F5-2AAD423752F0")
    else:
        size = nass_file.stat().st_size / (1024 * 1024)  
        print_success(f"NASS data found ({size:.2f} MB)")
    
    # Reminder about NOAA token
    token_notebook = Path("Notebooks/01_GSOM_Acquisition.ipynb")
    if token_notebook.exists():
        print_success("GSOM acquisition notebook found")
        print_warning("Ensure NOAA API token is set in 01_GSOM_Acquisition.ipynb")
    else:
        warnings.append("01_GSOM_Acquisition.ipynb not found")
    
    if warnings:
        print(f"\n{Colors.YELLOW}Found {len(warnings)} warning(s). Continue anyway? (y/N): {Colors.END}", end='')
        response = input().strip().lower()
        return response == 'y'
    
    return True

def create_directories():
    """Create necessary directories"""
    dirs = ['data/raw', 'data/processed', 'data/cleaned', 'logs']
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    print_success("Directories created/verified")

def run_notebook(notebook_path, step_num, description):
    """Execute a Jupyter notebook"""
    print_step(step_num, description)
    print(f"   Executing: {notebook_path}")
    
    start_time = datetime.now()
    
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'nbconvert', '--to', 'notebook', '--execute',
             '--inplace', '--ExecutePreprocessor.timeout=600', notebook_path],
            capture_output=True,
            text=True,
            timeout=900 
        )
        
        elapsed = (datetime.now() - start_time).total_seconds()
        
        if result.returncode == 0:
            print_success(f"Completed in {elapsed:.1f} seconds")
            return True
        else:
            print_error(f"Failed with return code {result.returncode}")
            if result.stderr:
                print(f"{Colors.RED}Error output:{Colors.END}")
                print(result.stderr[:500])
            return False
            
    except subprocess.TimeoutExpired:
        print_error("Notebook execution timed out (>15 minutes)")
        return False
    except FileNotFoundError:
        print_error("nbconvert not found. Install with: pip install nbconvert")
        return False
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        return False

def verify_outputs():
    """Verify that expected output files were created"""
    print_header("Verifying Outputs")
    
    expected_outputs = [
        ("data/raw/USC00118740_GSOM_1902-08-01_to_2025-10-31.csv", "NOAA climate data"),
        ("data/processed/illinois_corn_wide.csv", "Transformed NASS data"),
        ("data/processed/gsom_monthly_selected.csv", "Selected climate variables"),
        ("data/cleaned/gsom_annual_clean.csv", "Cleaned climate data"),
        ("data/cleaned/nass_clean.csv", "Cleaned corn data"),
        ("data/cleaned/integrated_climate_corn.csv", "Final integrated dataset")
    ]
    
    all_present = True
    for filepath, description in expected_outputs:
        path = Path(filepath)
        if path.exists():
            size = path.stat().st_size / 1024 
            print_success(f"{description}: {filepath} ({size:.1f} KB)")
        else:
            print_error(f"{description}: {filepath} - NOT FOUND")
            all_present = False
    
    return all_present

def main():
    """Main execution function"""
    print_header("Climate Impact on Illinois Corn Production (1902-2025)")
    print("Automated Workflow Execution")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create directories
    create_directories()
    
    # Check prerequisites
    if not check_prerequisites():
        print_error("\nPrerequisite check failed. Please fix issues and try again.")
        return 1
    
    # Check manual steps
    if not check_manual_steps():
        print_error("\nManual prerequisites not complete. Aborting.")
        return 1
    
    # Define workflow
    notebooks = [
        ("Notebooks/01_GSOM_Acquisition.ipynb", 1, "Acquiring NOAA GSOM climate data via API"),
        ("Notebooks/02_NASS_Alteration.ipynb", 3, "Transforming NASS data (long → wide format)"),
        ("Notebooks/03_GSOM_Alteration.ipynb", 4, "Selecting relevant GSOM climate variables"),
        ("Notebooks/04_GSOM_Cleaning.ipynb", 5, "Cleaning and annualizing GSOM data"),
        ("Notebooks/05_NASS_Cleaning.ipynb", 6, "Cleaning NASS corn production data"),
        ("Notebooks/06_Integration_Analysis.ipynb", 7, "Integrating datasets and performing analysis"),
    ]
    
    print_header("Executing Notebooks")
    
    # Execute each notebook
    for notebook_path, step_num, description in notebooks:
        if not Path(notebook_path).exists():
            print_error(f"Notebook not found: {notebook_path}")
            return 1
        
        success = run_notebook(notebook_path, step_num, description)
        
        if not success:
            print_error(f"\nWorkflow stopped due to error in {notebook_path}")
            print("Check the error messages above and fix the issue.")
            print("When ready, run this script again - completed notebooks will be skipped if outputs exist.")
            return 1
        
        print() 
    
    # Verify outputs
    if not verify_outputs():
        print_warning("\nSome output files are missing. Check notebook execution above.")
        return 1
    
    # Success summary
    print_header("Workflow Complete!")
    print_success(f"All {len(notebooks)} notebooks executed successfully")
    print_success("All expected output files created")
    print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Analysis pipeline completed successfully!{Colors.END}")
    print(f"{Colors.GREEN}Final dataset: data/cleaned/integrated_climate_corn.csv{Colors.END}")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Workflow interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print_error(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)