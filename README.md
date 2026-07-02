# Sales Reporting Automation

This project automates sales data analysis and reporting using Python.

## Features
- Loads sales data from CSV
- Cleans and prepares the data
- Calculates KPIs like revenue, profit, total orders, and customer rating
- Performs product, category, region, state, city, channel, and monthly trend analysis
- Generates charts automatically
- Creates an Excel report with multiple analysis sheets
- Sends the report by email automatically

## Tech Stack
- Python
- Pandas
- Matplotlib
- OpenPyXL

## Project Structure
- `automation.py` → main pipeline file
- `scripts/data_loader.py` → load dataset
- `scripts/data_cleaner.py` → clean data
- `scripts/analyzer.py` → KPI and analysis logic
- `scripts/chart_generator.py` → chart generation
- `scripts/report_generator.py` → Excel report generation
- `scripts/email_sender.py` → email automation

## Output
- Excel report in `reports/Sales_Report.xlsx`
- Charts saved in `charts/`

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the automation:
    ```bash
    python automation.py
    ```
## Author
Sachin kumar Chauhan
