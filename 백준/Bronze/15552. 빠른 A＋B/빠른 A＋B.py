import sys
# dir(객체) -> 객체의 메소드 확인
t = int(sys.stdin.readline().rstrip())

for i in range(1,t+1):
    a,b = map(int, sys.stdin.readline().rstrip().split()) # split() -> 나눈 다음에 문자열 리스트에 넣음.    
    print(a+b)