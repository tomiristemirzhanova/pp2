
from datetime import datetime

date1=input()
date2=input()

d1=datetime.strptime(date1, "%Y-%m-%d %H:%m:%s")
d2=datetime.strptime(date2, "%Y-%m-%d %H:%m:%s")

diff=d2-d1
seconds=diff.total_seconds

print(int(diff))

