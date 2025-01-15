# 문제: 바구니를 총 N개 가짐. 각각 1~N번까지 번호 매겨짐. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니 번호 = 공 번호

#   앞으로 M번 공을 바꾸려함. 공을 바꿀 바구니 2개를 선택, 두 바구니의 공을 서로 교환
#   공을 어떻게 바꿀지 주어졌을 때, M번 공을 바꾼 이 후 각 바구니에 어떤 공이 들어있는지 구하는 프로그램 작성

# 입력: 첫째 줄에 N, M 주어짐.
#       둘째 줄부터 M개의 줄에 걸쳐 공을 교환할 방법이 주어짐. 각 방법은 두 정수 i,j로 이루어져 있음.

# 출력: 1~N 바구니에 들어있는 공 번호를 공백으로 구분해 출력

import sys

inputF = sys.stdin.readline

n,m = map(int,inputF().rstrip().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = i+1

for k in range(m):
    i,j = map(int, inputF().rstrip().split())
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp

for i in arr:
    print(i, end=" ")


