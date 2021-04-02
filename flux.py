XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)

import pandas as pd

def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = pd.read_csv(XYZ)
    
    df['Dollar Flux'] = df['12/31/20'] - df['12/31/19']
    df['Percentage Flux'] = df['12/31/20'] / df['12/31/19']
    
    return list(tuple(df.loc[i]) for i in range(df.shape[0]))


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []

    return flagged_lines
    
print(calculate_flux(XYZ))