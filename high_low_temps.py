from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value
         
    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    temp_data = pd.read_csv(DATA_FILE)
    
    temp_data['Date'] = pd.to_datetime(temp_data['Date'])
    
    temp_data['No 29th'] = temp_data['Date'].dt.day != 29 
    temp_data['No Feb'] = temp_data['Date'].dt.month != 2
    temp_data['No Feb 29'] = temp_data[['No 29th', 'No Feb']].any(axis='columns')
    
    temp_data = temp_data[temp_data['No Feb 29']][['ID', 'Date', 'Element','Data_Value']]
    temp_data['Temp'] = temp_data['Data_Value']/10
    
    pivoted_temp = pd.pivot_table(temp_data, index=['ID','Date'], columns='Element', values='Temp')
    pivoted_temp = pivoted_temp.reset_index()
    
    pivoted_05_to_14 = pivoted_temp[pivoted_temp['Date'].dt.year != 2015].copy()
    pivoted_15 = pivoted_temp[pivoted_temp['Date'].dt.year == 2015].copy()
    
    #print(pivoted_05_to_14.head())
    #print(pivoted_15.head())
    
    pivoted_05_to_14['MonthDay'] = pivoted_05_to_14['Date'].dt.dayofyear
    pivoted_15['MonthDay'] = pivoted_15['Date'].dt.dayofyear
    
    max_temps_0514 = pivoted_05_to_14.groupby(['ID', 'MonthDay'])['TMAX'].max().reset_index()
    min_temps_0514 = pivoted_05_to_14.groupby(['ID', 'MonthDay'])['TMIN'].min().reset_index()
    
    
    comparison_df = pd.merge(pivoted_15, max_temps_0514, how='left', left_on=['ID','MonthDay'], right_on=['ID','MonthDay'])
    comparison_df = pd.merge(comparison_df, min_temps_0514, how='left', left_on=['ID','MonthDay'], right_on=['ID','MonthDay'])
    
    #print(comparison_df.head())
    
    comparison_df['high 2015'] = comparison_df['TMAX_x'] > comparison_df['TMAX_y']
    comparison_df['low 2015'] = comparison_df['TMIN_x'] < comparison_df['TMIN_y']
    
    high_df = comparison_df[comparison_df['high 2015']]
    low_df = comparison_df[comparison_df['low 2015']]
    
    high_df = high_df[['ID','Date','TMAX_x']]
    low_df = low_df[['ID','Date','TMIN_x']]
    
    high_value = high_df.loc[high_df['TMAX_x'].idxmax()]
    low_value = low_df.loc[low_df['TMIN_x'].idxmin()]
    
    #print(high_value['ID'])
    
    high_2015 = STATION(ID=high_value['ID'], Date=high_value['Date'].date(), Value=high_value['TMAX_x'])
    low_2015 = STATION(ID=low_value['ID'], Date=low_value['Date'].date(), Value=low_value['TMIN_x'])
    
    return (high_2015, low_2015)
    
    pass