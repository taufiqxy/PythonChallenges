# Enter your code here. Read input from STDIN. Print output to STDOUT
#input
S = input()

# sorted based lowercase, upper, digit
digitS = sorted([x for x in S if x.isdigit()]) # digit only
sortedS = sorted([x for x in S if x.islower()]) \
          + sorted([x for x in S if x.isupper()]) \
          + sorted([x for x in digitS if int(x) % 2 != 0])\
          + sorted([x for x in digitS if int(x) % 2 == 0])

# print result
print(''.join(sortedS))
