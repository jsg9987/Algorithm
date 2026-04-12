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