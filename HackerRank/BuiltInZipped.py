# Enter your code here. Read input from STDIN. Print output to STDOUT
# read input
i, line = [int(x) for x in input().split()]

# concat input to a list
aList = []
for _ in range(line):
    aList.append([float(x) for x in input().split()])
    
zipped = list(zip(*aList))
for item in zipped:
    print(sum(item)/len(item))
