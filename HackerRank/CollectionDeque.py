# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

# operation
d = deque()
for _ in range(0, int(input())):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    else:
        print('command not found!')

# print deque
print(*d, sep=' ')
