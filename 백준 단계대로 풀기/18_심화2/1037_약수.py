import sys
inputF = sys.stdin.readline

cnt = int(inputF())

li = list(map(int, inputF().split()))
li.sort()
n = li[0] * li[-1]

print(n)
