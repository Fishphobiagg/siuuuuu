N = int(input())

p_list = list(map(int,input().split())) # [3, 1, 4, 3, 2]
p_list.sort() # [1, 2, 3, 3, 4]

total = 0
for i in range(N):
    total += sum(p_list[:i+1])

print(total)