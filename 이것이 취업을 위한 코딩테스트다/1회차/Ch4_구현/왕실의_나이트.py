x_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
coordinate = list(input())
x = x_dic[coordinate[0]]
y = int(coordinate[1])
cnt = 0
# 문제점: 너무 반복되는 길고 단순한 코드 -> 리스트, 튜플로 짧게
if x + 2 <= 8 and y + 1 <= 8:
    cnt += 1
if x + 2 <= 8 and y - 1 >= 1:
    cnt += 1
if x - 2 >= 1 and y + 1 <= 8:
    cnt += 1
if x - 2 >= 1 and y - 1 >= 1:
    cnt += 1
if x + 1 <= 8 and y + 2 <= 8:
    cnt += 1
if x + 1 <= 8 and y - 2 >= 1:
    cnt += 1
if x - 1 >= 1 and y + 2 <= 8:
    cnt += 1
if x - 1 >= 1 and y - 2 >= 1:
    cnt += 1

print(cnt)
