# this challenge is about dictionary

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    aStudentList = student_marks[query_name]
    average = sum(aStudentList) / len(aStudentList)
    formatted_average = format(average, '.2f') # two place after decimal
    print(formatted_average)
