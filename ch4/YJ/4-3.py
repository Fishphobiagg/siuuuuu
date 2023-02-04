#게임 개발
#맵의 세로크기 n, 가로크기 m
n, m = map(int, input().split())
#캐릭터의 좌표, 바라보는 방향
x, y, direction = map(int, input().split())

#왼쪽으로 도는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#이미 가본 위치를 저장
clone_map = [[0] * m for _ in range(n)]
clone_map[x][y] = 1

#전체 맵 input
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

#북 동 남 서 방향 (그 direction 번호가 차례로 0123이기 때문)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#시작
cnt = 1  #칸 수를 세는 문제라 1부터 시작
turn_time = 0
while True:
    turn_left()
    #캐릭터가 갈 곳
    nx = x + dx[direction]
    ny = y + dy[direction]
    if (clone_map[nx][ny] == 0) and (game_map[nx][ny] == 0):
        clone_map[nx][ny] =1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else: 
            break
        turn_time = 0 #??? 이건 왜?
print(cnt)
