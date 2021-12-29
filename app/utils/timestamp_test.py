from utils.timestamp import *

def test_timestamp():
    date = timestamp_to_date(1640794133000)
    assert date.hour == 16
    assert date.minute == 8
    assert date.second == 53
    date = timestamp_to_date(1640810035000, format=True)
    assert date == "29/12/2021 - 20h33"
    date = timestamp_to_date(982792800000, format=True)
    assert date == "21/02/2001 - 22h00" #my birthday tbh
    date = timestamp_to_date(1340794133000, format=True)
    assert date == "27/06/2012 - 10h48"

test_timestamp()