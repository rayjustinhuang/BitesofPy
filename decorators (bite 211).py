from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    @wraps(func)
    # ... retry MAX_RETRIES times
    def looper():
    for i in range(MAX_RETRIES):
    # make sure you include this for testing:
        try:
            func
        except Exception as exc:
            print exc
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    pass