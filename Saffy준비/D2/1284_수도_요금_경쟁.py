T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    price_A = p * w
    price_B = 0

    if w <= r:
        price_B = q
    else:
        price_B = q + (w - r) * s

    print(f"#{test_case} {min(price_A, price_B)}")

