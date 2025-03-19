T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    locations = list(map(int, input().split()))

    for i in range(n):
        if locations[i] < 0:
            locations[i] = -locations[i]

    best = min(locations)
    cnt += locations.count(best) + locations.count(-best)

    print(f"#{tc} {best} {cnt}")
