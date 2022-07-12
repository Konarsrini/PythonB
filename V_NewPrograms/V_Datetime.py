"""
Python Datetime
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

Example
Import the datetime module and display the current date:
"""
import datetime

x = datetime.datetime.now()
# x = datetime.datetime(2021, 9, 12)
print(x)
# 2021-09-12 17:42:36.283558
"""
Date Output
When we execute the code from the example above the result will be:

2021 - 09 - 12 17: 38: 45.641511
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

Example
Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

Example
Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
The datetime() class also takes parameters for time and timezone(hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

Example
Display the name of the month:
"""
import datetime
import time
import pytz  # for zones
#================
print(dir(datetime))  # All attrubites of datetime listed
#['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
x3 = time.strftime("%Y-%b-%d %H:%M:%S")
print(x3)  # 2021-Sep-12 20:07:07
#================
x4 = time.localtime()
curr_clock = time.strftime("%H:%M:%S", x4)
print("curr_clock: " + curr_clock)  # curr_clock: 20:14:43
#==========
IST = pytz.timezone('Asia/Kolkata')
ANY = pytz.timezone('America/New_York')
x5 = datetime.datetime.now(IST)
x6 = datetime.datetime.now(ANY)
print("x5: IST current " + str(x5))  # x5: 2021-09-13 05:50:59.327103+05:30
print("x6: LocalTime EST current " + str(x6))
# x5: IST current 2021-09-13 06:19:01.534322+05:30
# x6: LocalTime EST current 2021-09-12 20:49:01.534322-04:00
#----------Get current time in all time zones
for i in pytz.all_timezones:
    xB = pytz.timezone(i)
    x5A = datetime.datetime.now(xB)
    print("Time in " + i + " zone is : " + str(x5A))
"""
Time in Africa/Abidjan zone is : 2021-09-13 00:31:40.630559+00:00
Time in Africa/Accra zone is : 2021-09-13 00:31:40.632559+00:00
Time in Africa/Addis_Ababa zone is : 2021-09-13 03:31:40.634559+03:00
Time in US/Samoa zone is : 2021-09-12 13:31:41.739364-11:00
Time in UTC zone is : 2021-09-13 00:31:41.739364+00:00
Time in Universal zone is : 2021-09-13 00:31:41.740365+00:00
Time in W-SU zone is : 2021-09-13 03:31:41.741363+03:00
Time in WET zone is : 2021-09-13 01:31:41.743362+01:00
Time in Zulu zone is : 2021-09-13 00:31:41.744362+00:00
etc etc
Time of all time zones are enlisted
"""
"""
for i in pytz.all_timezones:
    print(i)
    x5A = datetime.datetime.now(i)
    print(str(x5A))
"""
#----------
IST = pytz.timezone('Asia/Kolkata')
x5 = datetime.datetime.now(IST)
print("x5: " + str(x5))  # x5: 2021-09-13 05:50:59.327103+05:30
#==========
x = datetime.datetime.now()
print(x)  # 2021-09-12 18:15:07.652066
# ==Summary (important usages of datetime) when now() = 2021-09-12 18:23:36.738933)
print(x.year)  # 2021
print(x.month)  # 9
print(x.day)  # 12
print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print("#============#")
# t = datetime.strptime(x, "%d %B, %Y")
# x1 = datetime.now()
# print("Current date and time: " + str(x1.strftime("%d/%m/%Y %H:%M:%S")))

