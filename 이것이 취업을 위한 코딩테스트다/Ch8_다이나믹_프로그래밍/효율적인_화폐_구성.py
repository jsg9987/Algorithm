import sys

n, m = map(int, input().split())
inputF = sys.stdin.readline
coin = []
for _ in range(n):
    coin.append(int(inputF().rstrip()))

d = [10001] * 10001
# 0원은 하나도 안썼을 때 만들 수 있다.
d[0] = 0
for i in coin:
    d[i] = 1

for i in range(min(coin), len(d)):
    for j in coin:
        if i - j > 0:
            d[i] = min(d[i], d[i - j] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
