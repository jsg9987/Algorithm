# 4/23 21:02 ~ 22:08
# 올바른 암호코드: (홀수 자리의 합 *3) + (짝수 자리 합)이 10의 배수

T = int(input())
dic = dict()
dic["0001101"] = 0
dic["0011001"] = 1
dic["0010011"] = 2
dic["0111101"] = 3
dic["0100011"] = 4
dic["0110001"] = 5
dic["0101111"] = 6
dic["0111011"] = 7
dic["0110111"] = 8
dic["0001011"] = 9

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    binary_code = [input() for _ in range(n)]
    result = 0
    for row in binary_code:
        if '1' not in row:
            continue

        last_idx = row.rfind('1')
        start_idx = last_idx - 55

        bits = [row[i:i+7] for i in range(start_idx, last_idx + 1, 7)]

        if len(bits) != 8:
            continue

        digits = [dic[bit] for bit in bits]

        odd_sum = sum(digits[i] for i in range(0,8,2))
        even_sum = sum(digits[i] for i in range(1,8,2))
        total = odd_sum * 3 + even_sum

        if total % 10 == 0:
            result = sum(digits)
            break
    print(f"#{tc} {result}")