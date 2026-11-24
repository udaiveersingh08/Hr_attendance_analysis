# HR Attendance Analysis using Python & Pandas

## Project Overview
This project focuses on analyzing HR attendance and workforce data using **Python and Pandas**. The goal is to inspect attendance records, identify data quality issues, clean the dataset, and prepare useful outputs that can support HR reporting and workforce analysis.

The project covers employee attendance, working hours, late arrivals, work modes, departments, completed tasks, and performance ratings.

## Business Scenario
Imagine working as a Data Analyst supporting an HR team. The HR team wants to understand attendance patterns, late arrivals, working hours, and performance-rating records. The analyst's responsibility is to identify data-quality issues and prepare the data for further analysis.

## Dataset Information
- **Dataset:** `02_hr_attendance.csv`
- **Total records:** 2,408 rows
- **Total columns:** 10
- **Duplicate rows :** 8

### Dataset Columns

| Column | Description |
|---|---|
| `record_id` | Unique attendance record identifier |
| `employee_id` | Employee identifier |
| `date` | Attendance date |
| `department` | Employee department |
| `attendance_status` | Attendance status |
| `work_mode` | Work arrangement (Office, Remote, Hybrid, etc.) |
| `hours_worked` | Number of hours worked |
| `late_arrival` | Indicates whether the employee arrived late |
| `tasks_completed` | Number of tasks completed |
| `performance_rating` | Recorded performance rating |

## Project Objectives
- Inspect the dataset structure, data types, and dimensions.
- Identify missing values and exact duplicate rows.
- Clean department and work-mode text values.
- Convert the date column into datetime format.
- Convert performance ratings into numeric format.
- Create useful attendance indicators.
- Analyze attendance status, late arrivals, and working hours.
- Identify records that need further review.
- Export cleaned data and selected analysis outputs.

## Tools & Technologies
- **Python**
- **Pandas**
- **Jupyter Notebook**
- **CSV**

## Key Pandas Concepts Used
- `read_csv()`, `head()`, `shape`, `info()`
- `isna()` and `sum()`
- `duplicated()` and `drop_duplicates()`
- `fillna()`, `astype()`, `str.strip()`, `str.title()`
- `to_datetime()` and `to_numeric()`
- Boolean masks and conditional filtering
- `loc[]` and `iloc[]`
- `sort_values()` and `head()`
- `value_counts()` and `describe()`
- Calculated columns and CSV export using `to_csv()`

## Project Workflow

### 1. Data Loading & Inspection
- Load the CSV file using Pandas.
- Check the number of rows and columns.
- Inspect sample records and data types.
- Review missing values and duplicate rows.

### 2. Data Cleaning
- Remove exact duplicate rows.
- Convert the `date` column into datetime format.
- Fill missing department and work-mode values with `Unknown`.
- Standardize department text using trimming and title case.
- Convert performance ratings into numeric format.
- Review missing performance ratings instead of automatically replacing them with an average.

### 3. Feature Engineering
Create additional columns to support analysis:
- `is_absent` – identifies absent records.
- `is_late` – identifies late-arrival records.
- `is_full_workday` – identifies records with at least 7.5 working hours.
- `month` – extracts the year and month from the attendance date.

### 4. HR Data Analysis
The project investigates questions such as:
- What is the distribution of attendance statuses?
- How many unique employees are present in the dataset?
- Which department has the highest number of records?
- How many late-arrival records are there?
- What are the average and median working hours?
- How many records have more than 0 but fewer than 5 working hours?
- How are performance ratings distributed?
- Which records have the 15 highest working-hour values?
- Are there records marked `Absent` with positive working hours that need review?


## Data Quality Notes
The raw dataset contains:
- 8 exact duplicate rows.
- 24 missing values in `department`.
- 19 missing values in `work_mode`.
- 14 missing values in `performance_rating`.


## Project Outcome
This project demonstrates practical use of Pandas for data inspection, data cleaning, missing-value handling, duplicate detection, datetime conversion, conditional filtering, descriptive statistics, feature engineering, and CSV export.

## Author
**Udaiveer Singh**

**Project:** HR Attendance & Workforce Analysis  
**Domain:** Data Analytics  
**Tools:** Python | Pandas | Jupyter Notebook
