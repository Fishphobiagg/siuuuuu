# https://www.acmicpc.net/problem/2579
# 계단 오르기 
# # 각 계단을 밟아서 꼭대기까지 올라갈 때 
# 계단의 점수를 확득할 수 있음
# 1. 연속 3개의 계단 밟기 금기 
# 2. 한번에 2칸씩 오르기 가능 
# 꼭대기에 올랐을 때 점수의 최댓값은?'

N = int(input()) # 계단 개수 
stairs = [0] 
for _ in range(N):
    stairs.append(int(input())) 

d = [0] * (N + 1)


# 경우 2가지 (연속 2번 더하기 / 한칸띄고 더하기)
for i in range(1, N+1): 
    if i <= 2:
        d[i] = d[i-1] + stairs[i]
    else:
        d[i] = max(d[i-3] + stairs[i-1] + stairs[i], d[i-2] + stairs[i])

print(d[N])