
def game(x,y,direction):

    def turn(direction1):
        direction1 -= 1
        if direction1 < 0 :
            direction1 = 3
        return direction1

    # 변경사항이 없을 global 변수들 가져오기 
    global game_map
    global N
    global M


    # 방문 기록 용 맵
    check_map = [[0] * M for j in range(N)]
    # 이동 횟수
    move = 0
    # 회전 수 
    turn_count = 0
    
    # 이동 커멘드 
    dx = [0, 1, 0, -1] 
    dy = [-1, 0, 1, 0]

    # 현위치는 1로 바꿈
    check_map[x][y] = 1

    while True:
        # 1
        # 회전 
        direction = turn(direction)
        print('turn')
        turn_count += 1
        # 1칸 이동할때의 위치 
        nx = x + dx[direction]
        ny = y + dy[direction] 
        print(ny, nx)
        
        # 2  
        if game_map[ny][nx] == 0 and check_map[ny][nx] == 0: # 전진할 칸이 바다가 아님 and 가보지 않은 칸 이면 go
            x = nx
            y = ny
            check_map[ny][nx] = 1
            move += 1
            print('move')
            turn_count = 0
        else : # 전진할 칸이 바다거나 가본 칸이면 
            if turn_count == 4: # 네방향 모두 전진 불가이면

                return move + 1 # +1 은 초기 위치 


            continue # 1로 돌아가기 

        # 3 
          




# 맵 크기 N x M
N,M = map(int, input().split())

# 캐릭터의 초기 위치 
x,y,direction = map(int, input().split())

# 게임 맵
game_map = [list(map(int,input().split())) for i in range(N)]

print(game(x,y,direction))
