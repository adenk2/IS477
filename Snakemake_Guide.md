# Snakemake Workflow Guide

This document explains how to use the Snakemake workflow to automate the entire analysis pipeline.

Snakemake is included in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

Verify installation:
```bash
snakemake --version
```

## Workflow Structure

The `Snakefile` in the project root defines 7 main steps:

1. **acquire_gsom**: Download NOAA climate data via API
2. **check_nass_download**: Check for manually downloaded NASS data
3. **transform_nass**: Transform NASS data (long → wide format)
4. **select_gsom_variables**: Select relevant climate variables
5. **clean_gsom**: Clean and annualize GSOM data
6. **clean_nass**: Clean NASS corn production data
7. **integrate_data**: Integrate datasets and perform analysis

## Running the Workflow

### Complete Workflow

Execute the entire analysis pipeline:

```bash
snakemake --cores 1
```

### Dry Run (Preview)

Preview what will be executed without running anything:

```bash
snakemake --cores 1 --dry-run
```

### Run Specific Steps

Execute only up to a specific rule:

```bash
# Run only up to GSOM cleaning
snakemake --cores 1 clean_gsom

# Run only up to data integration
snakemake --cores 1 integrate_data
```

### Force Re-run

Force re-execution of all steps (ignoring existing outputs):

```bash
snakemake --cores 1 --forceall
```

Force re-run of specific rule and downstream dependencies:

```bash
snakemake --cores 1 --forcerun clean_gsom
```

### Visualize Workflow

Generate a workflow diagram:

```bash
# DAG (Directed Acyclic Graph)
snakemake --dag | dot -Tpng > workflow_dag.png

# Rule graph
snakemake --rulegraph | dot -Tpng > workflow_rules.png
```

Requires graphviz: `pip install graphviz`

## Important Notes

### Manual NASS Data Download

**Step 2 requires manual intervention**. The workflow will pause and provide instructions:

1. Visit: https://quickstats.nass.usda.gov/
2. Follow instructions in `documentation/USDA_NASS_Data_Acquisition.md`
3. Save file to: `data/raw/nass_qs_1902_to_2025.csv`
4. Re-run Snakemake

**Workflow will stop at this step until the file is present.**

### NOAA API Token

Before running, ensure you have:
1. Obtained a NOAA API token: https://www.ncdc.noaa.gov/cdo-web/token
2. Added token to `Notebooks/01_GSOM_Acquisition.ipynb`

## Cleaning Outputs

### Clean Generated Files (Keep Raw Data)

Remove processed and cleaned data to re-run analysis:

```bash
snakemake clean
```

This removes:
- `data/processed/*`
- `data/cleaned/*`
- `logs/*`
- `analysis_complete.flag`

But preserves `data/raw/*` (downloaded data)

### Clean Everything

Remove all data including raw downloads:

```bash
snakemake clean_all
```

**Warning**: This requires re-downloading NOAA data and NASS data

## Workflow Outputs

After successful execution, you'll have:

### Data Files
- `data/raw/USC00118740_GSOM_1902-08-01_to_2025-10-31.csv` - Raw NOAA data
- `data/raw/nass_qs_1902_to_2025.csv` - Raw NASS data (manual)
- `data/processed/gsom_monthly_selected.csv` - Selected climate variables
- `data/processed/illinois_corn_analysis_ready.csv` - Transformed NASS data
- `data/cleaned/gsom_annual_clean.csv` - Cleaned annual climate data
- `data/cleaned/nass_clean.csv` - Cleaned corn production data
- `data/cleaned/integrated_climate_corn.csv` - **Final integrated dataset**

### Log Files
- `logs/01_gsom_acquisition.log`
- `logs/02_nass_alteration.log`
- `logs/03_gsom_alteration.log`
- `logs/04_gsom_cleaning.log`
- `logs/05_nass_cleaning.log`
- `logs/06_integration_analysis.log`

### Visualizations
Generated within `06_Integration_Analysis.ipynb`:
- Correlation matrix heatmap
- Time series plots
- Scatter plots

## Troubleshooting

### Issue: "No rule to make target"

**Cause**: Missing input files

**Solution**: Ensure NASS data is manually downloaded to `data/raw/nass_qs_1902_to_2025.csv`

### Issue: Notebook execution fails

**Cause**: Missing dependencies or incorrect notebook paths

**Solution**:
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Check notebook names match Snakefile
ls Notebooks/
```

### Issue: NOAA API rate limit

**Cause**: Too many API requests

**Solution**: Wait 1 hour and re-run. Snakemake will skip completed steps.

### Issue: Permission denied

**Cause**: Cannot create directories

**Solution**:
```bash
# Ensure directories exist and are writable
mkdir -p data/{raw,processed,cleaned} logs
chmod -R u+w data/ logs/
```

## Advanced Usage

### Run with More Cores

Some steps can benefit from parallel execution:

```bash
snakemake --cores 4
```

### Generate Report

Create an HTML report of the workflow:

```bash
snakemake --report report.html
```

### Use Different Notebook Directory

Edit the `Snakefile` and change:
```python
NOTEBOOKS_DIR = "Notebooks"  # Change to your directory
```

## Comparison: Snakemake vs Manual Execution

| Aspect | Manual | Snakemake |
|--------|--------|-----------|
| **Execution** | Run each notebook individually | One command |
| **Dependencies** | Manual tracking | Automatic |
| **Re-runs** | Re-run everything | Only changed steps |
| **Reproducibility** | Requires documentation | Self-documenting |
| **Error handling** | Manual restart | Resume from failure |
| **Time** | 15+ minutes | ~15 minutes (first run), <5 min (updates) |

## Getting Help

- Snakemake documentation: https://snakemake.readthedocs.io/
- View workflow rules: `snakemake --list`
- Check specific rule: `snakemake --list-rules`
- Verbose output: `snakemake --cores 1 --verbose`

## Best Practices

1. **Always run dry-run first**: `snakemake -n`
2. **Check logs** if a step fails: `logs/*.log`
3. **Use version control**: Commit Snakefile changes
4. **Document modifications**: Update this file if you modify the workflow
5. **Test incrementally**: Run to specific rules during development