# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

myDict = OrderedDict()
for _ in range(0, int(input())):
    item = input()
    if item in myDict:
        myDict[item] += 1
    else:
        myDict[item] = 1

print(len(myDict))
print(*myDict.values())
