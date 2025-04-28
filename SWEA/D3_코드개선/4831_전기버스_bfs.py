from collections import deque

T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    bus_stops = set(map(int, input().split()))
    queue = deque([(0, 0)])
    visited = [0] * (n+1)
    min_charge = 0

    while queue:
        num, charge = queue.popleft()

        if num + k >= n:
            min_charge = charge
            break

        for move in range(k, 0, -1):
            if num + move in bus_stops:
                if not visited[num+move]:
                    visited[num+move] = 1
                    queue.append((num+move, charge + 1))

    print(f"#{tc} {min_charge}")

