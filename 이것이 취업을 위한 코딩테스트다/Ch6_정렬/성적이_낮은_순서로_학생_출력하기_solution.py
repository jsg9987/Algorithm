n = int(input())
arr = []

for _ in range(n):
    name, score = input().split()
    arr.append((name, score))

arr.sort(key=lambda student: student[1]) # score를 기준으로

for student in arr:
    print(student[0], end=' ')