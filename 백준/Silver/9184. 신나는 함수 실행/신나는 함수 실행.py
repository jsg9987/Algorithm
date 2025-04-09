def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: # 종료 조건
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if d[a][b][c] != 0:
        return d[a][b][c]
    if a < b < c:
        d[a][b][c] =  w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return d[a][b][c]

    d[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return d[a][b][c]


while True:
    a, b, c = map(int, input().split())
    d = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
