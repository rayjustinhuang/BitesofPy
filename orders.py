from os import path
from urllib.request import urlretrieve

import pandas as pd

EXCEL = path.join('/tmp', 'order_data.xlsx')
if not path.isfile(EXCEL):
    urlretrieve('https://bit.ly/2JpniQ2', EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(EXCEL, sheet_name='SalesOrders')
    pass

df=load_excel_into_dataframe()

def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df['Year'] = df['OrderDate'].dt.year
    return df.groupby(['Year','Region'])['Total'].sum()
    pass

#get_year_region_breakdown(df)
#print(df.columns)

def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    best_rep_df = df.groupby(['Rep'])['Total'].sum()
    return (best_rep_df.idxmax(), best_rep_df.loc[best_rep_df.idxmax()])
    pass

#print(get_best_sales_rep(df))

def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    most_sold_df = df.groupby(['Item'])['Units'].sum()
    return (most_sold_df.idxmax(), most_sold_df.loc[most_sold_df.idxmax()])
    pass

#print(get_most_sold_item(df))