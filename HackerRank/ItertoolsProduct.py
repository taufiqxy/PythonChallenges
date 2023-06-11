# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = input().split()
b = input().split()

# convert string's instances to int
a = [int(x) for x in a]
b = [int(x) for x in b]

temp = list(product(a, b))

for tup in temp:
    print(tup, end=' ')
