# 심뽀찜뽀

N, M = map(int,input().split())
nemmo = [[0]*(M+1) for _ in range(N+1)]
res = 0
def back(x, y): # -> 방향으로 검사
    global res
    if x == N+1 and y == 1:
        res += 1
        return
    if y == M:
        ny = 1
        nx = x + 1
    else:
        nx = x
        ny = y + 1
    if not nemmo[x][y-1] or not nemmo[x-1][y] or not nemmo[x-1][y-1]:
        nemmo[x][y] = 1
        back(nx, ny)
        nemmo[x][y] = 0
    back(nx,ny)

back(1, 1)
print(res)