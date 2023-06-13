# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

# read input
s, k = input().split()

# combination with replacement
c = list(combinations_with_replacement(sorted(s), int(k)))

# join tuple in list
c = [''.join(x) for x in c]

# print result
print(*c, sep='\n')
