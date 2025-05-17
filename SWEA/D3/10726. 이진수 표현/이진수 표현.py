T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    binary = format(m, 'b').zfill(n)

    result = "ON"
    for i in range(1,n+1):
        if binary[-i] == '0':
            result = "OFF"
            break

    print(f"#{tc} {result}")