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
    start = time()
    
    yield
    
    end = time()
    
    total_time = (end - start)

    if total_time >= OPERATION_THRESHOLD_IN_SECONDS:
        today = [get_today()]
        violations.update(today)
    
    if sum(violations.values()) >= ALERT_THRESHOLD:
        print(ALERT_MSG)
    pass

#with timeit():
#    print(abcd)
#    sleep(2)