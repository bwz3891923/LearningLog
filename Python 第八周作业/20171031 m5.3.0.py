from datetime import *


someday=datetime(2016,9,16,22,33,32,47)
print(someday)

today=datetime.now()
print(today)

today1=datetime.utcnow()
print(today1)

print(someday.isoformat())
print(someday.isoweekday())

print(someday.strftime("%Y-%m-%d %H:%M:%S"))
