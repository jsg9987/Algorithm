T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    result_h = (h1 + h2) % 12
    result_m = (m1 + m2) % 60
    result_h += (m1 + m2) // 60

    print(f"#{tc} {result_h} {result_m}")

