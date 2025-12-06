"""
Snakemake workflow for Climate Impact on Illinois Corn Production Analysis
Automates the complete data acquisition, cleaning, integration, and analysis pipeline

Usage:
    snakemake --cores 1                    # Run entire workflow
    snakemake --cores 1 --dry-run          # Preview workflow
    snakemake --cores 1 integrate_data     # Run up to specific rule
"""

import os

# Configuration
NOTEBOOKS_DIR = "Notebooks"
DATA_RAW = "data/raw"
DATA_PROCESSED = "data/processed"
DATA_CLEANED = "data/cleaned"

# Create directories if they don't exist
os.makedirs(DATA_RAW, exist_ok=True)
os.makedirs(DATA_PROCESSED, exist_ok=True)
os.makedirs(DATA_CLEANED, exist_ok=True)

# Rule: all - defines final outputs
rule all:
    input:
        f"{DATA_CLEANED}/integrated_climate_corn.csv",
        "analysis_complete.flag"
    message:
        "✅ Complete workflow executed successfully!"

# Rule 1: Acquire NOAA GSOM climate data via API
rule acquire_gsom:
    output:
        raw_gsom = f"{DATA_RAW}/USC00118740_GSOM_1902-08-01_to_2025-10-31.csv"
    log:
        "logs/01_gsom_acquisition.log"
    message:
        "Step 1: Acquiring NOAA GSOM climate data via API..."
    notebook:
        f"{NOTEBOOKS_DIR}/01_GSOM_Acquisition.ipynb"

# Rule 2: Manual NASS data download check
rule check_nass_download:
    output:
        nass_raw = f"{DATA_RAW}/nass_qs_1902_to_2025.csv"
    message:
        "⚠️  Step 2: MANUAL DOWNLOAD REQUIRED\n"
        "Please download USDA NASS data manually:\n"
        "1. Visit: https://quickstats.nass.usda.gov/\n"
        "2. Apply filters as described in documentation/USDA_NASS_Data_Acquisition.md\n"
        "3. Save to: {output.nass_raw}\n"
        "4. Re-run snakemake after download"
    run:
        if not os.path.exists(output.nass_raw):
            raise FileNotFoundError(
                f"\n{'='*70}\n"
                f"MANUAL STEP REQUIRED:\n"
                f"Please download NASS data manually to: {output.nass_raw}\n"
                f"See documentation/USDA_NASS_Data_Acquisition.md for instructions\n"
                f"Direct link: https://quickstats.nass.usda.gov/results/18E1C479-6BCF-3726-A3F5-2AAD423752F0\n"
                f"{'='*70}\n"
            )

# Rule 3: Transform NASS data from long to wide format
rule transform_nass:
    input:
        nass_raw = f"{DATA_RAW}/nass_qs_1902_to_2025.csv"
    output:
        nass_wide = f"{DATA_PROCESSED}/illinois_corn_wide.csv"
    log:
        "logs/02_nass_alteration.log"
    message:
        "Step 3: Transforming NASS data (long → wide format)..."
    notebook:
        f"{NOTEBOOKS_DIR}/02_NASS_Alteration.ipynb"

# Rule 4: Select relevant GSOM climate variables
rule select_gsom_variables:
    input:
        raw_gsom = f"{DATA_RAW}/USC00118740_GSOM_1902-08-01_to_2025-10-31.csv"
    output:
        gsom_selected = f"{DATA_PROCESSED}/gsom_monthly_selected.csv"
    log:
        "logs/03_gsom_alteration.log"
    message:
        "Step 4: Selecting relevant GSOM climate variables..."
    notebook:
        f"{NOTEBOOKS_DIR}/03_GSOM_Alteration.ipynb"

# Rule 5: Clean and annualize GSOM data
rule clean_gsom:
    input:
        gsom_selected = f"{DATA_PROCESSED}/gsom_monthly_selected.csv"
    output:
        gsom_clean = f"{DATA_CLEANED}/gsom_annual_clean.csv"
    log:
        "logs/04_gsom_cleaning.log"
    message:
        "Step 5: Cleaning and annualizing GSOM data (unit conversion, aggregation)..."
    notebook:
        f"{NOTEBOOKS_DIR}/04_GSOM_Cleaning.ipynb"

# Rule 6: Clean NASS corn production data
rule clean_nass:
    input:
        nass_wide = f"{DATA_PROCESSED}/illinois_corn_wide.csv"
    output:
        nass_clean = f"{DATA_CLEANED}/nass_clean.csv"
    log:
        "logs/05_nass_cleaning.log"
    message:
        "Step 6: Cleaning NASS corn production data (validation, quality checks)..."
    notebook:
        f"{NOTEBOOKS_DIR}/05_NASS_Cleaning.ipynb"

# Rule 7: Integrate datasets and perform analysis
rule integrate_data:
    input:
        gsom_clean = f"{DATA_CLEANED}/gsom_annual_clean.csv",
        nass_clean = f"{DATA_CLEANED}/nass_clean.csv"
    output:
        integrated = f"{DATA_CLEANED}/integrated_climate_corn.csv"
    log:
        "logs/06_integration_analysis.log"
    message:
        "Step 7: Integrating datasets and performing statistical analysis..."
    notebook:
        f"{NOTEBOOKS_DIR}/06_Integration_Analysis.ipynb"

# Rule: Mark analysis as complete
rule analysis_complete:
    input:
        f"{DATA_CLEANED}/integrated_climate_corn.csv"
    output:
        "analysis_complete.flag"
    shell:
        """
        echo "Analysis completed on $(date)" > {output}
        echo "✅ All notebooks executed successfully!"
        echo "📊 Final output: {input}"
        """

# Rule: Clean all generated files (for re-running workflow)
rule clean:
    shell:
        """
        rm -rf {DATA_PROCESSED}/* {DATA_CLEANED}/* logs/* analysis_complete.flag
        echo "🧹 Cleaned all generated files (raw data preserved)"
        """

# Rule: Clean everything including raw data
rule clean_all:
    shell:
        """
        rm -rf {DATA_RAW}/* {DATA_PROCESSED}/* {DATA_CLEANED}/* logs/* analysis_complete.flag
        echo "🧹 Cleaned all data and outputs"
        """