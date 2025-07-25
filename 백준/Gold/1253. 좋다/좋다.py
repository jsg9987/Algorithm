import sys

# 메인 아이디어: 단순 구현한다면 시간복잡도가 O(N^3)으로 40억을 초과한다.
# 따라서 정렬을 한 후에 두 포인터(초기값 0)를 오른쪽으로 옮겨가며 합이 어떤 수와 같은지 비교한다. 최대 O(N^2)
# tail이 어떤 수보다 같거나 클 수 없다!
inputF = sys.stdin.readline

n = int(inputF().rstrip())
nums = list(map(int, inputF().rstrip().split()))
nums.sort() # 투포인터 사용을 위한 정렬
result = 0

# 각 위치에서 "좋다"인지 확인
for i in range(n):
    left, right = 0, n-1
    while left < right:
        # 포인터가 어떤 수에 걸치면 건너뛴다.
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        # 합이 같으면 결과를 ++하고 break
        if nums[left] + nums[right] == nums[i]:
            result += 1
            break

        # 합이 어떤 수보다 작으면 left를 ++
        if nums[left] + nums[right] < nums[i]:
            left += 1
            continue
        # 합이 어떤 수보다 크면 right를 --
        elif nums[left] + nums[right] > nums[i]:
            right -= 1
            continue

print(result)

