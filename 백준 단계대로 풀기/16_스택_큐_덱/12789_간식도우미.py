if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    ST = []
    cnt = 1

# for문 안에서 스택 모두를 처리 가능하도록 하는게 좋다.
# ST이 비었을 때 pop하면 IndexError가 발생 가능하다. ST[-1]을 체크할 때는 항상 Stack이 비어있지 않은지도 체크해야한다.
    for num in nums:
        ST.append(num)
        while ST and ST[-1] == cnt:
            ST.pop(-1)
            cnt += 1

    if not ST:
        print("Nice")
    else:
        print("Sad")
