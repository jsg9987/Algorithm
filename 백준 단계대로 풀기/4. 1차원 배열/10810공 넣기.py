# 문제: 바구니를 총 N개 가지고 있음. 1~N까지 번호 매겨짐. 1~N번까지 번호가 적혀있는 공을 매우 많이 가지고 있음. 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있음. 앞으로 M번 공을 넣으려고 함. 한 번 공을 넣을 때 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣음. 공을 넣을 바구니는 연속되어 있어야함. 어떻게 넣을지 주어졌을 때, M번 공을 넣은 이후 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램 작성.

# 입력: 첫째 줄에 N과 M이 주어짐.
#       둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법
#       각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 

import sys

inputF = sys.stdin.readline
n,m = map(int, inputF().rstrip().split())
listA = [0 for i in range(n)]
for i in range(m):
    i,j,k = map(int, inputF().rstrip().split())

    for t in range(i-1,j):
        listA[t] = k

for i in listA:
    print(i, end=" ")