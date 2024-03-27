import datetime
today = datetime.datetime.now()
print(today.date(), "\n", today.time().replace(microsecond=0))
