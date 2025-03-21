# 반복되는 수열의 횟수를 안다면 반복문을 돌리지 않고도 간단한 수학식을 사용하여 풀이가 가능하다.

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

result = 0
first = nums[0]
second = nums[1]

# 수열은 (k+1)번 반복된다. 그리고 마지막에 수열 중 나머지 일부 숫자가 나올 수 있다.
# 가장 큰 수의 등장 횟수, 두 번째 큰 수의 등장 횟수를 구한다면 바로 계산 가능

count = m // (k + 1) * k
count += m % (k + 1)

result += count * first
result += (m - count) * second

print(result)
