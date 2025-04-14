# 그리디로 풀이
# 두 수 중에서 하나라도 1 이하인 경우, 더하기를 수행하는게 best

data = input()

result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)