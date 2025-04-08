from itertools import product

n, m = map(int, input().split())
li = [i for i in range(1, n + 1)]
candidates = list(product(li, repeat=m))

for candidate in candidates:
    print(*candidate)
