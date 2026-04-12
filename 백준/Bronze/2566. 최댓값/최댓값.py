# 1. 입력 및 변수 초기화
# - 9줄 동안 9개씩 수가 주어짐(0 <= x <100)
import sys

inputF = sys.stdin.readline

global_max = 0
row_index = 0
col_index = 0
arr = []

for i in range(9):
    arr.append(list(map(int, inputF().rstrip().split())))

# index는 0부터 시작한다!! 주의하자.. i+1, j+1 해줘야함.
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if global_max <= arr[i][j]:
            global_max = arr[i][j]
            row_index = i+1
            col_index = j+1
print(global_max)
print(row_index, end=" ")
print(col_index)