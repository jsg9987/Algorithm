'''
문제 2745 진법 변환
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.

'''
import sys


def transformNum(n, b):
    b = int(b)
    resultSum = 0
    strInput = list(n)

    for i in range(len(strInput)):
        if strInput[len(strInput) - i - 1].isdigit():
            resultSum += int(strInput[len(strInput) - i - 1]) * pow(b, i)
        else:
            resultSum += (ord(strInput[len(strInput) - i - 1]) - ord('A') + 10) * pow(b, i)

    return resultSum


def convertBase(n, b):
    # Str 문자열로 알파벳 순서를 적고 그에 맞게 진법 변환
    numDict = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sumResult = 0
    for ri, rc in enumerate(n): # 문자열의 첫번째부터 읽으니까 숫자의 자리수와 반대이다. 거꾸로 처리 필요
        for i, c in enumerate(numDict):
            if rc == c:
                sumResult += i * pow(int(b), len(n) - ri -1)

    return sumResult

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n, b = inputF().rstrip().split() # n: B진법 수 N, b: 진법

    print(convertBase(n, b))

'''
enumerate(list) 
인덱스와 원소로 이루어진 튜플을 만들어준다. -> 인덱스, 원소를 각각 다른 변수에 할당하려면 unpacking 필요
for i, b in enumerate(list):
    print(i, b)
'''
