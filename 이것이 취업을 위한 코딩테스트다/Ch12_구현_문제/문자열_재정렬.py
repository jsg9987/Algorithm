# 알파벳 대문자 문자열을 정의하고 문자열의 원소가 이에 해당하면 alphabet에 append, 아니면 number에 append
import sys

inputF = sys.stdin.readline
alphabet_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = list(inputF().rstrip())
alphabets = []
numbers = []

for i in arr:
    if i in alphabet_str:
        alphabets.append(i)
    else:
        numbers.append(int(i))

alphabets.sort()
print(*alphabets, sum(numbers), sep='')