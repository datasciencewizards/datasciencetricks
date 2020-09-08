import datetime

#getting current time and formatting
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"))
# >>> '09/09/2020 00:49:56'

#getting today's date
today = datetime.date.today()
print(today)
# >>> 2020-09-09

#extracting day and month
print('Day:', today.day, 'Month:', today.month)
# >>> Day: 9 Month: 9

#creating datetime object
sample = datetime.datetime(year=2011, month=6, day=17)
print(sample)
# >>> 2011-06-17 00:00:00
