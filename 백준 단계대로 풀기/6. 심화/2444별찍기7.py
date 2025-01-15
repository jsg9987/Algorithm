import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())
k = 1
for i in range(2*n-1):
    if k<n:
        print(" "*(n-k), end="")
        print("*"*(2*k-1))
        k+=1
    else:
        print(" "*(k-n), end="")
        print("*"*(4*n-2*k-1))
        k+=1
