# **Status Report:** 

## **Overview**
This project investigates the impact of climate factors on corn harvests in Illinois over time. By integrating NOAA Global Summary of the Month weather data with USDA NASS corn commodity data, we aim to analyze how climate variables influence corn yield, planted area, and other related variables year over year. 

## **Updated Timeline**

### **Weeks 1–2**: Both of these tasks have been completed!
Acquire NOAA GSOM and USDA NASS datasets (via API and download)
Store raw data in tabular CSV format and document characteristics.

The notebooks where we complete these tasks are under the “Notebooks” folder in the GitHub repository. The raw data can be found in the “raw” folder under the “data” branch in the GitHub repository.

**Locations:**
- Notebooks: `/Notebooks/`  
- Raw data: `/data/raw/`

### **Weeks 3–4** Both of these tasks have been completed!
Organize and clean datasets (naming, formats, missing values).
Assess and document data quality.

The notebooks where we complete these tasks are under the “Notebooks” folder in the GitHub repository. Both of these notebooks organize and clean the datasets while assessing the data quality and creating derived variables for analysis.

**Locations:**
- Notebooks: `/Notebooks/`

### **Weeks 5–6 (Nov 15–22)**: These tasks will be completed the week following the submission of this status report.
Integrate datasets (merge by year) and derive features (growing-season averages).
Note: We completed the feature derivation within the GSOM_Cleaning_Notebook
Begin exploratory analysis and create initial visualizations.

We will create a master analysis Jupyter notebook to complete these tasks and place it in the “Notebooks” folder of the GitHub repository.

### **Weeks 7–8 (Dec 1–10)**: These tasks will be completed following Thanksgiving break and before the deadline
Automate workflow and/or outline workflow processes.
Finalize report (README.md), metadata, and reproducibility documentation.
Note: We have partially created the metadata and reproducibility documentation for the acquisition of both NASS and GSOM data. This can be found in the documentation branch of our repo. 
Tag and release the final GitHub version.

## **Task Updates by Module**

_Data lifecycle (cf. Module 1): Relate your project to one or more of the lifecycle models discussed in class._ 
Formulate Research Question: Defining a clear research question with attainable goals and objectives while ensuring the data to answer said question exists or can be attained. 
Collect Data / Acquisition: Pull NOAA climate and USDA corn data via their respective methods
Storage and Organization: Save raw data as a CSV in a structured GitHub repository
Cleaning and Quality Assessment: Handle missing values, inconsistent formats, and outliers within our dataset
Integration and Analysis: Merge datasets by year, ensuring year identifiers are in the same format (Lifecycle step 3). We can then generate derived features such as seasonal averages
Visualization and Modeling: Explore correlations and build predictive models in Python
Archival and Reuse: Document workflow, provide metadata tags, and release the GitHub repository for reproducibility 

**Updated task:** We successfully pulled the NOAA climate data and USDA corn data via their respective methods and have stored both the raw data and processed data as a CSV in their respective GitHub repositories. We’ve also proceeded with cleaning and assessment, creating two notebooks that handle missing values, create derived variables, and assess the overall quality of each variable. We have yet to create a merged dataset; however, we have annualized the GSOM dataset.

_Ethical data handling (cf. Module 2): Identification of all ethical, legal, or policy constraints and how they were addressed. This includes issues related to consent, privacy/confidentiality, copyright, licenses and terms of use._
Both datasets, NCEI and NASS of the USDA, are public domain, so no individual consent is required. Regarding API usage, we will respect the terms of use for APIs (limiting requests to 5 per second) as well as adhere to document attribution for NCEI and USDA. Data storage will happen in the GitHub repository, with personal identifiable information not included, and is non applicable to our dataset. 

**Updated task:** After pulling our respective datasets, we’ve ensured our processes adhere to the API terms of use and no subsequent personal information is included within our datasets. 

_Data collection and acquisition (cf. Module 3): Collection or acquisition of at least 2 different datasets from distinct trustworthy sources. Selected datasets should either have different access methods (e.g., APIs) or formats/schemas._
NOAA GSOM: API request for Champaign, IL, retrieved as CSV/JSON
USDA NASS: Download of CSV for Illinois corn data. 
Each dataset uses a distinct access method, i.e., API request and download. 

**Updated task:** We successfully pulled the NOAA GSOM data via API and have stored it in a raw CSV format within our GitHub filesystem. Additionally, we’ve downloaded the USDA NASS CSV for Illinois corn data and have stored it within the raw data folder as well. Both methods have reproducibility information included in the documentation folder of our repository.  

_Storage and organization (cf. Modules 4-5): Select and describe a specific storage and organization strategy. This may include use of tabular, relational, or semi-structured models via filesystems or databases as well as filesystem structures and naming conventions._
We plan on storing the data as tabular CSV files in the GitHub repository, ensuring the filenames and directories follow clear naming conventions for reproducibility. 

