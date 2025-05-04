# 아무리 봐도 오류가 없는 것 같으면 문제 중에서 한글을 잘못 이해하지 않았나 확인하자.

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    length = len(nums)
    sums = []

    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j + 1, length):
                sums.append(nums[i] + nums[j] + nums[k])
    sums = list(set(sums))
    sums.sort(reverse=True)
    print(f"#{tc} {sums[4]}")