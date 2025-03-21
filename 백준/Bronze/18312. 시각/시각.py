# n, k = map(int, input().split())
# hour = 0
# minute = 0
# second = 0
# cnt = 0
# # 오류: 23시 59분 59초가 포함이 안되어있기 때문에 잘못 작성된 코드다.
# while hour != n or minute != 59 or second != 59:
#     if str(k) in str(hour) or str(k) in str(minute) or str(k) in str(second):
#         cnt += 1
#
#     second += 1
#     if second >= 60:
#         second = 0
#         minute += 1
#     if minute >= 60:
#         minute = 0
#         hour += 1
#
# print(cnt)
n, k = map(int, input().split())

cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if len(str(h)) == 1:
                h = '0' + str(h)
            if len(str(m)) == 1:
                m = '0' + str(m)
            if len(str(s)) == 1:
                s = '0' + str(s)
            if str(k) in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)
