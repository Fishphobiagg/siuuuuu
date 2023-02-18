# 백준 지름길
# https://www.acmicpc.net/problem/1446
# 다익스트라 
import sys
sys.stdin = open('input_for_1446.txt')

import heapq

def dijkstra(M):
    q = []
    # 시작위치까지의 이동거리, 시작위치 
    heapq.heappush(q,(0,0))
    while q: # q가 빌때까지
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 확인했다면 무시
            continue
        for i in graph[now]: # 현재위치와 연결된 길 확인
            cost = dist + i[1]
            # print(i[0])
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0])) 

    return distance[M]

# T = int(input())

# fr _ in range(T):
# 지름길의 개수, 고속도로의 길이(도착점)
N, D = map(int,input().split())

# 각 노드와 연결된 노드들의 정보를 넣을 리스트 
# [도착위치, 거리]
graph = [[(i+1, 1)] for i in range(10001)]
del graph[-1][0]

# 각 노드와 연결된 노드들의 정보 입력
# 시작위치 , 도착위치, 지름길의 길이 
for _ in range(N):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
inf = 10001
distance = [inf]*(10001) 
# print(distance)
print(dijkstra(D))