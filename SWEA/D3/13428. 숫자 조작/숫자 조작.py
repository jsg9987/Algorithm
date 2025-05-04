# 5/4 16:55 ~ 17:13
# 조건: 단, 바꾼 결과 M의 맨 앞이 '0'이면 안 된다.
from copy import deepcopy

T = int(input())

for tc in range(1, T+1):
    num = input()
    length = len(num)
    max_result = int(num)
    min_result = int(num)
    num = list(num)

    for i in range(length-1):
        for j in range(i+1, length):
            temp_num = deepcopy(num)
            if i == 0 and temp_num[j] == '0':
                continue
            temp_num[i], temp_num[j] = temp_num[j], temp_num[i]
            temp_value = int(''.join(temp_num))
            max_result = max(max_result, temp_value)
            min_result = min(min_result, temp_value)

    print(f"#{tc} {min_result} {max_result}")

