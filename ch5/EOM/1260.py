def dfs(graph,  V, check, print_list):
    
    if check[V] == 1: # 이미 방문했으면 즉시 종료    
        return 
    
    check[V] += 1 # 방문체크
    # print(V,end = ' ')
    print_list.append(V)
    
    
    stack = [] # 방문해야하는 노드를 담을 스택
    for link in graph:
        if V in link: 
            for node1 in link:
                if check[node1] == 0: # 방문 안했으면
                    stack.append(node1) # 방문해야할 노드를 스택에 넣기
    
    stack.sort() # 크기순으로 방문해야하므로 정렬 
    # print(stack)
    
    for node2 in stack: # 스택에 담긴 노드들 방문
        dfs(graph, node2, check, print_list)
        
        
def bfs(graph, V, check, print_list):
    from collections import deque
    
    quque = deque()
    quque.append(V)

    while quque:
        V = quque.popleft() # 큐에서 꺼내기 
        
        if check[V] == 1: # 이미 방문했으면 종료 
            continue
        
        check[V] += 1 # 방문체크
        # print(V, end = ' ') 
        print_list.append(V)
        
        check_list = [] # V와 간선으로 연결된 노드를 담을 리스트
        for link in graph:
            if V in link: 
                for node1 in link:
                    if check[node1] == 0: # 방문 안했으면
                        check_list.append(node1) # 방문해야할 노드를 리스트에 넣기
        
        check_list.sort() #여러개의 간선으로 연결되어있으면 작은거부터 해야하므로 정렬
        
        # 큐에 연결된 노드들 넣기 
        for node2 in check_list:
            quque.append(node2)      
            
N, M, V = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(M)]

check = [0] * (N+1) # 방문체크용 리스트

print_list = []
        

dfs(graph, V, check, print_list)
print(' '.join(str(x) for x in print_list))
check = [0] * (N+1)
print_list = []
bfs(graph, V, check, print_list)
print(' '.join(str(x) for x in print_list))  