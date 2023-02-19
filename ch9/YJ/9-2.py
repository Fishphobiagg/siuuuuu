#  9-2 미래도시
INF = int(1e9)  # 무한을 의미하는 값

n, m = map(int, input().split()  # n: 전체 회사의 개수 / m: 경로의 개수
# 2차원 리스트. 모든 값에 무한. 리스트 컴프리핸션
arr = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에도 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            arr[a][b] = 0
# 기본 값은 무한이지만 각 간선에 대한 정보를 받고
# 서로에게 가는 비용은 1이라고 설정
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# 거쳐갈 노드 k와 최종목적지 노드 x
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

# 수행된 결과를 출력
ans = arr[1][k] + arr[k][x]

#도달할 수 없는 경우, -1을 출력
if ans >= IMF:
    print('-1')
# 도달할 수 있다면, 최단거리 출력
else:
    print(ans)
