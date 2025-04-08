import sys
def cut(start, n):
    if n == 1:
        return
    for i in range(start + n // 3, start + (n // 3) * 2):
        result[i] = ' '
    cut(start, n // 3)
    cut(start + (n // 3) * 2, n // 3)


while True:
    try:
        n = int(sys.stdin.readline())
        result = ['-'] * (3 ** n)
        cut(0, 3 ** n)
        print(*result, sep="") # print(' '.join(result))
    except:
        break
