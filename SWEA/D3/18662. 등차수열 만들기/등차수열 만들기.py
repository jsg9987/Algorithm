# 5/10 20:16 ~
import math

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    candidates = []

    for i in range(len(data)):
        if i == 0:
            x = round(abs(2 * data[1] - data[2] - data[0]),1)
            candidates.append(x)
        if i == 1:
            x = round(abs((data[0] + data[2]) / 2 - data[1]),1)
            candidates.append(x)
        if i == 2:
            x = round(abs(2 * data[1] - data[0] - data[2]),1)
            candidates.append(x)
    if min(candidates) == 0:
        print(f"#{tc} 0.0")
    else:    
        print(f"#{tc} {min(candidates)}")
