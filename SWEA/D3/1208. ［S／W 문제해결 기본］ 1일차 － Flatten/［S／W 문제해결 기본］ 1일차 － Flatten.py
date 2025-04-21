from operator import index

T = 10

for tc in range(1, T+1):
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))

    while dump_cnt != 0:
        max_value = max(boxes)
        max_idx = boxes.index(max_value)
        min_value = min(boxes)
        min_idx = boxes.index(min_value)

        if max_idx == min_idx:
            boxes[max_idx] -= 1
            if max_idx == 0:
                boxes[max_idx+1] +=1
            else:
                boxes[max_idx-1] += 1
        else:
            boxes[max_idx] -= 1
            boxes[min_idx] += 1
        dump_cnt -= 1
    min_diff = max(boxes) - min(boxes)
    print(f"#{tc} {min_diff}")
