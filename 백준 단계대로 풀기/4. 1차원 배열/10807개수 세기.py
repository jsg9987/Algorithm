# 문제: 총 N개 정수 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램 작성

# 입력: 첫째 줄에 정수 개수 N 주어짐. 
# 둘째 줄에는 정수가 공백으로 구분되어져 있음. 
# 셋째 줄에는 찾으려고 하는 정수 v가 주어짐. 

import sys
# readline을 써야함 (not s)
n = sys.stdin.readline()

Nlist = list(map(int, sys.stdin.readline().rstrip().split()))
# print(Nlist)

v = int(sys.stdin.readline().rstrip())
print(Nlist.count(v))