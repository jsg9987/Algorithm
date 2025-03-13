T = int(input())
month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
day = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11": 30,
       "12": 31}

for test_case in range(1, T + 1):
    n = input()
    result = n[:4] + "/" + n[4:6] + "/" + n[6:8]
    ymd = [n[:4], n[4:6], n[6:8]]

    if ymd[1] not in month:
        result = -1
    else:
        if ymd[2] == 0 or int(ymd[2]) > day[ymd[1]]: # int와 str type 잘 파악하기
            result = -1

    print(f"#{test_case} {result}")
