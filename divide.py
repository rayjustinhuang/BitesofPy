def positive_divide(numerator, denominator):
    try:
        q = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
    else:
        if q < 0:
            raise ValueError
        return q
    pass