import sys

inputF = sys.stdin.readline
gradeSum = 0.0
scoreSum = 0.0
checkGrade = True

for i in range(20):
    arr = list(inputF().rstrip().split())
    if arr[2] == "A+":
        grade = 4.5
    elif arr[2] == "A0":
        grade = 4.0
    elif arr[2] == "B+":
        grade = 3.5
    elif arr[2] == "B0":
        grade = 3.0
    elif arr[2] == "C+":
        grade = 2.5
    elif arr[2] == "C0":
        grade = 2.0
    elif arr[2] == "D+":
        grade = 1.5
    elif arr[2] == "D0":
        grade = 1.0
    elif arr[2] == "F":
        grade = 0.0
    elif arr[2] == "P":
        grade = 0.0
        checkGrade = False
    
    if checkGrade:
        gradeSum += float(arr[1])
    scoreSum += float(arr[1])*grade

print(scoreSum/gradeSum)