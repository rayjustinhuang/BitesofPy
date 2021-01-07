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
    assert str(iplist[-1]) == (f"54.250.251.0/24 is allocated to the WORKSPACES_GATEWAYS "
                                f"service in the ap-northeast-1 region")
    assert str(iplist[1]) == (f"18.208.0.0/13 is allocated to the AMAZON "
                                f"service in the us-east-1 region")
    assert len(iplist) == 1886
    assert type(iplist[0]) == ServiceIPRange
    assert iplist[0] == ServiceIPRange(service='AMAZON', region='eu-west-1', cidr=IPv4Network('13.248.118.0/24'))
                                
def test_error_get_aws_service_range(json_file):
    iplist = parse_ipv4_service_ranges(json_file)
    
    with pytest.raises(ValueError):
        get_aws_service_range('invalid string', iplist)
    
    with pytest.raises(ValueError):
        get_aws_service_range('52.95.245.0/24', iplist)

def test_working_get_aws_service_range(json_file):
    iplist = parse_ipv4_service_ranges(json_file)
    assert ServiceIPRange(service='AMAZON', region='us-east-1', cidr=IPv4Network('52.95.245.0/24')) in get_aws_service_range('52.95.245.0', iplist)
    

    
#def serviceIPrange():
#    print(json_file())
#    print(parse_ipv4_service_ranges(json_file()))
#    print(len(parse_ipv4_service_ranges(json_file())))

#serviceIPrange()    