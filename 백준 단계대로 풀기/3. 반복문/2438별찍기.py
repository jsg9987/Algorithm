# 문제: 첫째 줄에는 별 1개, ... N번째 줄에는 별 N개
# 입력: 첫째 줄에 N이 주어짐.
# 출력: 첫째 줄부터 N번째 줄까지 차례대로 별 출력

import sys

n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):     
    print("*"*i)
    
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n):
#     print(" "*(n-i-1), end="")
#     print("*"*(1+2*i), end="")
#     print(" "*(n-i-1))