"""
2021
9
12
18
22
33
"""
today = datetime.date.today()
print(today)  # 2021-09-12
print('ctime:', today.ctime())  # Sun Sep 12 00:00:00 2021
# time.struct_time(tm_year=2021, tm_mon=9, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=255, tm_isdst=-1)
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())  # 738045
print('Year :', today.year)  # 2021
print('Month:', today.month)  # 9
print('Day  :', today.day)  # 12
# print(t)
"""
t = datetime.time(4, 20, 1)

# Let's show the different components
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)
"""
# 04:20:01
# hour  : 4
# minute: 20
# second: 1
# microsecond: 0
# tzinfo: None
"""
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
"""
# Earliest  : 00:00:00
# Latest    : 23:59:59.999999
# Resolution: 0:00:00.000001
"""
l = datetime.date.today()
print(l)
"""
# 2019-11-03
"""
print(l.day)
print(l.month)
"""
# 3
# 11
"""

"""
# 2019-11-03
# ctime: Sun Nov  3 00:00:00 2019
# tuple: time.struct_time(tm_year=2019, tm_mon=11, tm_mday=3, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=307, tm_isdst=-1)
# ordinal: 737366
# Year : 2019
# Month: 11
# Day  : 3
"""
"""
# print(x.H)  # 12
# print(x.M)  # 12
print(x.strftime("%a"))  # % a  :  Weekday, short versionWed
print(x.strftime("%A"))  # % A  :  Weekday, full versionWednesday
print(x.strftime("%w"))  # % w  :  Weekday as a number 0 - 6, 0 is Sunday3
print(x.strftime("%d"))  # % d  :  Day of month 01 - 3131
print(x.strftime("%b"))  # % b  :  Month name, short versionDec
print(x.strftime("%B"))  # % B  :  Month name, full versionDecember
print(x.strftime("%m"))  # % m  :  Month as a number 01 - 1212
print(x.strftime("%y"))  # % y  :  Year, short version, without century18
print(x.strftime("%Y"))  # % Y  :  Year, full version2018
print(x.strftime("%H"))  # % H  :  Hour 00 - 2317
print(x.strftime("%I"))  # % I  :  Hour 00 - 125
print(x.strftime("%p"))  # % p  :  AM / PMPM
print(x.strftime("%M"))  # % M  :  Minute 00 - 5941
print(x.strftime("%S"))  # % S  :  Second 00 - 598
print(x.strftime("%f"))  # % f  :  Microsecond 000000 - 999999548513
print(x.strftime("%z"))  # % z  :  UTC offset + 0100
print(x.strftime("%Z"))  # % Z  :  TimezoneCST
print(x.strftime("%j"))  # % j  :  Day number of year 001 - 366365
# % U  :  Week number of year, Sunday as the first day of week, 00 - 5352
print(x.strftime("%U"))
# % W  :  Week number of year, Monday as the first day of week, 00 - 5352
print(x.strftime("%W"))
# % c  :  Local version of date and timeMon Dec 31 17: 41: 00 2018
print(x.strftime("%c"))
print(x.strftime("%C"))  # % C  :  Century20
print(x.strftime("%x"))  # % x  :  Local version of date43465
print(x.strftime("%X"))  # % X  :  Local version of time0.736805555555556
#% % A % character %"))     #% % A % character %  :
print(x.strftime("%G"))  # %G  :  ISO 8601 year2018
print(x.strftime("%u"))  # % u  :  ISO 8601 weekday(1 - 7)1
print(x.strftime("%V"))  # % V  :  ISO 8601 weeknumber(01 - 53)1
print(x.strftime("%B"))  # %B  :  Month
"""
2021-09-12 18:10:49.209824
2021
9
12
Sun
Sunday
0
12
Sep
September
09
21
2021
18
06
PM
10
49
209824
255
37
36
Sun Sep 12 18:10:49 2021
20
09/12/21
18:10:49
2021
7
36
September
# % c  :  Local version of date and timeMon Dec 31 17: 41: 00 2018
A reference of all the legal format codes:

Directive   Description Example Try it
% a Weekday, short version  Wed
% A Weekday, full version   Wednesday
% w Weekday as a number 0 - 6, 0 is Sunday  3
% d Day of month 01 - 31    31
% b Month name, short version   Dec
% B Month name, full version    December
% m Month as a number 01 - 12   12
% y Year, short version, without century    18
% Y Year, full version  2018
% H Hour 00 - 23    17
% I Hour 00 - 12    05
% p AM / PM PM
% M Minute 00 - 59  41
% S Second 00 - 59  08
% f Microsecond 000000 - 999999 548513
% z UTC offset + 0100
% Z Timezone    CST
% j Day number of year 001 - 366    365
% U Week number of year, Sunday as the first day of week, 00 - 53   52
% W Week number of year, Monday as the first day of week, 00 - 53   52
% c Local version of date and time  Mon Dec 31 17: 41: 00 2018
% C Century 20
% x Local version of date   12 / 31 / 18
% X Local version of time   17: 41: 00
% % A % character %
%G  ISO 8601 year   2018
% u ISO 8601 weekday(1 - 7) 1
% V ISO 8601 weeknumber(01 - 53)    01
"""
#Check elapsed time
strT1 = time.time()
print(strT1)
#1647821859.644773
time.sleep(3)
strT2 = time.time()
print(strT2)
#1647821862.6456172
strH = strT2 - strT1
print(strH)
#3.0008442401885986

#=================
from datetime import *
print(f'Current Date: {datetime.now()}')
print(f'Add 1 day to current date: {datetime.now()+timedelta(days=1)}')
print(f'Subtract 1 day,4 minutes, 4 seconds from current date: Current DT: {datetime.now()}::{datetime.now()+timedelta(days=-1)+timedelta(minutes=-4)+timedelta(seconds=-4)}')
print(f'(Add 1 second to current date: {datetime.now()+timedelta(seconds=1)})')
print(f'(Add 1 minute to current date: {datetime.now()+timedelta(minutes=1)})')
print(x.strftime("%y"))
print(x.strftime("%d"))
print(x.strftime("%m"))
#======================Add days and display in format dmyyyy
intDepfromCurrDt = 10
intDepDt = datetime.now()+timedelta(days=intDepfromCurrDt)
print(intDepDt.strftime("%d%m%Y"))
#======================