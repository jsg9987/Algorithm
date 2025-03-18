p, k = map(int, input().split())
cnt = 1

while True:
    if p == k:
        print(cnt)
        break
    else:
        cnt += 1
        k += 1
