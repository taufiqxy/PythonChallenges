# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
_ = input()
setA = set(input().split())
N = int(input())

# run command
for _ in range(0, N):
    command, _ = input().split()
    subSet = set(input().split())
    if command == 'intersection_update':
        setA.intersection_update(subSet)
    elif command == 'update':
        setA.update(subSet)
    elif command == 'symmetric_difference_update':
        setA.symmetric_difference_update(subSet)
    elif command == 'difference_update':
        setA.difference_update(subSet)
    else:
        print('command not found!')

# convert element to int to perform sum operation
setA = [int(x) for x in list(setA)]
        
print(sum(setA))
