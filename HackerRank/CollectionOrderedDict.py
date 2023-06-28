# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

# read input
N = int(input())

# parse
sale = OrderedDict()
for _ in range(0, N):
    x = input().split()
    itemName = ' '.join(x[0:-1])
    price = int(x[-1])
    if itemName in sale:
        sale[itemName] += price
    else:
        sale[itemName] = price

# print
for item in sale:
    print(item, sale[item])
