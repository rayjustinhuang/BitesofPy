from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    
    delta = PY2_DEATH_DT - start_date
    
    return round(delta.days *24 + delta.seconds / 3600,2)
    
    pass


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    
    delta = PY2_DEATH_DT - start_date
    
    earth_hours = round(delta.days *24 + delta.seconds / 3600,2)
    
    conversion = 365*24*7
    
    miller_minutes = round(earth_hours/conversion * 60,2)
    
    return miller_minutes
    pass