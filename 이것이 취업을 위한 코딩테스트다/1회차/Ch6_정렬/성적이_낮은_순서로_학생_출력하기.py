# n = int(input())
# names = [[] for _ in range(101)]
#
# for _ in range(n):
#     name, score = input().split()
#     names[int(score)].append(name)
#
# for name in names:
#     if name:
#         print(*name, sep=" ", end=" ")

n = int(input())
array = []

for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key= lambda x: x[1]) # sorted() 함수는 리스트의 각 요소를 하나씩 key에 전달해서 반환된 값을 기준으로 정렬한다.

for student in array:
    print(student[0], end=' ')