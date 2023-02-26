map_row, map_col = map(int, input().split())  # 맵 
row, col, dir = map(int, input().split())  # 캐릭터 생성 
map_list = [[]] * len(map_col)
for i in range(len(map_col)):  # 맵 정보 받기
    map_list[i] = list(map(int, input().split())) # i번째 인덱스에 맵 정보 저장
cnt = 1 # 총 방문 횟수
finish = 0 # 만약 한바퀴 돌아도 변화가 없다면 종료하기 위해
    

while True: 
    if finish >= 4: # 네바퀴 돌 동안 변화가 없으면 종료
        break
    map_list[row][col] = 1  # 현재 위치를 다시 방문 못하도록 함
    if dir == 0: #북쪽을 바라볼경우
        if map_list[row][col-1]: # 현재 위치 왼쪽이 1이라면
            dir = 3 #서쪽을 바라보도록
            finish += 1
            continue 
        else : # 땅이라면
            col -= 1
            cnt += 1
            finish = 0
    if dir == 1: #동쪽을 바라볼경우
        if map_list[row-1][col]: # 현재 위치 위쪽이 1이라면
            dir = 0 #북쪽을 바라봄
            finish += 1
            continue 
        else : # 땅이라면
            row -= 1
            cnt += 1
            finish =0
    if dir == 2: #남쪽을 바라볼경우
        if map_list[row][col+1]: # 현재 위치 오른쪽이 1이라면
            dir = 1 # 동쪽을 바라봄
            finish += 1
            continue 
        else : # 땅이라면
            col += 1
            cnt += 1
            finish = 0
    if dir == 3: #서쪽을 바라볼경우
        if map_list[row+1][col]: # 현재 위치 아래가 1이라면
            dir = 2 #남쪽을 바라봄
            finish += 1
            continue 
        else : # 땅이라면
            row += 1
            cnt += 1    
            finish =0
print(cnt)