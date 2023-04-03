# 로봇
'''
hint : 3차원 리스트로 방문처리
'''
from collections import deque

M, N = map(int, input().split())
factory = [list(map(int,input().split())) for _ in range(M)]
start_x, start_y, s_dir = map(int, input().split())
end_x, end_y, e_dir = map(int, input().split())
move = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북
visited = [[[0] for k in range(4)]*N for i in range(M)]
