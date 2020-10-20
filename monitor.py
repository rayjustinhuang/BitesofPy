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
    global violations
    start = time.time()
    
    #print(start)
    
    yield
    
    end = time.time()
    
    total_time = (end - start)
    
    #print(total_time)
    
    #seconds = total_time.total_seconds()

    if total_time >= OPERATION_THRESHOLD_IN_SECONDS:
        violations += 1
    
    if len(violations) >= ALERT_THRESHOLD:
        print(ALERT_MSG)
    pass