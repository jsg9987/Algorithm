# 5/14 16:46 ~
import sys

inputF = sys.stdin.readline
a, b, c = map(int, inputF().split())

def solution(a,b,c):
    if b == 1:
        return a % c

    temp = solution(a, b//2, c) # 전체의 절반 값

    if b % 2 == 0:
        return ((temp % c) * (temp % c)) % c
    else:
        return ((temp % c) * (temp % c) * (a % c)) % c

print(solution(a,b,c))
