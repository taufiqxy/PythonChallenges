if __name__ == '__main__':
    # Initialiazation List and Set
    StudentGradeList = []
    ScoreSet = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        StudentGradeList.append([name, score])
        ScoreSet.add(score)
    
    # sort score
    sortedScore = sorted(ScoreSet) # auto convert to list
    SecondLowest = sortedScore[1]
    
    # get second lowest with student name
    SecondLowestName = []
    for aStudentGrade in StudentGradeList:
        if aStudentGrade[1] == SecondLowest:
            SecondLowestName.append(aStudentGrade[0])
    
    # sort name
    SecondLowestName = sorted(SecondLowestName)
    
    for name in SecondLowestName:
        print(name)
