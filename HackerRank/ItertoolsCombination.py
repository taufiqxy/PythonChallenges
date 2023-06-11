# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, n = input().split()

n = int(n)

for i in range(1, n+1):
    c = list(combinations(sorted(s), i))
    c = [''.join(x) for x in c]
    print(*c, sep='\n')
