from datetime import date

import dateutil.rrule

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    #print(TODAY + dateutil.relativedelta.relativedelta(days=100))
    
    print(list(dateutil.rrule.rrule(dateutil.rrule.DAILY, count=100, dtstart=TODAY)))
    pass

get_hundred_weekdays()