def calculate_kpis(df):

    """ Calculate overall business KPIs.
    """
    total_revenue = df["Sales"].sum().round(2)

    total_profit = df["Profit"].sum().round(2)

    total_orders = df["Order_ID"].nunique()

    average_customer_rating = df["Customer_Rating"].mean().round(2)


    return {
            "Total Revenue" : total_revenue,
            "Total Profit" : total_profit,
            "Total Orders": total_orders,
            "Average Customer Rating": average_customer_rating
        }


def product_analysis(df):
     
     """
    Analyze product performance.
    """
     product_summary = (df.groupby("Product_Name")
                        .agg(Total_Revenue = ("Sales", "sum"),
                             Total_Profit = ("Profit","sum"),
                             Total_Quantity = ("Quantity","sum")
                             ).reset_index()
                             )

     return product_summary

def top_products(product_summary,n =10):
     
     """ Return the top 10 products by revenue."""
     
     top10 = (
        product_summary
        .sort_values(by="Total_Revenue", ascending=False)
        .head(n)
)

     return top10

def bottom_products(product_summary,n = 10):

     """Return the bottom products by revenue"""
     bottom10 = (product_summary.sort_values(
          by  = "Total_Revenue",ascending = True
     ).head(n))
     return bottom10


def category_analysis(df):

     """Category performance analysis"""
     category_summary = (df.groupby("Category").
                         agg(Total_Revenue = ("Sales","sum"),
                             Total_Profit = ("Profit","sum"),
                             Total_Quantity = ("Quantity","sum"))).reset_index()
     return category_summary
     

def region_analysis(df):

     """Region performance analysis"""
     region_summary = (df.groupby("Region").agg(
          Total_Revenue = ("Sales","sum"),
          Total_Profit = ("Profit","sum"),
          Total_Quantity = ("Quantity","sum")
     )).reset_index()

     return region_summary

def state_analysis(df):

     """State Performance analysis"""

     state_summary = (df.groupby("State").agg(
          Total_Revenue = ("Sales","sum"),
          Total_Profit = ("Profit","sum"),
          Total_Quantity = ("Quantity","sum")
     )).reset_index()

     return state_summary

def city_analysis(df):

     """Citywise Performance analysis"""

     city_summary = (df.groupby("City").agg(
          Total_Revenue = ("Sales","sum"),
          Total_Profit = ("Profit","sum"),
          Total_Quantity = ("Quantity","sum")
     )).reset_index()

     return city_summary


def channel_analysis(df):

     """Channelwise performance analysis"""

     channel_summary = (df.groupby("Sales_Channel").agg(
          Total_Revenue = ("Sales","sum"),
          Total_Profit = ("Profit","sum"),
          Total_Quantity = ("Quantity","sum")
     )).reset_index()

     return channel_summary

def monthly_sales_trend(df):

     """Monthly Performance analysis"""
     monthly_summary = (df.groupby(df["Order_Date"].dt.to_period("M")).agg(
          Total_Revenue = ("Sales","sum"),
          Total_Profit = ("Profit","sum"),
          Total_Quantity = ("Quantity","sum")

     )).reset_index()

     return monthly_summary