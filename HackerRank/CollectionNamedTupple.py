# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

# read input
N = int(input())
Student = namedtuple('Student', input().split())
totalGrade = 0
for _ in range(0, N):
    student = Student(*input().split())
    totalGrade += float(student.MARKS)

print(totalGrade/N)
