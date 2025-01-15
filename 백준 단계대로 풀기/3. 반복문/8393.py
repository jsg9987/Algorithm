# 문제: n이 주어졌을 때, 1~n까지 합 구하는 프로그램
# 입력: 첫째 줄에 n(1<=n<=10000)
# 출력: 1~n까지 합 출력

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)