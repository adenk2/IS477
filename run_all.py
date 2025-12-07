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
import os
from pathlib import Path
from datetime import datetime

# ANSI color codes for pretty output
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
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")

def print_warning(message):
    """Print a warning message"""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.END}")

def print_error(message):
    """Print an error message"""
    print(f"{Colors.RED}✗ {message}{Colors.END}")

def check_prerequisites():
    """Check if required files and setup exist"""
    print_header("Checking Prerequisites")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print_error(f"Python 3.8+ required. You have {sys.version_info.major}.{sys.version_info.minor}")
        return False
    print_success(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check required packages
    try:
        import pandas
        import numpy
        import matplotlib
        import seaborn
        import scipy
        import sklearn
        import requests
        print_success("All required packages installed")
    except ImportError as e:
        print_error(f"Missing package: {e.name}")
        print_error("Run: pip install -r requirements.txt")
        return False
    
    # Check Jupyter is installed
    try:
        result = subprocess.run(['jupyter', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print_success("Jupyter installed")
        else:
            print_error("Jupyter not found. Install with: pip install jupyter")
            return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print_error("Jupyter not found. Install with: pip install jupyter")
        return False
    
    # Check if notebooks directory exists
    if not Path("Notebooks").exists():
        print_error("Notebooks directory not found. Are you in the project root?")
        return False
    print_success("Notebooks directory found")
    
    return True

def check_manual_steps():
    """Check if manual prerequisite steps are complete"""
    print_header("Checking Manual Prerequisites")
    
    warnings = []
    
    # Check NASS data
    nass_file = Path("data/raw/nass_qs_1902_to_2025.csv")
    if not nass_file.exists():
        warnings.append("NASS data not found at: data/raw/nass_qs_1902_to_2025.csv")
        print_warning("NASS data must be downloaded manually")
        print("   Instructions: documentation/USDA_NASS_Data_Acquisition.md")
        print("   Direct link: https://quickstats.nass.usda.gov/results/18E1C479-6BCF-3726-A3F5-2AAD423752F0")
    else:
        print_success("NASS data found")
    
    # Check NOAA token (basic check - just look for the notebook)
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

def run_notebook(notebook_path, step_num, description):
    """Execute a Jupyter notebook"""
    print_step(step_num, description)
    print(f"   Executing: {notebook_path}")
    
    start_time = datetime.now()
    
    try:
        # Use jupyter nbconvert to execute notebook
        result = subprocess.run(
            ['jupyter', 'nbconvert', '--to', 'notebook', '--execute',
             '--inplace', '--ExecutePreprocessor.timeout=600', notebook_path],
            capture_output=True,
            text=True,
            timeout=900  # 15 minute timeout
        )
        
        elapsed = (datetime.now() - start_time).total_seconds()
        
        if result.returncode == 0:
            print_success(f"Completed in {elapsed:.1f} seconds")
            return True
        else:
            print_error(f"Failed with return code {result.returncode}")
            print(f"{Colors.RED}Error output:{Colors.END}")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print_error("Notebook execution timed out (>15 minutes)")
        return False
    except FileNotFoundError:
        print_error("jupyter command not found. Is Jupyter installed?")
        return False
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    dirs = ['data/raw', 'data/processed', 'data/cleaned', 'logs']
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    print_success("Directories created/verified")

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
        # Step 2 is manual NASS download - already checked
        ("Notebooks/02_NASS_Alteration.ipynb", 3, "Transforming NASS data (long → wide format)"),
        ("Notebooks/03_GSOM_Alteration.ipynb", 4, "Selecting relevant GSOM climate variables"),
        ("Notebooks/04_GSOM_Cleaning.ipynb", 5, "Cleaning and annualizing GSOM data"),
        ("Notebooks/05_NASS_Cleaning.ipynb", 6, "Cleaning NASS corn production data"),
        ("Notebooks/06_Integration_Analysis.ipynb", 7, "Integrating datasets and performing analysis"),
    ]
    
    print_header("Executing Notebooks")
    
    failed_notebooks = []
    
    # Execute each notebook
    for notebook_path, step_num, description in notebooks:
        if not Path(notebook_path).exists():
            print_error(f"Notebook not found: {notebook_path}")
            failed_notebooks.append((notebook_path, "File not found"))
            continue
        
        success = run_notebook(notebook_path, step_num, description)
        
        if not success:
            failed_notebooks.append((notebook_path, "Execution failed"))
            print_error(f"\nWorkflow stopped due to error in {notebook_path}")
            print("Fix the issue and run again. Completed notebooks will be skipped.")
            return 1
        
        print()  # Blank line between steps
    
    # Summary
    print_header("Workflow Complete!")
    print_success(f"All {len(notebooks)} notebooks executed successfully")
    print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check outputs
    print_header("Verifying Outputs")
    expected_outputs = [
        "data/cleaned/integrated_climate_corn.csv",
        "data/cleaned/gsom_annual_clean.csv",
        "data/cleaned/nass_clean.csv"
    ]
    
    all_present = True
    for output in expected_outputs:
        if Path(output).exists():
            size = Path(output).stat().st_size / 1024  # KB
            print_success(f"{output} ({size:.1f} KB)")
        else:
            print_error(f"{output} - NOT FOUND")
            all_present = False
    
    if all_present:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Analysis pipeline completed successfully!{Colors.END}")
        print(f"{Colors.GREEN}Final dataset: data/cleaned/integrated_climate_corn.csv{Colors.END}")
        return 0
    else:
        print_error("\nSome output files are missing. Check notebook execution logs.")
        return 1

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