from datetime import date

from dateutil.rrule import rrule, YEARLY, SU


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    mothers_day_list = list(rrule(YEARLY, count=10, bymonth=5, byweekday=SU(2), dtstart=date(2014, 1, 1)))
    
    year_to_use = [repr(i.date()) for i in mothers_day_list if i.year == year][0]
    
    return year_to_use
    pass