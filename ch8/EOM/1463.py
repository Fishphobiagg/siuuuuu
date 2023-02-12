# https://www.acmicpc.net/problem/1463
# 1로 만들기
# 1. if x % 3 == 0 : X / 3
# 2. if x % 2 == 0 : x / 2
# 3. x - 1
# x가 주어졌을 때 위의 3가지 연산을 적절히 사용하여 1을 만들어야함
# 연산을 사용하는 횟수의 최솟 값은? 
# 바텀업 

X = int(input())

d = [100001] * (X + 1) # 결과 저장용  
d[0] , d[1] = 0, 0
for i in range(2, X+1):

    # - 1
    d[i] = d[i-1] + 1
    # / 3
    if i % 3 == 0 : # 3으로 나누어 떨어지면 
        d[i] = min( d[i],d[int(i/3)] + 1)

    if i % 2 == 0 : # 2으로 나누어 떨어지면 
        d[i] = min( d[i],d[int(i/2)] + 1)

print(d[X])




