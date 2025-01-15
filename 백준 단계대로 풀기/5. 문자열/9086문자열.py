import sys

inputF = sys.stdin.readline
t = int(inputF().rstrip())
for i in range(t):
    arr = list(inputF().rstrip())
    lastIdx = len(arr)-1
    print(arr[0], end="")
    print(arr[lastIdx])