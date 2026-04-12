import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())
arr = list(map(int, inputF().rstrip()))
print(sum(arr))
