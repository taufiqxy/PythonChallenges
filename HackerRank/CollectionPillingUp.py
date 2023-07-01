# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

# process
d = deque()
for _ in range(int(input())):
    n = int(input())
    d.clear()
    d.extend([int(x) for x in input().split()])
    for i in range(n):
        if d[0] >= d[-1]:
            pop = d.popleft()
        else:
            pop = d.pop()
        
        if len(d) !=0:
            if pop < d[0] or pop < d[-1]:
                print('No')
                break
    if len(d) == 0:
        print('Yes')
