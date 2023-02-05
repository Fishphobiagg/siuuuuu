# 프린터 큐
from collections import deque

def find(quque,M):
    count = 0
    while True:
        # 프린트 
        max_index = max(quque)
        print_index = quque.popleft()
        M -= 1 # 관심있는 출력물의 위치 -1 

        if M == -1:  # 출력된게 관심있는 출력물이면       
            if max_index == print_index : # 만약 뽑은게 중요도 제일 큰거라면 
                count += 1  # 카운트
                # print(quque, M)
                return count 
            else: # 중요도 떄문에 아직 뽑을 차례가 아니면 
                quque.append(print_index) # 도로 집어넣기 
                M = len(quque) - 1 # 순서는 맨뒤
                # print(quque, M) 
                continue
        else: # 출력된게 관심있는게 아니면 
            if max_index == print_index : # 출력된게 중요도 가장 큰거라면
                count += 1  # 카운트
                # print(quque, M)
                continue # 뽑은채로 다음거 뽑으러 돌아감
            else: # 출력된게 아직 차레까 아니면
                quque.append(print_index) # 도로 집어넣음 
                # print(quque, M)
                continue 

T = int(input())

for i in range(T):
    N , M = map(int,input().split())
    quque = deque(list(map(int,input().split())))
    print(find(quque,M))

