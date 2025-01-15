# 문제: N개의 정수가 주어짐. 최대, 최소 구하는 프로그램 작성

# 입력: 첫째 줄에 정수의 개수 N
#       둘째 줄에 N개의 정수를 공백으로 구분해 주어짐.

# 출력: 첫째 줄에 주어진 정수 N개의 최소, 최댓값을 공백으로 구분해 출력

import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())

listA = list(map(int, inputF().rstrip().split()))
min = listA[0]
max = listA[0]
for i in listA:
    if i<min:
        min = i
    if i>max:
        max = i
print(min,max)