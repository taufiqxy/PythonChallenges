# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

# read input
month, date, year = [int(x) for x in input().split()]

# get day index
day = calendar.weekday(year, month, date)

# list of the days
dayName = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

# print day's name
print(dayName[day])
