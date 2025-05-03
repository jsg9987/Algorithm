# 5/3 16:47 ~ 17: 34

T = int(input())

points = [(0,0)]
first_sum = 2
cnt = 1

while first_sum != 801:
    i = first_sum - 1
    j = 1
    while i != 0:
        if i <= 400 and j <= 400:
            points.append((i, j))
            cnt += 1
        i -= 1
        j += 1

    first_sum += 1
for tc in range(1, T+1):

    p, q = map(int, input().split())

    p_point = points[p]
    q_point = points[q]
    x = p_point[0] + q_point[0]
    y = p_point[1] + q_point[1]
    result = points.index((x,y))
    print(f"#{tc} {result}")







