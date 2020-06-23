from dateutil.relativedelta import relativedelta
from datetime import datetime

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    timestamps = []
    
    for line in reboots.splitlines()[1:]:
        timestamps.append(datetime.strptime(line[-16:], "%a %b %d %H:%M"))
    
    timestamps = sorted(timestamps)
    timedeltas = []
    
    for i in range(1, len(timestamps)):
        timedeltas.append(timestamps[i] - timestamps[i-1])
    
    return max(timedeltas)
    pass