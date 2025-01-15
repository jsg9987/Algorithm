# 문제: 두 정수 a,b 입력받은 다음 A+B 출력
# 입력: 첫째 줄에 테스트 케이스 수 T
#       각 테스트 케이스 한 줄로 이루어져 있고, A,B 주어짐(0<a,b<10)
# 출력: 각 테스트 케이스마다 "Case #x: A + B = C"형식으로 출력, x는 1부터 시작 

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(1,t+1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")