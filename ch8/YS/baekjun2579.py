# 바텀업 방식
n = int(input())
lst = [0] + [int(input()) for _ in range(n)] + [0] # 계단을 리스트에 입력
d = [0]*(n+2)  # dp 테이블 초기화
d[1], d[2] = lst[1], lst[1]+ lst[2]
for i in range(3, n+1):
    d[i] = max(d[i-3] + lst[i-1] + lst[i], d[i-2]+ lst[i]) 
print(d[n])