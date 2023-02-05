# 미로 탈출 
# 가까운 곳부터 탐색 가능한 bfs가 좋대 

# 괴물이 있는 부분인 0 은 피해서 미로를 탈출 
# 미로의 출구는 n,m
# 시작위치는 1,1

from collections import deque




def bfs(x, y):
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 큐 사용
    queue = deque()
    queue.append((x, y))

    while queue: # 큐가 빌 때까지 반복 
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if 0 <= nx < M and 0 <= ny < N: # 미로 범위 안에 있다면 
                if maze[ny][nx] == 1: # 안가본 칸이라면 
                    maze[ny][nx] += maze[y][x] 
                    queue.append((nx,ny))

                else:
                    continue # 용이 있으면 안감 
            
            else:
                continue # 범위 밖이면 안감 
    
    return maze[N-1][M-1]
    
N,M = map(int,input().split())

maze = [list(map(int,input())) for i in range(N)]

print(bfs(0,0))




