# 로봇
'''
깊은 복사와 얕은 복사...
3차원 배열...
'''
from collections import deque

M, N = map(int, input().split())
factory = [list(map(int,input().split())) for _ in range(M)]
start_x, start_y, s_dir = map(int, input().split())
end_x, end_y, e_dir = map(int, input().split())
move = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북
visited = [[[0 for i in range(5)] for j in range(N)] for k in range(M)]

Q = deque([(start_x-1, start_y-1, s_dir, 0)])
visited[start_x-1][start_y-1][s_dir] = 1

while Q:
    x, y, k, cnt = Q.popleft()
    if (x, y, k) == (end_x-1, end_y-1, e_dir):
        print(cnt)
        break
    for i in range(1, 4):
        nx = x + move[k][0]*i
        ny = y + move[k][1]*i
        if nx < 0 or ny < 0 or nx == M or ny == N:
            break
        if factory[nx][ny]:
            break
        if not visited[nx][ny][k]:
            visited[nx][ny][k] = 1
            Q.append((nx, ny, k, cnt+1))
    for i in range(1, 5):
        if i == k:
            continue
        if (i == 1 and k == 2) or (i == 2 and k == 1) or (i == 3 and k == 4) or (i == 4 and k == 3):
            if not visited[x][y][i]:
                visited[x][y][i] = 1
                Q.append((x, y, i, cnt+2))
        else:
            if not visited[x][y][i]:
                visited[x][y][i] = 1
                Q.append((x, y, i, cnt+1))
