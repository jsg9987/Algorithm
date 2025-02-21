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
