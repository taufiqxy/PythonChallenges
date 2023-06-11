# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, n = input().split()

# check if n available
if n == None:
    n = len(s)

# convert n to int
n = int(n)

# permutation
p = list(permutations(s, n))

# join tupple in list
p = [''.join(x) for x in p]

# sort list by lexicographic
p = sorted(p)

# print permutation
for a in p:
    print(a)
