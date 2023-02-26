import heapq
import sys
sys.stdin = open('input_for_9_2.txt')

# 다익스트라 
def dijkstra(start,end):
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [inf] * (N+1)
    q = []
    # 시작노드로 가기 위한 최단 경로는 0으로 설정해서 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q : # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인 
        for i in graph[now]:
            cost = dist + i[1] 
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    print(distance)
    return distance[end]

T = int(input())
for _ in range(T):
    inf = 10e9 # 무한 
    # 노드의 개수, 간선의 개수
    N,M = map(int,input().split())
    
    # 시작 번호 
    # start = 1
    
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 
    graph = [[] for _ in range(N+1)]
    
    # 간선 정보 입력 받기 
    for _ in range(M):
        s, e = map(int,input().split())
        # s번 노드에서 e번 노드로 가는 비용이 1
        graph[s].append((e, 1))
    
    # K번 회사를 방문한 뒤 X번 회사로 가는것이 목표 
    X,K = map(int,input().split())
    
    
    # 1 -> K -> X
    if K < X:
        if dijkstra(1,K) >= inf or dijkstra(K,X) >= inf:
            print(-1)
        else:    
            print(dijkstra(1,K) + dijkstra(K,X))
    else:
        if dijkstra(1,K) >= inf or dijkstra(X,K) >= inf:
            print(-1)
        else:    
            print(dijkstra(1,K) + dijkstra(X,K))
    
    
    
    