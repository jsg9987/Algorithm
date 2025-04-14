n, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=False)
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(k): # 오답: a에서 가장 작은 수가 b에서 가장 큰 수보다 클 수가 있다. 그 경우에는 바꾸면 안된다.
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

