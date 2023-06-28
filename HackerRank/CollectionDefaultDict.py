# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# read input
n, m = [int(x) for x in input().split()]

# create defaultdict
d = defaultdict(list)
for _ in range(0, n):
    d['A'].append(input())

for _ in range(0, m):
    d['B'].append(input())

# print
for item in d['B']:
    condition = True
    for i in range (0, len(d['A'])):
        if item == d['A'][i]:
            print(i+1, end=' ')
            condition = False
    if condition:
        print(-1, end='')
    print()
