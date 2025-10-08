Overview: This project investigates the impact of climate factors on corn harvests in Illinois over time. By integrating NOAA Global Summary of the Month weather data with USDA NASS corn commodity data, we aim to analyze how climate variables influence corn yield, planted area, and other related variables year over year. 

Research Question(s): How do climate factors impact the yearly corn harvests for the state of Illinois? Can we identify climate patterns that predict high or low corn yields? 

Team: Brady Brooks and Aden Krueger 

Both team members found a data source and a dataset and will adhere to all ethical guidelines. They will also devise a plan for the precise steps that will be taken to utilize the datasets to solve our research question, such as implementing a workflow and documentation.
Brady will focus on a lot of the Python portion of the project, such as the extraction and enrichment, data integration, and data cleaning.
Aden will focus on the data quality checks, ensuring reproducibility, and upload any reproducibility steps and data documentation to GitHub.

Datasets: 
1)https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-month?pageNum=1&pageSize=10&bbox=40.240,-88.368,39.992,-88.120
The first dataset is NOAA’s weather and climate data for Champaign, Illinois, spanning from 1902 to the present.  Each observation contains features about the weather for each month and year. The dataset includes features such as the mean, lowest, and highest temperatures in Fahrenheit for each month, as well as precipitation.

2) https://quickstats.nass.usda.gov
The second dataset we will use for this project is the USDA National Agricultural Statistics Service's corn commodity records. This dataset provides detailed annual information on corn production, yield, acreage, and related economic data across the continental United States. For this analysis, we will focus on state-level data for Illinois, allowing us to examine how long-term climate trends correspond with agricultural outcomes within the state. Key variables we may look at include: Yield (bushels per acre), Area Harvested (acres), and Area Planted (acres). 

Timeline: Document the plan and timeline for implementing your project, including who will complete each task.
Weeks 1–2:
Acquire NOAA GSOM and USDA NASS datasets (via API and download)
Store raw data in tabular CSV format and document characteristics.
Brady: NOAA data acquisition & documentation.
Aden: USDA data acquisition & documentation.
Both: Collaborate on profiling and look into including an ethical data statement if necessary
Weeks 3–4:
Organize and clean datasets (naming, formats, missing values).
Assess and document data quality.
Brady: Write Python cleaning scripts (Pandas).
Aden: Conduct data quality checks and document results.
Weeks 5–6:
Integrate datasets (merge by year) and derive features (growing-season averages).
Begin exploratory analysis and create initial visualizations.
Brady: Integration, feature engineering, and analysis in Python.
Aden: Verify integration accuracy, manage GitHub documentation.
Weeks 7–8:
Automate workflow and/or outline workflow processes.
Finalize report (README.md), metadata, and reproducibility documentation.
Tag and release the final GitHub version.
Brady: Automation and script testing
Aden: Automation and script testing, Documentation, metadata, and reproducibility validation.

Data lifecycle (cf. Module 1): Relate your project to one or more of the lifecycle models discussed in class. 
Formulate Research Question: Defining a clear research question with attainable goals and objectives while ensuring the data to answer said question exists or can be attained. 
Collect Data / Acquisition: Pull NOAA climate and USDA corn data via their respective methods
Storage and Organization: Save raw data as a CSV in a structured GitHub repository
Cleaning and Quality Assessment: Handle missing values, inconsistent formats, and outliers within our dataset
Integration and Analysis: Merge datasets by year, ensuring year identifiers are in the same format (Lifecycle step 3). We can then generate derived features such as seasonal averages
Visualization and Modeling: Explore correlations and build predictive models in Python
Archival and Reuse: Document workflow, provide metadata tags, and release the GitHub repository for reproducibility 

Ethical data handling (cf. Module 2): Identification of all ethical, legal, or policy constraints and how they were addressed. This includes issues related to consent, privacy/confidentiality, copyright, licenses and terms of use.
Both datasets, NCEI and NASS of the USDA, are public domain, so no individual consent is required. Regarding API usage, we will respect the terms of use for APIs (limiting requests to 5 per second) as well as adhere to document attribution for NCEI and USDA. Data storage will happen in the GitHub repository, with personal identifiable information not included, and is non applicable to our dataset. 

Data collection and acquisition (cf. Module 3): Collection or acquisition of at least 2 different datasets from distinct trustworthy sources. Selected datasets should either have different access methods (e.g., APIs) or formats/schemas.
NOAA GSOM: API request for Champaign, IL, retrieved as CSV/JSON
USDA NASS: Download of CSV for Illinois corn data. 
Each dataset uses a distinct access method, i.e., API request and download. 

Storage and organization (cf. Modules 4-5): Select and describe a specific storage and organization strategy. This may include use of tabular, relational, or semi-structured models via filesystems or databases as well as filesystem structures and naming conventions.
We plan on storing the data as tabular CSV files in the GitHub repository, ensuring the filenames and directories follow clear naming conventions for reproducibility. 

Extraction and enrichment (cf. Module 6): 
We plan on calculating derived variables such as growing-season mean temperature, total precipitation, and temperature/precipitation outliers. We believe these manufactured variables will enrich our dataset and provide new insights. 

Data integration (cf. Module 7-8): Integration of datasets (Python/Pandas or SQL)
We plan on merging our NOAA and USDA data by year, utilizing Pandas. By left-joining our USDA dataset with the NOAA annual summaries, we can validate matching years and handle missing entries. We will also look into schema documentation creation to describe the integrated dataset variables. 

Data quality (cf. Module 9): Document data quality assessment results.
We plan on identifying missing values in climate and crop data as well as assessing outliers, e.g., extreme yields or precipitation values. We will also document coverage gaps, looking for any general inconsistencies in weather station data or reporting. 

Data cleaning (cf. Module 10): Describe any data cleaning methods applied (e.g., missing values, outliers, syntactic or semantic cleaning)
We plan to convert any string numeric values into numeric types, as well as handling missing or flagged values as NaN. After doing preliminary analysis, we intend to normalize temperature units and precipitation measures if necessary. Additionally, ensuring consistent year identifiers are available for integration will be crucial to our left-join process. 

Workflow automation and provenance (cf. Module 11-12): Provide an automated end-to-end workflow. 
We can design and implement an end-to-end Python workflow:
Pull data from APIs
Perform cleaning, aggregation, and merging
Conduct analysis and generate visualizations based on findings
Document and interpret visualizations 

Reproducibility and transparency (cf. Module 13):  Your project must provide sufficient information to allow someone else to reproduce your workflow and analysis. 
We can ensure reproducibility and transparency by including a README.md document containing:
How to obtain NOAA NCEI API keys
How to run the provided code/scripts, as well as how to adjust for new time filtering
Steps to reproduce the results 
We can also include a requirements.txt for Python dependencies to ensure proper libraries have been downloaded. Finally, we’ll provide sample outputs and visualizations in the repository for reproducibility.

Metadata and data documentation (cf. Module 15): Metadata and data documentation to support discovery, understandability, and reuse.
We plan to create a data dictionary for all variables in the merged dataset, as well as including descriptive metadata, e.g., source, units, and description. As a final step, we can ensure documentation follows the FAIR principles as discussed in class: Findable, Accessible, Interoperable, and Reusable. 
