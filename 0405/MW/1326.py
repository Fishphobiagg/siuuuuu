# 팔딱팔딱

N = int(input())
bridge = [0]+list(map(int, input().split()))
a, b = map(int,input().split())

dp = [10000]*10001
dp[a] = 0

for i in range(a, b+1):
    k = bridge[i]
    while k <= N:
        dp[i+k] = min(dp[i] + 1, dp[i+bridge[i]])

        k += bridge[i]
print(dp[b-1])