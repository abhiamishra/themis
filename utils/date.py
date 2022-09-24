import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time(dt: datetime):
    return int((dt - epoch).total_seconds() * 1000)
