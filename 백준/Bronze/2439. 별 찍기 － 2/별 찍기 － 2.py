import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*i, end="")
    if i<n:
        print()