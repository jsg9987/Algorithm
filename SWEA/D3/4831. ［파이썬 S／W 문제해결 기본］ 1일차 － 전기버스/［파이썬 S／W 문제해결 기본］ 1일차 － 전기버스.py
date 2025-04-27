T = int(input())

for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    bus_stops = set(map(int, input().split()))
    current = 0
    charge = 0

    while current + k < n:
        for move in range(k, 0, -1):
            if current + move in bus_stops:
                charge += 1
                current += move
                break
        else:
            charge = 0
            break

    print(f"#{tc} {charge}")