# 문제: 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번 째 줄에는 별 N개 찍는 문제(오른쪽 정렬)

# 입력: 첫째 줄에 N
# 출력: 첫째 줄 부터 N번째 까지 차레대로 별 출력


# 테스트 케이스가 아닌 모든 테스트 케이스에 부합하게
# 변수를 모두 임의의 수 n을 기준으로 잡아야함.
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*i, end="")
    if i<n:
        print()
        

# for i in range(1,n+1):
#     for j in range(1):
#         print(" "*(n-i),end="")
#         print("*"*i, end="")
#     if i<n:
#         print()