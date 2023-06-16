# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

# read input
k = int(input())
rooms = sorted([int(x) for x in input().split()], reverse=False)

groupedRoom = groupby(rooms)

captainRoom = 'Not Found!'
for x,y in groupedRoom:
    aGroup = list(y) # using list only can be read once, next use will be empty list
    if len(aGroup) != k:
        captainRoom = aGroup[0]

print(captainRoom)
