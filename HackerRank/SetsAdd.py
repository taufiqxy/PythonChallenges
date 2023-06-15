# Enter your code here. Read input from STDIN. Print output to STDOUT

countrySet = set()
for _ in range (0, int(input())):
    countrySet.add(input())
    
print(len(countrySet))
