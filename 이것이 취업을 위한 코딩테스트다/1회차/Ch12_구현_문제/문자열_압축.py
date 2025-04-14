def solution(s):
    best = s
    for step in range(1, len(s)):
        cnt = 1
        first = s[:step]
        answer = ""
        for i in range(step,len(s),step):
            if first == s[i:i+step]:
                cnt += 1
            else:
                if cnt == 1:
                    answer += first
                else:
                    answer += str(cnt) + first
                first = s[i:i+step]
                cnt = 1
        if cnt > 1:
            answer += str(cnt) + first
        else:
            answer += first

        if len(answer) < len(best):
            best = answer

    return len(best)


if __name__ == '__main__':
    s = "a"
    solution(s)
