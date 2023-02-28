import sys
sys.stdin = open('input_for_9_3.txt')
# 다익스트라 
import heapq

# 도시의 개수 , 통로의 개수, 메세지를 보내고자 하는 도시 
N,M,C = map(int,input().split())

# 각 노드에 연결되어 있는 노드의 정보를 담은 리스트
graph = [[] for _ in range(N+1)]

# x에서 y로 걸리는 시간 z
for _ in range(M):
    X, Y, Z = map(int, input().split())
    # 걸리는 시간, 도착 도시
    graph[X].append((Z,Y))

# 초기 거리정보를 무한대로 설정
inf = 10e9
distance = [inf] * (N+1)

def dijkstra(start):
    q = []
    # 시작노드로 가기위한 최단 경로 0 
    heapq.heappush(q, (0,start))
    while q: # q가 비어있지 않다면
        # 최단거리 정보 꺼내기 
        dist, now = heapq.heappop(q)
        # 이미 처리 했다면 무시
        if dist > distance[now]:
            continue
        # 현재 노드와 연결되어 있는 노드들 확인 
        for i in graph[now]:
            cost = dist + i[0]
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q,(cost, i[1]))

    counts = 0
    for d in range(N+1):
        if distance[d] < inf:
            counts += 1
        else:
            distance[d] = -1
    
    return f'{counts} {max(distance)}'

print(dijkstra(C))
            









