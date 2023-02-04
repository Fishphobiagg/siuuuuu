# 음료수 얼려 먹기 
# dfs 사용하면 쉽대

def dfs(y,x):
    if 0 <= y < N and 0 <= x < M:
        if ice_case[y][x] == 0: # 음료가 안부어진 공간이면  
            ice_case[y][x] = 1 # 음료 붓기(방문 체크) 
            dfs(y-1,x) # 위칸 확인 
            dfs(y+1,x) # 아래칸 확인 
            dfs(y,x-1) # 왼칸 확인 
            dfs(y,x+1) # 오른칸 확인 
            return True

    else: # 얼음틀 범위에서 벗어나면 종료 
        return False  
    
def count_ice(N,M):
    counts = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                counts += 1
    
    return counts



# 입력
N,M = map(int,input().split())

ice_case = [list(map(int,input())) for i in range(N)]

print(count_ice(N,M))