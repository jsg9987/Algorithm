# 5/12 22:57 ~
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    palindromes = [input() for _ in range(n)]
    non_palin = []
    palin = []

    for x in palindromes:
        if x != x[::-1] and x[::-1] in palindromes:
            non_palin.append(x)
            non_palin.append(palindromes.pop(palindromes.index(x[::-1])))
        if x == x[::-1]:
            palin.append(x)
    result = 0

    if palin:
        result = m
    print(f"#{tc} {len(non_palin) * m + result}")
