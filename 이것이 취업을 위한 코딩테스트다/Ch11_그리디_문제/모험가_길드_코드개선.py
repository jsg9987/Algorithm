import sys
inputF = sys.stdin.readline

n = int(inputF())
scare_scores = list(map(int, inputF().split()))
scare_scores.sort()
group = []
result = 0

for x in scare_scores:
    group.append(x)

    if len(group) >= x:
        result += 1
        group.clear()

print(result)

