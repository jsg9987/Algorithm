import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n, m = map(int, inputF().rstrip().split())
    dic = {}
    li = []

    for _ in range(n):
        dic[inputF().rstrip()] = 1

    for _ in range(m):
        value = inputF().rstrip()
        if value in dic:
            li.append(value)

    li.sort()
    print(len(li))
    for name in li:
        print(name)
