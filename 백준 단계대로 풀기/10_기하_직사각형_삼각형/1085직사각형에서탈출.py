if __name__ == '__main__':
    x, y, w, h = map(int, input().split())
    x_min = min(x - 0, w - x)
    y_min = min(y - 0, h - y)
    print(min(x_min, y_min))
