from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    start = get_today()
    
    yield
    
    end = get_today()
    
    total_time = (end - start)
    
    seconds = total_time.total_seconds()
    
    violations = seconds % OPERATION_THRESHOLD_IN_SECONDS
    
    if violations >= ALERT_THRESHOLD:
        print(ALERT_MSG)
    pass