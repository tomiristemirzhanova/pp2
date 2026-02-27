#1.Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

current_date=datetime.now()
new_date=current_date-timedelta(days=5)

print (current_date)
print (new_date)

#2. Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)

#3. Write a Python program to drop microseconds from datetime.

from datetime import datetime

now = datetime.now()
without_m= now.replace (microsecond=0)

print (now)
print (without_m)


#4. Write a Python program to calculate two date difference in seconds.

from datetime import datetime

d1=datetime (2026, 2, 27, 12, 0, 0)
d2=datetime(2026, 2, 28, 16, 30, 0)

difference=d1-d2
seconds=difference.total_seconds()

print(difference)