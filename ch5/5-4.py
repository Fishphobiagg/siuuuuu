from collections import deque

n, m = map(int, input().split())
maze = [] #맵 정보
for _ in range(n):
    maze.append(list(map(int, input())))
#방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs 구현
def bfs(x, y):
    #큐 구현을 위한 deque 라이브러리
    #deque(덱)은 앞 뒤로 요소를 추가, 제거할 수 있는 자료구조
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        #제일 끝 요소가 아니라 제일 앞의 요소가 삭제됨.
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #0일 경우에는 무시
            if maze[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단거리 기록
            #가는 경로마다 숫자를 1씩 더해주자
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                print(maze[nx][ny])
                print(maze[x][y])
                #print(f' 이건nx {nx}')
                #print(f' 이건ny {ny}')
                queue.append((nx, ny))
                #print(queue)
    #가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n-1][m-1]
#bfs를 수행한 결과
print(bfs(0,0))



