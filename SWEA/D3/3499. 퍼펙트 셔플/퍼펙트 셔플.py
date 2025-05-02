# 5/2 23:10 ~
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cards = input().split()
    mid = n // 2
    first = []
    second = []

    if n % 2 == 0:
        first = cards[0:mid]
        second = cards[mid:]
    elif n % 2 != 0:
        first = cards[0:mid+1]
        second = cards[mid+1:]
    
    print(f"#{tc} ", end="")
    while first:
        print(first.pop(0), end=" ")
        if second:
            print(second.pop(0), end=" ")
    print()