# DFS와 BFS
from collections import deque


N, M, V = map(int, input().split())

graph = [[]for i in range(N)]
visited_BFS = [0 for i in range(N)]
visited_DFS = [0 for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# BFS
visited_BFS[V-1] = 1
Q = deque([V-1])
BFS_list = [V]
while Q:
    c = Q.popleft()
    graph[c].sort()
    for i in graph[c]:
        if not visited_BFS[i-1]:
            visited_BFS[i-1] = 1
            Q.append(i)
            BFS_list.append[i]        

print(*BFS_list)