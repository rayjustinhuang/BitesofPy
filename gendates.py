from datetime import datetime,timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    
    working_date = PYBITES_BORN
    special_dates = []
    
    while working_date.year < 2018:
        working_date = working_date.replace(year=working_date.year + 1)
        special_dates.append(working_date)
    
    working_date = PYBITES_BORN
        
    while working_date < PYBITES_BORN.replace(year = 2018):
        working_date = working_date + timedelta(days=100)
        special_dates.append(working_date)
        
    return special_dates
    
    pass