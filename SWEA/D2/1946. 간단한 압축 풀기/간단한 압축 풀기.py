T = int(input())

for tc in range(1, T+1):
    n = int(input())
    answer = ""
    print(f"#{tc}")
    for i in range(n):
        alphabet, cnt = input().split()
        cnt = int(cnt)
        
        while cnt !=0:
            if len(answer) != 10:
                empty_len = 10 - len(answer)
                if empty_len < cnt:
                    answer += empty_len * alphabet
                    cnt -= empty_len
                else:
                    answer += cnt * alphabet
                    cnt = 0
            if len(answer) == 10:
                print(answer)
                answer = ""
            if i == n-1 and cnt == 0:
                print(answer)