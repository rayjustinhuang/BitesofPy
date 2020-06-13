from datetime import datetime, date

import pandas as pd

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    ordered_dates = sorted(dates)
    
    return [i.date() for i in pd.date_range(ordered_dates[0], ordered_dates[-1], freq='D') if i.date() not in dates]
    pass