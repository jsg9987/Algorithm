import sys

if __name__ == '__main__':
    n = int(input())
    dic = {}
    inputF = sys.stdin.readline
    for _ in range(n):
        name, enter = inputF().rstrip().split()
        if enter == "enter":
            dic[name] = 1
        if enter == "leave":
            del dic[name]

    result = sorted(list(dic.keys()), reverse=True)
    for name in result:
        print(name)