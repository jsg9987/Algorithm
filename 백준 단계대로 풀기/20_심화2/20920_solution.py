import sys

inputF = sys.stdin.readline
n, m = map(int, inputF().split())
dic = dict()

for i in range(n):
    word = inputF().rstrip()
    if len(word) >= m:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

li = sorted(dic.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
li2 = []

for i in li:
    li2.append(i[0])

for i in li2:
    print(i)
