# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
a = input()
setA = set(input().split())
b = input()
setB = set(input().split())

# outer join
outerJoin = setA.difference(setB).union(setB.difference(setA))

# convet it to a list to print ordered
outerJoin = list(outerJoin)

# change every element to int to support numeric ordered
outerJoin = [int(x) for x in outerJoin]

# and order by asc
outerJoin = sorted(outerJoin, reverse=False)

for a in outerJoin:
    print(a)
