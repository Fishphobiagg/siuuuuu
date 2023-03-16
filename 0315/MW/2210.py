#number jump machine

jump = [list(map(int, input().split())) for _ in range(5)]
ans = []
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def dfs(x,y, number=''):
    if len(number)==6:
        if number not in ans:
            ans.append(number)
    else:
        for i in range(4):
            nx = x+move[i][0]
            ny = y+move[i][1]
            if nx < 0 or ny < 0 or nx == 5 or ny == 5:
                continue
            dfs(nx, ny, number+str(jump[nx][ny]))

for i in range(5):
    for j in range(5):
        dfs(i, j)

print(len(ans))