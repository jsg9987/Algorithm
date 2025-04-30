T = int(input())

for tc in range(1, T+1):
    l,u,x = map(int, input().split()) # L이상 U이하, X분 운동함.
    result = 0
    if x > u:
        print(f"#{tc} -1")
    elif x < l:
        more = l-x
        print(f"#{tc} {more}")
    elif l <= x <= u:
        print(f"#{tc} 0")



