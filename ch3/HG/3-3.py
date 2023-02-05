n, m = map(int, input().split())

num_list = [list(map(int,input().split())) for i in range(n)] #[[3, 1, 2], [4, 1, 4], [2, 2, 2]]

# min() / max() 함수를 이용한 풀이법 

min_list = []
for index1 in num_list:
    min_list.append(min(index1)) # min_list = [1, 1, 2]

print(max(min_list))




