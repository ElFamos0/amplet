from utils.timestamp import *

def test_timestamp():
    date = timestamp_to_date(1640794133000)
    assert date.hour == 16
    assert date.minute == 8
    assert date.second == 53
    date = timestamp_to_date(1640794133000, format=True)
    assert date == "29/12/2021 - 16h08"
    date = timestamp_to_date(1340794133000, format=True)
    assert date == "27/06/2012 - 10h48"