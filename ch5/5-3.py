n, m = map(int, input().split())
map_list = []
cnt = 0
for i in range(n):
    map_list.append(list(map(int,input().split)))
def search(x,y):
    if map_list[x][y] == 0:
        map_list[x][y] = 1
        search(x-1, y)
        search(x, y+1)
        search(x+1, y)
        search(x, y-1)
        return 1
    return 0

for row in range(n):
    for col in range(m):
        if search(row,col) == 1:
            cnt += 1
print(cnt)
    