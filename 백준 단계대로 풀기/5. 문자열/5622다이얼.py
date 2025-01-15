import sys
inputF = sys.stdin.readline

arr = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
sumNum = 0
s = list(inputF().rstrip())
for idx, value in enumerate(s):
    s[idx] = value
    sumNum+= arr[ord(s[idx])-ord('A')]+1

print(sumNum)
