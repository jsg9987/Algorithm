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

    '''
    set 사용 시
    s = set()
    for _ in range(n):
        s.add(input())
    for _ in range(m):
        t = input()
        if t in s:
            count += 1
    
    set도 검색 시간 복잡도 O(1)
    '''