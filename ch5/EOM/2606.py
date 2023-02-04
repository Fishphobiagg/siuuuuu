
# dfs 사용 
# 방문할때 마다 리스트에 넣기 

N = int(input())
M = int(input())

graph = [list(map(int, input().split())) for i in range(M)]
# print(graph)
check_list = [0] * (N+1)


def dfs(graph, check_list, v):
    
    if check_list[v] != 0: # 이미 방문했으면 즉시 종료 
        return
    
    check_list[v] += 1 # 방문 체크 
    # print(f'{v} 방문!')
    
    # 방문할 노드 스택에 넣기 
    stack = []
    for link in graph:
        # print(f'{link} 확인중')
        if v in link:
            # print(f'{v}가 {link}에 있어요')
            for node1 in link:
                # print(f'{node1} 확인중')
                if check_list[node1] == 0:
                    # print(f'{node1}은 방문 아직 안함')
                    stack.append(node1)
    
    stack.sort() # 크기 순으로 방문하기 위해 정렬
    # print(stack)
     
    # stack에 담긴 것들 방문 
    for node2 in stack: 
        # print(f'{node2} 시작')
        dfs(graph, check_list, node2)
    
dfs(graph, check_list, 1)
# print(check_list)
print(sum(check_list) - 1) # 1번 컴퓨터를 제외한 나머지 
    