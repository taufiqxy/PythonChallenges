# Enter your code here. Read input from STDIN. Print output to STDOUT
# input
_ = input()
aList = input().split()

# check integer and palindromic integer
condition = False
if all([int(x) >= 0 for x in aList]):
    if any([x == x[::-1] for x in aList]):
        condition = True

print(condition)
