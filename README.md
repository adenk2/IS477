# Climate Impact on Illinois Corn Production (1902-2025)
Repository dedicated to the IS 477 group project. 

* **Title:** Climate Impact on Illinois Corn Production (1902-2025)
* **Contributors:** 
    * Aden Krueger (adenk2)
    * Brady Brooks (bradymb2)

## Summary 
This project examines the relationship between climate variability and corn production in Illinois over 124 years (1902 to 2025), with the simple goal of integrating historical weather data with agricultural statistics to understand how growing-season climate affects crop yields. The motivation stems from the critical importance of understanding climate-agriculture relationships within Illinois, as Illinois is one of the top corn-producing states in the United States. 

Our primary research question is: How do growing-season climate variables correlate with corn production metrics in Illinois over 124 years? We hypothesized that climate-yield relationships would change over time as climate variability increases, with earlier periods showing a lessened climate sensitivity and modern eras potentially indicating climate-driven effects on yield metrics. 

To address this question, we integrated two major datasets: NOAA’s Global Summary of the Month (GSOM) climate data for Champaign County, Illinois, and USDA’s National Agricultural Statistics Service (NASS) corn production records. The climate data provided monthly observations of temperature, precipitation, and extreme weather events, which we aggregated to the corn growing season (April-September). The NASS corn data included key metrics such as yield per acre, planted acreage, harvest acreage, and total production.

Our analysis revealed several findings. First, corn yields in Illinois have unsurprisingly increased dramatically from an average of 22 bushels per acre in the early 1900s to over 200 bushels per acre in recent years, an increase, on average, of +1.47 bushels per acre per year. Second, we identified statistically significant correlations between climate variables and yield, with precipitation showing the strongest positive correlation (r=0.251, p=0.005) and heat stress days showing a negative correlation (r=-0.186, p=0.038). Additionally, temperature trends indicate a warming of approximately 0.13°F per decade during the growing season, while precipitation has increased by about 9.47mm per decade.

The integration of 124 years of data allowed for a perfect temporal alignment between our climate and agricultural datasets, with no missing values in critical variables after cleaning. This comprehensive dataset enabled robust statistical analysis methodologies, including correlation analysis, MLR (multiple linear regression), SLR (simple linear regression), and trend analysis. Our findings contribute to understanding how agricultural systems respond to climate variability over extended time periods, providing insights relevant to climate change and agricultural development in the Midwest. 

Although our methodologies are consistent and accurate given the data, there are areas for future improvement. Most notably, future work should account for the technological changes that occurred over the 124 years. Corn production has been fundamentally transformed over this time frame, from hybrid seed development to mechanization, and climate-yield relationships are not stationary across time. As a result, pooling all years into a single MLR framework may obscure meaningful decade-level differences and introduce substantial confounding. For example, early-century yields may have been more constrained by technological limits rather than climate, whereas modern yields may reflect the production capacity of hybrid seeds with certain climate resistances. A further discussion of what can be done to address this confounding will be addressed in the section “Future Work.”

## Data Profile

## Data Quality

## Findings
Our analysis of 124 years of integrated climate-corn data from 1902 to 2025 revealed several key findings that shed insight into the complex relationship between growing season climate patterns and the agricultural productivity in Champaign County, Illinois. 

The most striking finding is the dramatic increase in corn yields over time, with a linear trend of ~+14.75 bushels per acre per decade (Figure 2, bottom panel, “INTEGRATION_ANALYSIS.ipynb”). We identified early 1900s yields averaged ~30-40 bushels per acre, while modern yields regularly exceed 200 bushels per acre. This nearly 10-fold increase can be primarily attributed to technological advancements rather than climate improvement. Simultaneously, growing season average temperatures have increased by +0.13°F per decade, and total precipitation has increased by 9.47mm per decade. This indicates a gradual warming and wetting trend has been present during the period of analysis. 

Our correlation analysis identified statistically significant relationships between multiple climate variables and corn yield. Total growing season precipitation showed the strongest positive correlation (r = 0.251, p = 0.005), indicating that wetter growing seasons generally support higher yields. Minimum temperature also showed a positive correlation (r = 0.223, p = 0.013), while heat stress days (≥90°F) demonstrated a significant negative correlation (r = -0.186, p = 0.038), confirming that extreme heat events damage crop productivity. Interestingly, average temperature showed only a weak positive correlation (r = 0.193, p = 0.031), suggesting that within the observed range, moderate temperature increases may be beneficial, but extreme heat becomes detrimental.

