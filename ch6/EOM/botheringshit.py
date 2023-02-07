N = int(input())

sticks = list(map(int,input().split()))

sticks.sort()
sum_sticks = sum(sticks)
sum_sum_sum = 0
for i in range(N-1):
    sum_sticks -= sticks[i]
    sum_sum_sum += sticks[i] * sum_sticks 

print(sum_sum_sum)
    
    
# N = int(input())

# sticks = list(map(int,input().split()))

# sticks.sort()

# sum_sum_sum = 0
# for i in range(N-1):
#     sum_sum_sum += sticks[i] * sum(sticks[i+1:]) 

# print(sum_sum_sum)
        
    