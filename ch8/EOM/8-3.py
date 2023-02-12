N = int(input())
container = [0] + list(map(int,input().split()))

foods = [0]*101 # 식량 수를 저장할 리스트 
foods[1], foods[2] = container[1], max(container[1], container[2])

for i in range(3,N+1):

        foods[i] =  max(foods[i-1] , foods[i-2] + container[i])


print(foods[N]) 

