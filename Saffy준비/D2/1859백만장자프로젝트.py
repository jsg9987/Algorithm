T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    max_price = 0
    cnt = 0
    buy_price = 0
    sel_price = 0

    li = list(map(int, input().split()))

    for price in li[::-1]:
        if price > max_price:
            max_price = price
        else: # max_price가 갱신 안된 날 -> max_price - price값을 sel_price에 더해주는 날
            sel_price += max_price - price

    print(f"#{test_case} {sel_price}")
