# 조건: 특정 인덱스 번호의 원소를 K번 연속해 사용이 불가능하다.
# 특징: 같은 수인 다른 인덱스를 사용하는 건 상관 없다!

# 아이디어: 큰 순서대로 리스트를 정렬하고 맨 앞 원소를 K번 사용하고, 그 다음 원소를 한 번 사용하고, 다시 맨 앞의 원소를 K번 사용하도록 반복하자.
# 시간 복잡도: O(M)

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
result = 0

for i in range(1,m+1):
    if i % k == 0:
        result += nums[1]
    else:
        result += nums[0]

print(result)