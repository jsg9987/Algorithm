# 문제: 영수증에 적힌 구매한 각 물건의 가격과 개수, 구매한 물건의 총 금액을 보고 계산한 총 금액이 영수증 총 금액과 일치하는지 검사해보자.

# 입력: 첫째 줄에 영수증에 적힌 총 금액 X
#       둘째 줄에 영수증에 적힌 구매한 종류의 수 N
#       이후 N개의 줄에는 각 물건의 가격 a, 개수 b가 공백을 사이에 두고 주어짐.

# 출력: 일치 시 Yes, 불일치시 No 출력

x = int(input())
n = int(input())
sumPrice = 0
for i in range(1, n+1):
    a,b = map(int, input().split())
    sumPrice += a*b
if x==sumPrice:
    print("Yes")
else:
    print("No")