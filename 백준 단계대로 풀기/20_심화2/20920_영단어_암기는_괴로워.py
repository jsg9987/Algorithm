import sys
from collections import Counter

inputF = sys.stdin.readline
n, m = map(int, inputF().split())
words = []

for i in range(n):
    word = inputF().rstrip()
    if len(word) >= m:
        words.append(word)

# 사전 순으로 정렬
words.sort(key= lambda x: x)
# 단어의 길이가 길수록 앞에 배치
words.sort(key= lambda x: len(x), reverse=True)
dic = dict()

for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

li = sorted(dic.items(), key= lambda x: x[1], reverse=True)
li2 = []

for i in li:
    li2.append(i[0])

for word in li2:
    print(word)
