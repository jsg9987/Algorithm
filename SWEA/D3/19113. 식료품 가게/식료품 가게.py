# 5/10 19:10 ~
# 제일 작은 것부터 원래 가격으로 만들고 두개씩 제외하면 항상 동일한 결과가 나온다.
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))
    result = []

    while price:
        sale_price = price.pop(0)
        result.append(sale_price)
        origin_price = sale_price // 3 * 4
        origin_idx = price.index(origin_price)
        price.pop(origin_idx)

    print(f"#{tc} {' '.join(map(str, result))}")