# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
_ = input()
arr = input().split()
setA = set(input().split())
setB = set(input().split())

# compute happiness
happ = 0
for num in arr:
    if num in setA:
        happ += 1
    if num in setB:
        happ -= 1

# print final happiness
print(happ)
