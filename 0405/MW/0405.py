# 로봇

from collections import deque

M, N = map(int, input().split())
factory = [list(map(int,input().split())) for _ in range(M)]
start_x, start_y, s_dir = map(int, input().split())
end_x, end_y, e_dir = map(int, input().split())
move = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북
visited = [[0]*N for i in range(M)]
ans = 1e7
def bfs(x, y, dir, cnt=0):
    global ans
    if x == end_x-1 and y == end_y-1:
        if dir == e_dir:
            ans = min(ans, cnt)
            return
        else:
            if (dir == 1 and e_dir == 2) or (dir == 2 and e_dir == 1) or (dir == 3 and e_dir == 4) or (dir == 4 and e_dir == 3):
                ans = min(ans, cnt+2)
            else:
                ans = min(ans, cnt+1)
            return

    for i in range(1, 5):
        if (dir == 1 and i == 2) or (dir == 2 and i == 1)or(dir == 3 and i == 4)or(dir == 4 and i == 3):
            plus = 3
            for k in range(1, 4):
                if x + move[i][0]*k < 0 or y+move[i][1]*k < 0 or x + move[i][0] == M or y+move[i][1] == N:
                    break
                if factory[x+move[i][0]*k][y+move[i][1]*k]:
                    break
                if not visited[x+move[i][0]*k][y+move[i][1]*k]:
                    visited[x+move[i][0]*k][y+move[i][1]*k] = 1
                    bfs(x+move[i][0]*k, y+move[i][1]*k, i, cnt+plus)
        elif dir == i:
            plus = 1
            for k in range(1, 4):
                if x + move[i][0]*k < 0 or y+move[i][1]*k < 0 or x + move[i][0] == M or y+move[i][1] == N:
                    break
                if factory[x+move[i][0]*k][y+move[i][1]*k]:
                    break
                if not visited[x+move[i][0]*k][y+move[i][1]*k]:
                    visited[x+move[i][0]*k][y+move[i][1]*k] = 1
                    bfs(x+move[i][0]*k, y+move[i][1]*k, i, cnt+plus)
        else:
            plus = 2
            for k in range(1, 4):
                if x + move[i][0]*k < 0 or y+move[i][1]*k < 0 or x + move[i][0] == M or y+move[i][1] == N:
                    break
                if factory[x+move[i][0]*k][y+move[i][1]*k]:
                    break
                if not visited[x+move[i][0]*k][y+move[i][1]*k]:
                    visited[x+move[i][0]*k][y+move[i][1]*k] = 1
                    bfs(x+move[i][0]*k, y+move[i][1]*k, i, cnt+plus)
bfs(start_x, start_y, s_dir)
print(visited)
print(ans)