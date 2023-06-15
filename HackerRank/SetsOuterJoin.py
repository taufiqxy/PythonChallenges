# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
_ = input()
setA = set(input().split())
_ = input()
setB = set(input().split())

# symmetric differences A and B
smAB = (setA.difference(setB)).union(setB.difference(setA))

# print
print(len(smAB))
