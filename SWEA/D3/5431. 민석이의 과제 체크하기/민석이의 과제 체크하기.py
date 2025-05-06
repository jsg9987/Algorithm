# 5/6 22:51 ~
T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    submitted = set(map(int, input().split()))
    not_submitted = []

    for i in range(1,n+1):
        if i not in submitted:
            not_submitted.append(i)

    print(f"#{tc} {' '.join(map(str, not_submitted))}")