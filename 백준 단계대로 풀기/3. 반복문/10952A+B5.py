# 문제: 두 정수 A,B 입력받아 A+B 출력 프로그램 작성
# 입력: 여러 개의 테스트 케이스로 이루어짐
#       각 tc는 한 줄로, A,B / 입력 마지막에 0 두 개가 들어옴

# 출력: 각 tc마다 A+B

import sys

while 1:
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if a==b==0:
        break
    print(a+b)