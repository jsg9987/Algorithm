import sys

inputF = sys.stdin.readline

t = int(inputF().rstrip())
for i in range(t):
    r,s = inputF().rstrip().split()
    r = int(r)
    s = list(s)
    for i in s:
        i*r
        print(i*r, end="")
    print()


