import pandas as pd
def clean_data(df):
    #1.converts datatype.
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    #2.Remove duplicates
    df.drop_duplicates(inplace = True)

    return df