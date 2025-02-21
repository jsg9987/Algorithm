import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    a, b = map(int, inputF().rstrip().split())
    s = set()
    s2 = set()
    arr = list(map(int, inputF().rstrip().split()))
    arr2 = list(map(int, inputF().rstrip().split()))

    for num in arr:
        s.add(num)

    for num in arr2:
        s2.add(num)

    s3 = s & s2
    s4 = s - s2

    for num in s3:
        s4.remove(num)

    li = list(s4)
    print(len(li))

    '''
    n, m = map(int, input().split())
    a = set(map(int, input().split())
    b = set(map(int, input().split())
    print(len(a-b) + len(b-a))
    '''


