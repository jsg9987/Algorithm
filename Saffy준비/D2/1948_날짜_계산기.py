T = int(input())

for tc in range(1, T + 1):
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    month1, day1, month2, day2 = map(int, input().split())
    result += day[month1 - 1] - day1 + 1

    for i in range(month1 + 1, month2):
        result += day[i - 1]

    if month1 != month2:
        result += day2

    print(f"#{tc} {result}")
