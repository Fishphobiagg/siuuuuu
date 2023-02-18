# 전보
import heapq
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

# n: 도시의 개수, m: 통로의 개수, c: 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())
INF = int(1e9)  # 무한을 의미하는 값
# 각 노드에 연결되어 있는 노드에 대한 정보를 담을 리스트
graph = [[] for i in range(n+1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

# 다익스트라 함수만들기
def dijkstra(c):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정. 큐에 삽입
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:  # 큐가 빌 때까지 반복
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        # dist: 경로 now: 지점
        dist, now = heapq.heappop(q)  # 시작 노드가 먼저 나올 것 (튜플 앞 숫자 기준)
        #print(dist, now, q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # i[1]은 i[0]으로 가는 비용
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
# 다익스트라 수행
dijkstra(c)

#도달할 수 있는 노드의 개수 (메시지를 받는 도시의 총 개수)
cnt = 0
#도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    #도달할 수 있는 노드인 경우
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)
#시작노드 제외 cnt -1
print(cnt-1, max_distance)