The scatter plots seen in (Figure 3, “INTEGRATION_ANALYSIS.ipynb”) reveal the nature of these relationships visually. The precipitation-yield relationship found in panel 2 (top right) shows a mild scatter, indicating that precipitation only explains ~6% of yield variability when considered alone. This low R² value reflects the outside influence of certain aspects, like technological improvement, expansion of farming, and improvement of practices. The heat stress days plot found in panel 4 (bottom right) shows a negative trend, with years experiencing more days above 90°F tending to have lower yields relative to the baseline for that era. 
Our correlation analysis also included significance testing, which showed that precipitation (p = 0.005) and minimum temperature (p = 0.013) are highly significant predictors of yield, while maximum temperature alone was not statistically significant (p = 0.091). The multiple linear regression (MLR) model, which incorporates several climate variables simultaneously, demonstrated stronger explanatory power than the individual univariate relationships. This suggests that corn yield is influenced by a combination of climate factors working together, rather than by any single variable on its own.

These findings collectively demonstrate that while climate variability exerts a significant influence on year-to-year corn productivity, climate alone has not been the primary driver of yield increase over the past 120+ years. The persistent increase in yield may instead reflect a combination of technological improvements and the advancement of agricultural techniques within the Midwest. Regardless, the consistent occurrence of climate-yield correlations despite technological improvements suggests that further climate changes, particularly increases in extreme heat events, could pose challenges for increasing agricultural productivity in Illinois.

## Future Work
One of the most significant lessons involved handling temporal data with different characteristics. The NOAA GSOM data came in Celsius and millimeters, while the USDA NASS data used metrics (bushels, acres), which we were unfamiliar with. We learned the importance of maintaining documentation of all transformation steps within our notebooks and leaving debugging comments for future reference. Additionally, we discovered that the NASS data structure (long format with multiple domain categories) required sophisticated filtering to avoid double-counting. Specifically, the “ACRES PLANTED” variable initially appeared to be missing, but rather was present under a different domain specification. Neither of us had ever seen long-formatted data, and thus found the alteration notebook, NASS_Alteration.ipynb, to be one of the most difficult cleaning steps to produce. 

Our analysis used point weather data from a single station in Champaign County to represent climate conditions across the entire state of Illinois. This mismatch between county-level climate data and state-level agricultural data represents a significant limitation we encountered. Notably, we found it extremely difficult to aggregate and combine NOAA GSOM data from the entirety of Illinois into one dataset to be integrated with our corn production data. Future research should incorporate multiple weather stations across Illinois, potentially using spatial methods to create more representative statewide growing season climate metrics. Additionally, we’ve wondered whether splitting the state of Illinois into different regions (North vs. South, East vs. West) could reveal regional differences in yield masked by our state-level aggregation. 

While our regression models and correlation methods provided interpretable results and attempted to avoid overfitting, several more advanced methodologies may yield additional insights. For example, time-varying coefficient models could capture smooth changes in climate-yield relationships. Additionally, non-linear models may capture threshold effects, such as the negative impact of temperatures above 90°F on corn yields during critical reproductive periods. Machine learning approaches, such as k-nearest neighbors or random forest regressions, could identify complex interactions between climate variables that linear models miss. We did not attempt to use these models in our current analysis, as we identified significant overfitting due to the lack of sample size. 

Several potentially important variables were not available to us in our analysis. Soil quality data, if available historically, may help explain some of the residual yield variability. Economic variables such as corn prices, input costs, and governmental farm subsidies may influence planting decisions, indirectly affecting yields. Pest and disease outbreak records could additionally provide context for years with unexpectedly low yields. 
Extending this analysis to other neighboring corn-producing states (Iowa, Indiana, Minnesota, etc.) would allow for spatial comparison of climate-yield relationships and potentially identify geographic differences in climate sensitivity.
Future work should more explicitly address technological advancements to findings in yield. If technology has successfully buffered climate impacts, understanding which specific technologies are most effective could inform agricultural policy and habits.

While we have made our analysis reproducible through comprehensive documentation in each notebook, future work could further enhance reproducibility by containerizing the analysis environment through Docker or publishing repositories with persistent identifiers like Zenodo. Additionally, creating an interactive web-based dashboard could make the findings more accessible to non-technical audiences such as farmers and policymakers. 

These future directions would build on the strong foundation established by this project while addressing current limitations and extending our lens into climate-agriculture relationships in the Midwest corn belt. 

## Prerequisites 

