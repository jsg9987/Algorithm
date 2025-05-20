T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    li = []
    while len(li) < n:
        li += input().split()

    s = ''.join(li)  # 문자열 한 번에 이어붙임
    made = set()

    # 슬라이싱을 통해 부분 문자열로 만들 수 있는 모든 수 저장
    for i in range(len(s)):
        for l in range(1, 6):  # 길이 제한: 작은 수부터 빠르게 찾기 위해 5자리까지만 (조절 가능)
            if i + l <= len(s):
                made.add(int(s[i:i + l]))

    # 가장 작은 만들 수 없는 수 찾기
    result = 0
    while result in made:
        result += 1

    print(f"#{tc} {result}")
