import datetime


def tomorrow(tdy = None):
    
    if tdy == None:
        tdy = datetime.date.today()
    
    return tdy + datetime.timedelta(days=1)