### Software Requirements
* Python 3.8 or higher
* Jupyter Notebook
* Require Python packages (see requirements.txt)

Install dependencies
```bash
pip install -r requirements.txt
```

## Reproducing

### Step 1: Acquire NOAA Weather Data

**Notebook**: 01_GSOM_Acquisition.ipynb
What it does:
* Downloads NOAA GSOM weather data via API
* Saves raw monthly climate data 

Requirements:
* NOAA API token (free): [https://www.ncdc.noaa.gov/cdo-web/token]
* Replace NOAA_TOKEN in notebook with your token.

**Ouput:** 
* `data/raw/USC00118740_GSOM_1902-08-01_to_2025-10-31.csv`

### STEP 2: Download USDA NASS Corn Data

**MANUAL DOWNLOAD REQUIRED - No notebook for this step**

**Instructions:** See `documentation/USDA_NASS_Data_Acquisition.txt`

Quick steps:

1. Go to: https://quickstats.nass.usda.gov/
2. Apply filters:
   * Sector: CROPS
   * Group: FIELD CROPS
   * Commodity: CORN
   * Category: Select all: AREA PLANTED, AREA HARVESTED, PRODUCTION, YIELD
   * Geographic Level: STATE
   * State: ILLINOIS
   * Year: 1902 to 2025
3. Click "Get Data"
4. Click "Download" to CSV format
5. Save as: `data/raw/nass_qs_1902_to_2025.csv`

**Verify:** File should be ~4,600 rows

**Direct link:** [https://quickstats.nass.usda.gov/results/18E1C479-6BCF-3726-A3F5-2AAD423752F0]

**Time:** ~5 minutes

### STEP 3: Transform NASS Data (Long to Wide)

**Notebook:** `02_NASS_Alteration.ipynb`

What it does:
* Transforms USDA data from long format to wide format
* Filters to state-level Illinois corn statistics
* Creates one row per year with metrics as columns

**Input:**
* `data/raw/nass_qs_1902_to_2025.csv`

**Output:**
* `data/processed/illinois_corn_analysis_ready.csv`
* Format: ~124 rows (one per year), 5 columns

Columns created:
* `year`
* `acres_planted`
* `acres_harvested`
* `yield_bu_per_acre`
* `production_bushels`

**Time:** ~1 minute

### STEP 4: Select GSOM Variables

**Notebook:** `03_GSOM_Alteration.ipynb`

What it does:
* Selects relevant climate variables from raw NOAA data
* Focuses on agricultural metrics (temp, precip, extreme events)
* Adds growing season flag (April-September)

**Input:**
* `data/raw/USC00118740_GSOM_*.csv`

**Output:**
* `data/processed/gsom_monthly_selected.csv`
* Format: ~1,479 monthly records, 25 variables
* Units: Still in Celsius and millimeters (will convert in next step)

Key variables:
* Temperature (avg, max, min, extremes)
* Precipitation (total, max daily, day counts)
* Degree days (heating, cooling)
* Extreme weather day counts

**Time:** ~1 minute

### STEP 5: Clean & Annualize GSOM Data

**Notebook:** `04_GSOM_Cleaning.ipynb`

What it does:
* Converts units: Celsius → Fahrenheit, millimeters → inches
* Filters to growing season (April-September)
* Aggregates monthly data to annual summaries
* Creates derived variables (GDD, precipitation adequacy)
* Adds data quality flags

**Input:**
* `data/processed/gsom_monthly_selected.csv`

**Output:**
* `data/processed/gsom_annual_clean.csv`
* Format: ~123 annual records, climate variables in proper units

Key transformations:
* Monthly to Annual (one row per year)
* Celsius to Fahrenheit
* Creates Growing Degree Days (GDD) and other derived variables

**Time:** ~1-2 minutes

### STEP 6: Clean NASS Data

**Notebook:** `05_NASS_Cleaning.ipynb`

What it does:
* Data quality checks on corn production data
* Validates ranges (no negative values, realistic yields)
* Handles any missing years
* Creates derived metrics (harvest efficiency)

**Input:**
* `data/processed/illinois_corn_analysis_ready.csv`

**Output:**
* `data/processed/nass_cleaned.csv`
* Format: ~124 annual records, validated and clean

Quality checks:
* Yield ranges (0-300 bu/acre)
* Acreage consistency
* Production calculation verification

**Time:** ~1 minute

### STEP 7: Integrate Datasets and Analyze

**Notebook:** `06_Integration_Analysis.ipynb`

What it does:
* Merges cleaned climate and corn production data via inner join on year
* Performs data quality checks and removes any incomplete records
* Generates comprehensive statistical analysis (correlations, regressions)
* Creates visualizations showing climate-agriculture relationships
* Identifies extreme weather and yield years

**Input:**
* `data/cleaned/gsom_annual_clean.csv`
* `data/cleaned/nass_clean.csv`

**Output:**
* `data/cleaned/integrated_climate_corn.csv`
* Format: ~124 annual records, 19 columns
* Multiple visualizations (correlation heatmap, time series, scatter plots)

Analysis performed:
* Pearson correlations between climate variables and corn yield
* Simple linear regression models for individual predictors
* Multiple linear regression model using key climate variables
* Temporal trend analysis (linear trends per decade)
* Extreme year identification (bottom/top 10% yields)

**Time:** ~2-3 minutes

## References

## Licenses

### Code License
All code and scripts in this repository are licensed under the MIT License. See `LICENSE` file for details.

## Data Availability 

### Box Repository 
All raw, processed, and cleaned datasets are available via Box:
* **Box Link:** [https://uofi.box.com/s/7m4ei68uzhfnoe2v5r4hby1cwu8ld2tj]
* **Contents:**
    * gsom_annual_clean.csv
    * integrated_climate_corn.csv
    * nass_clean.csv
    * gsom_monthly_selected.csv
    * illinois_corn_wide.csv
    * USC00118740_GSOM_1902-08-01_to_2025-10-31.csv
    * nass_qs_1902_to_2025.csv

## Data Licenses

### Source Data

### NOAA GSOM Climate Data
* **License:** U.S. Government Work - Public Domain
* **Source:** National Oceanic and Atmospheric Administration
* **Terms:** No copyright restrictions. Free to use, modify, and redistribute.
* **Attribution:** Not required but recommended

### USDA NASS Agricultural Statistics
* **License:** U.S. Government Work - Public Domain
* **Source:** United States Department of Agriculture
* **Terms:** No copyright restrictions. Free to use, modify, and redistribute.
* **Attribution:** Cite as "USDA National Agricultural Statistics Service"

### Derived/Integrated Data

### Integrated Climate-Corn Dataset
* **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
* **Rights:** You are free to:
  * Share — copy and redistribute the material
  * Adapt — remix, transform, and build upon the material
* **Conditions:**
  * Attribution — You must give appropriate credit to the creators
  * Cite original NOAA and USDA sources
* **License Text:** https://creativecommons.org/licenses/by/4.0/

## Code/Software

All Python scripts, Jupyter notebooks, and analysis code in this repository:
* **License:** MIT License (see LICENSE.txt)

## Troubleshooting 

### NOAA API Issues
* **Rate limit exceeded:** Wait 1 hour before retrying
* **Invalid token:** Verify token in notebook matches email
* **Network timeout:** Check internet connection, retry

### NASS Data Issues
* **File not found:** Verify filename exactly matches `nass_qs_1902_to_2025.csv`
* **Wrong format:** Ensure CSV download (not Excel)
* **Wrong filters:** Re-download using direct link in documentation

### Notebook Execution Errors
* **Module not found:** Run `pip install -r requirements.txt`
* **Kernel crash:** Restart kernel and re-run from beginning
* **Path errors:** Ensure running from project root directory


## Repository Artifact Structure 
```
├── Contributions/
│   ├── AdenKrueger.md
│   └── BradyBrooks.md
│
├── Notebooks/
│   ├── GSOM_Acquisition.ipynb
│   ├── GSOM_Alteration.ipynb
│   ├── GSOM_Cleaning_Notebook.ipynb
|   ├── INTEGRATION_ANALYSIS.ipynb
│   ├── NASS_Alteration.ipynb
│   └── NASS_Cleaning.ipynb
│
├── data/
│   ├── cleaned/
│   │   ├── gsom_annual_clean.csv
│   │   ├── integrated_climate_corn.csv
│   │   └── nass_clean.csv
│   ├── processed/
│   │   ├── gsom_monthly_selected.csv
│   │   └── illinois_corn_wide.csv
│   │
│   └── raw/
│       ├── USC00118740_GSOM_1902-08-01_to_2025-10-31.csv
│       └── nass_qs_1902_to_2025.csv
│
├── documentation/
│   ├── USDA_NASS_Data_Acquisition.md
│   └── gsom_data_acquisition.txt
│  
├── LICENSE.txt
├── ProjectPlan.md
├── README.md
├── requirements.txt
└── StatusReport.md
```
