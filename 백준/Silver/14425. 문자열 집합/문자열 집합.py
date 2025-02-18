import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    dic = {}
    count = 0

    for _ in range(n):
        dic[sys.stdin.readline().rstrip()] = 1

    for _ in range(m):
        if sys.stdin.readline().rstrip() in dic:
            count += 1

    print(count)