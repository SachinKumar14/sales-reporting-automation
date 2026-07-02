import matplotlib.pyplot as plt


def generate_category_chart(category_summary):

    """Generate Category Revenue Bar Chart"""

    fig = plt.figure(figsize= (10,6))
    x = category_summary["Category"]
    y = category_summary["Total_Revenue"]
    plt.bar(x,y,color= "skyblue")
    plt.title("Category Wise Total Revenue")
    plt.xlabel("Category")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
  
    plt.tight_layout()
    plt.savefig("charts/category_revenue.png")
    plt.close(fig)
   
  
def generate_region_chart(region_summary):

    """Generate Region Wise Revenue bar chart"""
    fig = plt.figure(figsize=(10,6))

    x = region_summary["Region"]
    y = region_summary["Total_Revenue"]

    plt.bar(x,y,color ="skyblue")
    plt.title("Region Wise Total Revenue")
    plt.xlabel("Region")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation = 45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("charts/region_revenue.png")
    plt.close(fig)


def generate_state_chart(state_summary):

    fig = plt.figure(figsize=(10,6))
    """Generate State wise Revenue bar chart"""
    x = state_summary["State"]
    y = state_summary["Total_Revenue"]

    plt.bar(x,y,color ="skyblue")
    plt.title("State Wise Total Revenue")
    plt.xlabel("State")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation = 45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("charts/Statewise_revenue.png")
    plt.close(fig)

def generate_city_chart(city_summary):

    fig = plt.figure(figsize=(10,6))
    """Generate city wise Revenue bar chart"""
    x = city_summary["City"]
    y = city_summary["Total_Revenue"]

    plt.bar(x,y,color ="skyblue")
    plt.title("City Wise Total Revenue")
    plt.xlabel("City")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation = 45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("charts/Citywise_revenue.png")
    plt.close(fig)


def generate_channel_chart(channel_summary):
    """Generate channel wise Revenue bar chart"""

    fig = plt.figure(figsize=(10,6))
    
    x = channel_summary["Sales_Channel"]
    y = channel_summary["Total_Revenue"]

    plt.bar(x,y,color ="#1d60f0",edgecolor = "black")
    plt.title("Channel Wise Total Revenue")
    plt.xlabel("Channel")
    plt.ylabel("Total Revenue")
    plt.grid(axis="x", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.savefig("charts/Channelewise_revenue.png")
    plt.close(fig) 

def generate_monthly_trend_chart(monthly_summary):

    """Generate Monthly Sales Trend Chart"""
    fig = plt.figure(figsize =(10,6))
    x = monthly_summary["Order_Date"].astype(str)
    y = monthly_summary["Total_Revenue"]

    plt.plot(x,y,color = "darkblue",marker = 'o',linewidth = 2)
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.grid(alpha = 0.3)
    plt.tight_layout()
    plt.savefig("charts/Monthly_Sales_Trend.png")
    plt.close(fig) 