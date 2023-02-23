# 효율적인 화폐 구성
'''
1원부터 올라가서 최소 개수를 계속해서 더해주기
'''
N, M = map(int, input().split())
money = [int(input()) for i in range(N)]
d = [0] * (10001)

for i in money:
    d[i] = 1

for i in range(1, M+1):
    for pay in money:
        if d[i] and d[i-pay]:
            d[i] = min(d[i],d[i-pay]+1)
        elif d[i-pay]:
            d[i] = d[i-pay] + 1
if d[M]:
    print(d[M])
else:
    print(-1)