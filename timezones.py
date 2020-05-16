import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    boolean = []
    
    timezone_list = list(timezones)[0]
    
    print(timezone_list)
    
    for i in range(len(timezone_list)):
        tz = pytz.timezone(timezone_list[i])
        boolean.append(pytz.utc.localize(utc).astimezone(tz))
    
    return boolean
    pass

utc = datetime(2018, 4, 18, 13, 28)
timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

print(within_schedule(utc, timezones))