# 두 정수 A,B -> A+B 출력 프로그램
# 입력: 첫째 줄에 테스트 케이스 개수 T
#각 테스트 케이스는 한 줄로 이루어짐, 각 줄에 A,B 주어짐

# 출력: 케이스마다 A+B 출력

t = int(input()) # 기본적으로 무조건 str type
# print(type(t))

for i in range(1,t+1):
    a,b = map(int, input().split())
    print(a+b)