from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    spinner_cycle = cycle(SPINNER_STATES)
    
    for _ in range(round(seconds/STATE_TRANSITION_TIME)):
        sys.stdout.write(next(spinner_cycle))
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
        sys.stdout.write('\r')
    pass


if __name__ == '__main__':
    spinner(2)