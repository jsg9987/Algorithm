# 4/24 23:00 ~

def pow(n, m):
    if m == 1:
        return n
    return n * pow(n, m-1)
for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    print(f"#{tc} {pow(n,m)}")