**Updated task:** For this task, we have created several folders in our repository to store our notebooks and data. Each folder and document title is easily interpretable. We have also separated each of the raw, processed, and cleaned datasets into their own respective folders. 

_Extraction and enrichment (cf. Module 6):_
We plan on calculating derived variables such as growing-season mean temperature, total precipitation, and temperature/precipitation outliers. We believe these manufactured variables will enrich our dataset and provide new insights. 

**Updated task:** We created several derived variables to capture key agricultural and climactic characteristics of each year. These include Growing Degree Days (GDD) to quantity heat accumulation, temperature range as a measure of thermal amplitude, precipitation deviation to evaluate moisture conditions, and stress indicators such as heat days anf forst days. These variables enhance the dataset by summarizing seasonal patterns and extreme events which could directly affect crop growth and yield. 

_Data integration (cf. Module 7-8): Integration of datasets (Python/Pandas or SQL)_
We plan on merging our NOAA and USDA data by year, utilizing Pandas. By left-joining our USDA dataset with the NOAA annual summaries, we can validate matching years and handle missing entries. We will also look into schema documentation creation to describe the integrated dataset variables. 

**Updated task:** We have not merged our USDA and NOAA cleaned datasets yet; however, this will be our next task. We will most likely still use a left-join and validate by matching years.

_Data quality (cf. Module 9): Document data quality assessment results._
We plan on identifying missing values in climate and crop data as well as assessing outliers, e.g., extreme yields or precipitation values. We will also document coverage gaps, looking for any general inconsistencies in weather station data or reporting. 

**Updated task:** For data quality assessment we examined missing values, outliers, and calculated the overall dataset completeness. We found when working with our NASS data that it was already extremely clean and chose to include missing values for acres_planted as we will determine the imputation methods in the analysis section. We also evaluated annual coverage and reporting consistency for the GSOM dataset to ensure reliablei integration with the NASS dataset. 

_Data cleaning (cf. Module 10): Describe any data cleaning methods applied (e.g., missing values, outliers, syntactic or semantic cleaning)_
We plan to convert any string numeric values into numeric types, as well as handling missing or flagged values as NaN. After doing preliminary analysis, we intend to normalize temperature units and precipitation measures if necessary. Additionally, ensuring consistent year identifiers are available for integration will be crucial to our left-join process. 

**Updated task:** For data cleaning, we reviewed temperature and precipitation units for consistency, ensuring all temperatures are in Fahrenheit while all precipitation is in milimeters. We also verified that year identifiers were correctly formatted and aligned across both datasets to support accurate integration. We also verified all values are in their correct datatypes. 

_Workflow automation and provenance (cf. Module 11-12): Provide an automated end-to-end workflow._
We can design and implement an end-to-end Python workflow:
Pull data from APIs
Perform cleaning, aggregation, and merging
Conduct analysis and generate visualizations based on findings
Document and interpret visualizations 

**Updated Task:** Since we are still in the earlier stages of our project, we have not gotten to this task yet, but it will be addressed soon.

_Reproducibility and transparency (cf. Module 13):  Your project must provide sufficient information to allow someone else to reproduce your workflow and analysis._
We can ensure reproducibility and transparency by including a README.md document containing:
How to obtain NOAA NCEI API keys
How to run the provided code/scripts, as well as how to adjust for new time filtering
Steps to reproduce the results 
We can also include a requirements.txt for Python dependencies to ensure proper libraries have been downloaded. Finally, we’ll provide sample outputs and visualizations in the repository for reproducibility.

**Updated Task:** Within the GSOM_Acquisition workbook I’ve added a self-populating text file documenting how to obtain the NOAA API keys, as well as reproducibility steps for obtaining the same file. Additionally, within the /documentation branch of our repository I’ve included a markdown file detailing how to generate the NASS dataset we use, along with reproducibility steps and a direct URL to download said dataset. Additionally, each notebook will contain an introduction comment section detailing the purpose, inputs, outputs, and reproducibility information. 

_Metadata and data documentation (cf. Module 15): Metadata and data documentation to support discovery, understandability, and reuse._
We plan to create a data dictionary for all variables in the merged dataset, as well as including descriptive metadata, e.g., source, units, and description. As a final step, we can ensure documentation follows the FAIR principles as discussed in class: Findable, Accessible, Interoperable, and Reusable. 

**Updated Task:** We’ve created a data dictionary for the derived and updated variables for the clean and annualized GSOM dataset; however, since we have yet to merge both datasets I have not created a “master” data dictionary for this dataset yet. To see the data dictionary for the derived variables please visit /Notebooks/GSOM_Cleaning_Notebook.ipynb. 

## **Description Summary:**
The project plan itself has remained the same. We have been able to stay on track with our timeline and have yet to come across anything we’ve needed to revise. Thus far, we have acquried both datasets and performed quality checks and cleaning on the data. Based on the feedback we have received for Milestone 2, **we have added a “Constraints” and “Gaps” section to our project plan** as we did not include this section upon our first submission.
