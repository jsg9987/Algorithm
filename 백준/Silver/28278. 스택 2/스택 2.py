import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    ST = []

    for _ in range(n):
        li = inputF().split()
        if li[0] == '1':
            ST.append(int(li[-1]))
        elif li[0] == '2':
            if ST:
                print(ST.pop(-1))
            else:
                print(-1)
        elif li[0] == '3':
            print(len(ST))
        elif li[0] == '4':
            if ST:
                print(0)
            else:
                print(1)
        elif li[0] == '5':
            if ST:
                print(ST[-1])
            else:
                print(-1)


