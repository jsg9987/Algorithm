from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
# 덧셈,뺄셈, 곱셈, 나눗셈 개수
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '//']
operators = []
for k in range(len(op_num)):
    for _ in range(op_num[k]):
        operators.append(op_list[k])

candidates = set(permutations(operators, n-1))

max_value = -int(1e9)
min_value = int(1e9)
for candidate in candidates:
    result = nums[0]
    for i in range(n-1):
        oper = candidate[i]
        if oper == '+':
            result += nums[i+1]
        elif oper == '-':
            result -= nums[i+1]
        elif oper == '*':
            result *= nums[i+1]
        elif oper == '//':
            result = int(result/ nums[i+1])
    if result > max_value:
        max_value = result
    if result < min_value:
        min_value = result

print(max_value)
print(min_value)