# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# read input
_ = input()
coll = Counter(input().split())
N = int(input())

# read offer
earned = 0
for i in range(0, N):
    size, price = input().split()
    if ((size in coll) and (coll[size]>0)):
        earned += int(price)
        coll[size] -= 1

# print
print(earned)
