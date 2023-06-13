# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


# read input
n = input()
s = ''.join(input().split())
k = int(input())

# combination
c = list(combinations(s, k))

# count combination contains 'a'
count = 0
for aCom in c:
    if 'a' in aCom:
        count += 1

# print probability combination contains 'a'
print(count/len(c))
