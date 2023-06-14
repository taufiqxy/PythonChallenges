# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# read input
k, m = input().split()
k = int(k)
m = int(m)

# get all lines and store into a nested list
allList = []
for i in range(0, k):
    aList = [int(x) for x in input().split()]
    aList = aList[1:] # ignore number of element list, just take the list
    allList.append(aList)

combinations = list(product(*allList))

sMax = 0
for aCombination in combinations:
    S = 0
    
    for aNum in aCombination:
        S += aNum**2
    
    S = S % m
    if S > sMax:
        sMax = S

# print sMax
print(sMax)
