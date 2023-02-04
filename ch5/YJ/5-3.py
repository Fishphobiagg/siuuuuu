#음료수 얼려먹기

#dfs함수. 특정 노드와 연결된 모든 노드 방문
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if tray[x][y] == 0: #아직 방문하지 않은 막히지 않은 곳
        tray[x][y] = 1 #방문 표시.
        dfs(x-1 , y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

#세로 길이 n /가로 길이 m
n, m = map(int, input().split())

tray = []
for _ in range(n):
    tray.append(list(map(int, input())))

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True: #dfs(i, j)의 type은 bool
            ans += 1

print(ans)

