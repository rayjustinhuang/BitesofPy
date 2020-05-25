from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if type(date) != datetime:
        raise ValueError
    if date > NOW:
        raise ValueError
    
    diff = (NOW - date).total_seconds()
    
    print(diff)
    
    if diff <= DAY*2:
        for timeoffset in TIME_OFFSETS:
            if timeoffset.offset > diff:
                if timeoffset.divider == None:
                    try:
                        return timeoffset.date_str.format(int(diff))
                    except:
                        return timeoffset.date_str
                else:
                    return timeoffset.date_str.format(int(diff/timeoffset.divider))
    else:
        date.strftime('%m/%d/%Y')
    pass