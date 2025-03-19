T = int(input())

for tc in range(1, T+1):
    n = int(input())
    answer = ""

    for i in range(n):
        alphabet, cnt = input().split()
        cnt = int(cnt)

        answer += alphabet * cnt

    for k in range(0, len(answer), 10):
        print(*answer[k:k+10], sep="")