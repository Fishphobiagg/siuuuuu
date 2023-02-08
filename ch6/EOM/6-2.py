
T = int(input())
num_list = []
for i in range(T):
    num = int(input())
    num_list.append(num) 

num_list.sort(reverse = True)
print(' '.join(str(x) for x in num_list))

