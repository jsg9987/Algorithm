def solution(p):
    # 1. 빈 문자열인 경우, 빈 문자열을 반환
    if not p:
        return p
    # 문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리
    left = 0
    right = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == ')':
            left += 1
        elif p[i] == '(':
            right += 1

        u += p[i]
        if left == right:
            v += p[i+1:]
            break
    # 문자열 u가 "올바른 괄호 문자열"이라면 v에 대해 재귀호출
    correct = [u[0]]
    for i in range(1,len(u)):
        if correct[-1] == '(' and u[i] == ')':
            correct.pop()
        else:
            correct.append(u[i])

    if ''.join(correct) == "":
        return u + solution(v)
    else:
        empty_str = ""
        empty_str += '('
        empty_str += solution(v)
        empty_str += ')'
        u = u[1:-1]
        new_u = ""
        for i in u:
            if i == '(':
                new_u += ')'
            elif i == ')':
                new_u += '('
        empty_str += new_u
        return empty_str

if __name__ == '__main__':
    p = "()))((()"
    print(solution(p))