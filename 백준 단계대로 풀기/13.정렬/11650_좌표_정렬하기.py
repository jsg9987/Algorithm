if __name__ == '__main__':
    n = int(input())
    x_points = []
    y_points = []

    for _ in range(n):
        x, y = map(int, input().split())
        x_points.append(x)
        y_points.append(y)

    # 10000000000 (100억) 시간초과
    for _ in range(n):
        for i in range(n-1):
            if x_points[i] == x_points[i+1]:
                if y_points[i] > y_points[i+1]:
                    temp = x_points[i]
                    x_points[i] = x_points[i+1]
                    x_points[i+1] = temp

                    y_temp = y_points[i]
                    y_points[i] = y_points[i+1]
                    y_points[i+1] = y_temp
                    # x_points[i], x_points[i+1] = x_points[i+1], x_points[i]
            elif x_points[i] > x_points[i+1]:
                temp = x_points[i]
                x_points[i] = x_points[i + 1]
                x_points[i + 1] = temp

                y_temp = y_points[i]
                y_points[i] = y_points[i + 1]
                y_points[i + 1] = y_temp

    for i in range(len(x_points)):
        print(x_points[i], y_points[i])
