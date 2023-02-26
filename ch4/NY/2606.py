import sys
sys.stdin = open('2606.txt')

N = int(input())
M = int(input())

graph = [[] * N for i in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def Dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            Dfs(i)
            cnt += 1

Dfs(1)
print(cnt)

