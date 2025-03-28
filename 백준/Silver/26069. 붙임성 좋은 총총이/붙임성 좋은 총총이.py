import sys

inputF = sys.stdin.readline
n = int(inputF())
names = set()
names.add("ChongChong")

for i in range(n):
    name1, name2 = inputF().rstrip().split()
    if name1 in names or name2 in names:
        names.add(name1)
        names.add(name2)

print(len(names))