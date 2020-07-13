import datetime


def tomorrow(date = datetime.datetime.today().date()):
    # Your code goes here
    return date + datetime.timedelta(days=1)