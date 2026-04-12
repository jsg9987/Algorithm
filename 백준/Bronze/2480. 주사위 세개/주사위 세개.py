# 한 줄의 문자열로 공백 기준으로 데이터 입력받기
a, b, c = map(int, input().split())

reward = 0
equalNum = 0
maxNum = 0

if(a == b == c):
    reward = 10000 + a*1000
elif(a==b or b==c or c==a):
    if(a==b):
        equalNum = a
    elif(b==c):
        equalNum = b
    else:
        equalNum = c
    reward = 1000 + equalNum*100
else:
    if a<b and maxNum<b:
        maxNum = b
    if b<c and maxNum<c:
        maxNum = c
    if c<a and maxNum<a:
        maxNum=a
    reward = maxNum*100
    
print(reward)