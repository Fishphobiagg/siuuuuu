# https://www.acmicpc.net/problem/1149
# rgb 거리에 집 칠하기
# input으로 집의 수 N 과 RGB 순으로 칠하는 비용 주어짐 


N = int(input())
h = [[0,0,0]]+[list(map(int,input().split())) for _ in range(N)]

# 모든 경우를 다구하기 
d = [[0,0,0] for _ in range(N+1)]

for i in range(1,N+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + h[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + h[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + h[i][2]

print(d)
print(min(d[N]))    







 


