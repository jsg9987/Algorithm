# 5/8 22:30 ~ 44
from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    n = list(input())
    n_value = int(''.join(n))
    length = len(n)
    candidates = list(permutations(n, length))

    for candidate in candidates:
        if candidate[0] == '0':
            continue
        if int(''.join(candidate)) % n_value == 0 and int(''.join(candidate)) != n_value:
            print(f"#{tc} possible")
            break
    else:
        print(f"#{tc} impossible")
