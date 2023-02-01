#4 1이 될 때까지
n, k = map(int, input().split())
cnt = 0
while True: 
    #세 가지 경우로 나누어 조건문
    if n == 1: 
        break
    elif n % k != 0:
        cnt += 1
        n -= 1

    elif n % k == 0:
        cnt += 1
        n = n / k
print(cnt)