from time import time
from datetime import datetime

def now() :
    return int(round(time() * 1000))

def timestamp_to_date(timestamp:int,format=False):
    if format==True:
        d = datetime.utcfromtimestamp(timestamp/1000)
        return f"{d.day}/{d.month}/{d.year} - {d.hour}h{d.minute}"
    return datetime.utcfromtimestamp(timestamp/1000)