import sys

isTrue = 1
inputF = sys.stdin.readline

s = list(inputF().rstrip())
for i in range(len(s)):
    if s[i] != s[len(s) -i -1]:
        isTrue = 0
    if i >= len(s)-i-1:
        break
print(isTrue)
