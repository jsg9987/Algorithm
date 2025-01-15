# 한 줄의 문자열로 공백 기준으로 데이터 입력받기

# max(a,b,c): 제일 큰 수 찾음
# map(): 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장 함수
# map(func, iter)
# lambda 함수 -> lambda x: x*2

# split(): 괄호 안의 조건을 기준으로 나눔
a, b, c = map(int, input().split())

reward = 0
equalNum = 0
maxNum = 0

if a == b == c:
    reward = 10000 + a*1000
elif a==b or b==c or c==a:
    if(a==b):
        equalNum = a
    elif(b==c):
        equalNum = b
    else:
        equalNum = c
    reward = 1000 + equalNum*100
else:
    # 세 숫자 중 가장 큰 수 구하기 -> max(a,b,c)
    if a<b and maxNum<b:
        maxNum = b
    if b<c and maxNum<c:
        maxNum = c
    if c<a and maxNum<a:
        maxNum=a
    reward = maxNum*100
    
print(reward)