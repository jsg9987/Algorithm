# 해당 클래스에 접근해 메소드 호출 -> "string".upper()
# 대,소문자 확인 .isupper()

import sys

max = 0
result = None
inputF = sys.stdin.readline

arr = list(inputF().rstrip().upper())
alphabet = [0 for i in range(26)]

for i in range(len(arr)):
    alphabet[ord(arr[i])- ord('A')] +=1

for i in alphabet:
    if max<i:
        max = i
        result = alphabet.index(i) + 65
    elif max == i:
        result = ord("?")

print(chr(result))
