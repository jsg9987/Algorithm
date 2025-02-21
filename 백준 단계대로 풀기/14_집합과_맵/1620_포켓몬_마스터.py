import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n, m = map(int, inputF().rstrip().split())
    dic = {}
    dic2 = {}

    for i in range(1, n + 1):
        value = inputF().rstrip()
        dic[value] = i
        dic2[str(i)] = value

    for i in range(m):
        value = inputF().rstrip()
        if value not in dic:
            print(dic2[value])
        else:
            print(dic[value])

    # str.isdigit() 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
    # -, .을 문자로 판단함.(실수, 음수를 판단 못한다.)