# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input().split(' ') # split string into list
height = int(a[0])
width = int(a[1])

sub1 = '.|.'
sub2 = '-'

# note: Un = a + (n-1)b
# Un = 1 + (i-1)2, for i start with 1
# Un = 1 + (i)2, for i start with 0

for i in range(0, int(height/2)):
    print((sub1*(1+(2*i))).center(width, sub2))

print(('WELCOME').center(width, sub2))

for i in range(0, int(height/2)):
    print((sub1*(1+(2*((int(height/2)-1)-i)))).center(width, sub2))
