# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input
T = int(input())

for _ in range(0, T):
    _ = input()
    setA = set(int(x) for x in input().split())
    _ = input()
    setB = set(int(x) for x in input().split())
    print(setA.issubset(setB))
