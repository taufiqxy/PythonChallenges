# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
_ = input()
setA = set(input().split())
_ = input()
setB = set(input().split())

# differences A and B
differenceAB = setA.difference(setB)

# print
print(len(differenceAB))
