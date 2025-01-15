# 문제: 9개의 서로 다른 자연수 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램 작성

# 입력: 첫째 줄부터 9번째 줄까지 한 줄에 하나의 자연수가 주어짐. 주어지는 자연수 100보다 작음

# 출력: 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

import sys

# inputF = sys.stdin.readline
# listA = []
# for i in range(9):
#     listA.append(int(inputF().rstrip()))
# maxNum = listA[0]
# maxIndex = 0
# for i in listA:
#     if i>maxNum:
#         maxNum = i
#         maxIndex = listA.index(maxNum) +1
# print(maxNum)
# print(maxIndex, end="")

inputF = sys.stdin.readline
maxNum = 0
listA = []
index = 0

for i in range(9):
    a = int(inputF().rstrip())
    listA.append(a)
    if a > maxNum:
        maxNum = a
    index = listA.index(maxNum) + 1

print(maxNum)
print(index)

