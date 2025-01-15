# 문제: 두 정수 a,b 입력 후 a+b 출력하는 프로그램 작성
# 입력: 첫째 줄에 테스트 케이스 개수 T
#       각 줄에 A,B 주어짐
# 출력: 각 테스트 케이스마다 "Case #x:" 출력한 다음 A+B 출력, 테스트 케이스 번호는 1부터 시작

import sys

t = int(sys.stdin.readline().rstrip())
# 오류! range(t)라고 하면 0부터 시작하기때문에 case번호 1부터 시작하지 않음.
for i in range(1,t+1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a+b}")
