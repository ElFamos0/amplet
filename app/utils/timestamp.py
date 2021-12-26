from time import time
from datetime import datetime

def now() :
    return int(round(time() * 1000))

def timestamp_to_date(timestamp:int):
    return datetime.utcfromtimestamp(timestamp/1000)