
if __name__ == '__main__':
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    fourth_x = 0
    fourth_y = 0

    if x1 == x2:
        fourth_x = x3
    else:
        if x1 == x3:
            fourth_x = x2
        else:
            fourth_x = x1

    if y1 == y2:
        fourth_y = y3
    else:
        if y1 == y3:
            fourth_y = y2
        else:
            fourth_y = y1

    print(fourth_x, fourth_y)
