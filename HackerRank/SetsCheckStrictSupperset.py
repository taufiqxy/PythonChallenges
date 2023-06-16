# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
setA = set(input().split())
n = int(input())

# check supperset using subset. (note: supperset also can be checked by supperset function)
condition = True
for _ in range(0, n):
    setB = set(input().split())
    if not (setB.issubset(setA) and setA != setB):
        condition = False
        break

print(condition)
