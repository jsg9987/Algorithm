import sys
inputF = sys.stdin.readline

n = int(inputF())
scare_scores = list(map(int, inputF().split()))
scare_scores.sort()
group = []
arr_len = 0
result = 0

for x in scare_scores:
    if len(group) == 0:
        arr_len = x
        group.append(x)
    else:
        if len(group) != arr_len:
            if x > arr_len:
                arr_len = x
            group.append(x)

    if len(group) == arr_len:
        group.clear()
        arr_len = 0
        result += 1

print(result)
