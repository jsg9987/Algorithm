# 5/10 23:42 ~
T = int(input())

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for tc in range(1, T+1):
    data = list(input())
    result = 0

    for i in range(len(data)):
        if i ==  alphabet.index(data[i]):
            result += 1
        else:
            break

    print(f"#{tc} {result}")

