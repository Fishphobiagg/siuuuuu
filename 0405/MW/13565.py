# 칵 투
from collections import deque
M, N = map(int, input().split())

move = [(0,1),(1,0),(-1,0),(0,-1)]
fiber = [list(map(int, input())) for i in range(M)]
visited = [[0]*N for _ in range(M)]

Q = deque([])
for i in range(N):
    if not fiber[0][i]:
        visited[0][i] = 1
        Q.append((0,i))
while Q:
    x, y = Q.popleft()
    if x == M-1:
        print('YES')
        exit()
    for i in range(4):
        nx, ny = x+move[i][0], y+move[i][1]
        if nx < 0 or ny < 0 or nx == M or ny == N:
            continue
        if fiber[nx][ny]:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            Q.append((nx, ny))

print("NO")