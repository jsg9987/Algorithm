import sys
# readline을 써야함 (not s)
n = sys.stdin.readline()

Nlist = list(map(int, sys.stdin.readline().rstrip().split()))
# print(Nlist)

v = int(sys.stdin.readline().rstrip())
print(Nlist.count(v))