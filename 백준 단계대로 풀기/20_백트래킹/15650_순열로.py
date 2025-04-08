from itertools import permutations

n, m = map(int, input().split())
li = [i for i in range(1, n + 1)]

candidates = list(permutations(li, m))
for candidate in candidates:
    check = True
    for i in range(len(candidate)-1):
        if candidate[i] > candidate[i+1]:
            check = False
    if check:
        print(*candidate)