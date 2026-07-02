# Sales Reporting Automation

An end-to-end Python automation project that reads raw sales data from CSV, cleans and transforms it, calculates business KPIs, performs multi-level sales analysis, generates charts, creates a formatted Excel report, and emails the report automatically.

---

## Project Objective
The goal of this project is to automate the manual sales reporting workflow by building a reusable Python pipeline that:
- ingests raw sales data
- cleans and validates the dataset
- calculates business KPIs
- performs product, category, region, state, city, channel, and monthly trend analysis
- generates charts automatically
- exports a multi-sheet Excel report
- emails the final report to stakeholders

---

## Features
- Loads sales data from CSV
- Cleans and prepares the data
- Calculates KPIs such as:
  - Total Revenue
  - Total Profit
  - Total Orders
  - Average Customer Rating
- Performs:
  - Product Analysis
  - Top / Bottom Product Analysis
  - Category Analysis
  - Region Analysis
  - State Analysis
  - City Analysis
  - Channel Analysis
  - Monthly Sales Trend Analysis
- Generates charts automatically using Matplotlib
- Creates a formatted Excel report using OpenPyXL
- Sends the final report via email using SMTP

---

## Tech Stack
- Python
- Pandas
- Matplotlib
- OpenPyXL
- SMTP / Email automation

---

## Project Structure
```bash
sales_automation/
│
├── automation.py                  # Main pipeline script
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
│
├── data/
│   └── Product_Dataset.csv        # Input dataset
│
├── charts/                        # Generated charts
│
├── reports/                       # Generated Excel report (ignored in Git)
│
├── notebooks/
│   └── 01_Load_Data.ipynb         # Notebook experimentation / practice
│
└── scripts/
    ├── __init__.py
    ├── data_loader.py             # Data loading logic
    ├── data_cleaner.py            # Data cleaning logic
    ├── analyzer.py                # KPI + analysis functions
    ├── chart_generator.py         # Chart generation logic
    ├── report_generator.py        # Excel report generation
    └── email_sender.py            # Email automation