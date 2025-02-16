import sys
if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(sys.stdin.readline().rstrip())

    li = list(set(arr))
    li.sort(key= lambda x: (len(x), x))
    for i in li:
        print(i)