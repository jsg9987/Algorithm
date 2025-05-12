T = int(input())

for tc in range(1, T + 1):
    result = True
    data = input()
    length = len(data)
    if data != ''.join(reversed(data)):
        result = False

    data_front = data[:(length - 1) // 2]
    if data_front != ''.join(reversed(data_front)):
        result = False

    data_rear = data[(length + 1) // 2:]
    if data_rear != ''.join(reversed(data_rear)):
        result = False

    if result:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
