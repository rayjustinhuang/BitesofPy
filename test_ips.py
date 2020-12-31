import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...
def test_serviceIPrange(json_file):
    iplist = parse_ipv4_service_ranges(json_file)
    assert str(iplist[0]) == (f"13.248.118.0/24 is allocated to the AMAZON "
                                f"service in the eu-west-1 region")
                                
def test_get_aws_service_range(json_file):
    iplist = parse_ipv4_service_ranges(json_file)
    with pytest.raises(ValueError):
        get_aws_service_range(123456, iplist) 
    

    
#def serviceIPrange():
#    print(json_file())
#    print(parse_ipv4_service_ranges(json_file()))

#serviceIPrange()    