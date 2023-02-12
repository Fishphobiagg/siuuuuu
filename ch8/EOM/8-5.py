# 바텀업 

N,M = map(int,input().split())

d = [10001]*(M+1)

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort()

d[0] = 0

for i in range(N):
    for j in range(coins[i], M+1):
        if d[j - coins[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우 
            d[j] = min(d[j], d[j - coins[i]] + 1)

print(d)

print(d[M]) if d[M] != 10001 else print(-1)


        
        
    



    




    

