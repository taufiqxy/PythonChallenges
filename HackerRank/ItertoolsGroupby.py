# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby


# read input
s = input()

# groupby
result = groupby(s)

# calculate len of every group and insert into list
myList = []
for key, group in result:
    myList.append((len(list(group)), int(key)))

print(*myList, sep=' ')
