if __name__ == '__main__':
    x_points = []
    y_points = []

    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        x_points.append(x)
        y_points.append(y)

    x_len = max(x_points) - min(x_points)
    y_len = max(y_points) - min(y_points)

    print(x_len * y_len)