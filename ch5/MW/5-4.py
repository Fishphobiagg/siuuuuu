# 미로 탈출
from collections import deque

N, M = map(int,input().split())

maze = [list(int(i)for i in input()) for j in range(N)]
cursor = deque((0, 0))
move_x = [1, 0, 0, -1]
move_y = [0, -1, 1, 0]

count = 0

while cursor != deque(N-1, M-1):
    Q = cursor.popleft()
    for i in range(4): # 오른쪽 맨 아래가 목적지 -> 오른쪽, 아래 우선으로 진행
        next_x = Q[0] + Q[i]
        next_y = Q[1] + Q[i]
        if next_x < 0 or next_x > N-1 or next_y <0 or next_y > M-1:
            continue
        if maze[Q[0]+move_x[i]][Q[1]+move_y[i]]:
            cursor.append((next_x, next_y))
            count += 1

print(count)