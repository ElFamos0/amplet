from time import time
from datetime import datetime

def until(t):
    return t-now()

def now() :
    return int(round(time() * 1000))

def timestamp_to_date(timestamp:int,format=False):
    if format==True:
        d = datetime.utcfromtimestamp(timestamp/1000)
        return f"{d.day:02d}/{d.month:02d}/{d.year:02d} - {d.hour:02d}h{d.minute:02d}"
    return datetime.utcfromtimestamp(timestamp/1000)