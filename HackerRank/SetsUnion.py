# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
_ = input()
setA = set(input().split())
_ = input()
setB = set(input().split())

# join the two sets
unionAB = setA.union(setB)

# print
print(len(unionAB))
