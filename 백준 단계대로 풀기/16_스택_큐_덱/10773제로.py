import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    k = int(inputF().rstrip())
    ST = []

    for _ in range(k):
        n = int(inputF().rstrip())

        if n == 0:
            ST.pop(-1)
        else:
            ST.append(n)

    print(sum(ST))