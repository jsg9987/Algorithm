import sys

t = int(sys.stdin.readline().rstrip())

for i in range(1,t+1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")