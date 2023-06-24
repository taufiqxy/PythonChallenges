# Enter your code here. Read input from STDIN. Print output to STDOUT
# read input
a = float(input())
b = float(input())
m = float(input())

# print pow
print(int(pow(a, b)))

# print pow modulo
a, b, m = int(a), int(b), int(m)
print(pow(a, b, m))
