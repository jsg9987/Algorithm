import sys

t = int(sys.stdin.readline().rstrip())
# 오류! range(t)라고 하면 0부터 시작하기때문에 case번호 1부터 시작하지 않음.
for i in range(1,t+1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a+b}")