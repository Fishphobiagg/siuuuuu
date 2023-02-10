# 바텀업 

# 한칸씩 채우기 

N = int(input())

cases = [0] * (N+1)

cases[1], cases[2] = 1, 3 # 1+2*2 

for i in range(3, N+1):
    cases[i] = cases[i-1] + cases[i-2]*2


print(cases[N])
print(cases)