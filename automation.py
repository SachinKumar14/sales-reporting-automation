from scripts.data_loader import load_data
from scripts.data_cleaner import clean_data
from scripts.analyzer import calculate_kpis
from scripts.analyzer import product_analysis
from scripts.analyzer import top_products
from scripts.analyzer import bottom_products
from scripts.analyzer import category_analysis
from scripts.analyzer import region_analysis
from scripts.analyzer import state_analysis
from scripts.analyzer import city_analysis
from scripts.analyzer import channel_analysis
from scripts.analyzer import monthly_sales_trend
from scripts.chart_generator import generate_category_chart
from scripts.chart_generator import generate_region_chart
from scripts.chart_generator import generate_state_chart
from scripts.chart_generator import generate_city_chart
from scripts.chart_generator import generate_channel_chart
from scripts.chart_generator import generate_monthly_trend_chart
from scripts.report_generator import generate_excel_report
from scripts.email_sender import send_email_with_report

# step 1 -load the data
df = load_data("data/Product_Dataset.csv")
print("Data loaded successfully")

# step 2 - clean the data
df = clean_data(df)
print("Data cleaned successfully")

# Step 3 - Calculate KPIs
kpis = calculate_kpis(df)

# Step 4 - Product Analysis
product_summary = product_analysis(df)

# Step 5 - Top 10 Products
top10 = top_products(product_summary)

# Step 6 - Bottom 10 Products
bottom10 = bottom_products(product_summary)

# Step 7- Category Analysis
category_summary = category_analysis(df)

# Step 8 -Region Analysis
region_summary = region_analysis(df)

# Step 9 - State Analysis
state_summary = state_analysis(df)

# Step 10 City Analysis
city_summary = city_analysis(df)

# Step 11 Channel Analysis
channel_summary = channel_analysis(df)

# Step 12 Monthly Sales trend
monthly_summary = monthly_sales_trend(df)

# Convert Period[M] to string so it can be written to Excel and plotted safely
monthly_summary["Order_Date"] = monthly_summary["Order_Date"].astype(str)

print("KPI analysis completed")

# Step 13 Generate Category Wise Revenue Chart
generate_category_chart(category_summary)

# Step 14 Generate Region Wise Revenue Chart
generate_region_chart(region_summary)

# Step 15 Generate State Wise Revenue Chart
generate_state_chart(state_summary)

# Step 16 Generate City Wise Revenue chart
generate_city_chart(city_summary)

# Step 17 Generate Channel Wise Revenue chart
generate_channel_chart(channel_summary)


# Step 18 Generate Monthly Sales Trend chart
generate_monthly_trend_chart(monthly_summary)

print("Charts generated successfully")

generate_excel_report(
    kpis,
    product_summary,
    top10,
    bottom10,
    category_summary,
    region_summary,
    state_summary,
    city_summary,
    channel_summary,
    monthly_summary
)

print("Excel report generated successfully")

send_email_with_report(
    sender_email="your_email@gmail.com",
    app_password="your_app_password",
    receiver_email="receiver_email@gmail.com",
    file_path="reports/Sales_Report.xlsx"
)
print("Email sent successfully")





