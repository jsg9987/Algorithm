# 5/7 22:14 ~
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    A = []
    B = []
    result = 0

    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] < A[j]:
                if B[i] > B[j]:
                    result += 1

            if A[i] > A[j]:
                if B[i] < B[j]:
                    result += 1

    print(f"#{tc} {result}")