import sys
sys.stdin = open('1260.txt')

N, M, v = map(int, input().split())
graph = [[0] * (N + 1) for i in range(N + 1)]
visited = [0] * (N + 1)

for j in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def Dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if (visited[i] == 0) and (graph[v][i] == 1):
            Dfs(i)

def Bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, N + 1):
            if (visited[i] == 1) and (graph[v][i] == 1):
                queue.append(i)
                visited[i] = 0

Dfs(v)
print()
Bfs(v)
