# 4/19 16:51~17:11
# 1의 묶음과 0의 묶음을 세고 더 작은 걸 뒤집는게 best
# 복기: 0에서 1로 바뀔 때 0의 묶음 개수가 1 증가한다.
#      i와 i+1을 비교하여 묶음 개수를 판단하기에 i+1은 따로 판단해줘야한다.
#      i+1 위치의 숫자가 마지막 묶음이다.
li = list(map(int, input()))
idx = 0
zero = 0
one = 0

for i in range(len(li)-1):
    if li[i] == 1 and li[i+1] == 0:
        one += 1
    if li[i] == 0 and li[i+1] == 1:
        zero += 1

if li[len(li)-1] == 0:
    zero += 1
elif li[len(li)-1] == 1:
    one += 1

print(min(zero, one))