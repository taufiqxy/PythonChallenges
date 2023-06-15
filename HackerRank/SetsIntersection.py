# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
_ = input()
setA = set(input().split())
_ = input()
setB = set(input().split())

# itersections the two sets
intersectAB = setA.intersection(setB)

# print
print(len(intersectAB))
