import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    times = []
    
    timezone_list = list(timezones)[0]
    
    for i in range(len(timezone_list)):
        if timezone_list[i] not in TIMEZONES:
            raise ValueError
        tz = pytz.timezone(timezone_list[i])
        times.append(pytz.utc.localize(utc).astimezone(tz))
    
    boolean = []
    
    for time in times:
        if time.hour in MEETING_HOURS:
            boolean.append(True)
        else:
            boolean.append(False)
            
    answer = all(boolean)
    
    return answer
    pass

#utc = datetime(2018, 4, 18, 13, 28)
#timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
