N, M, K = map(int,input().split())

num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
a, b = num_list[0], num_list[1]
num = a*K + b
print(num)
if a == b:
    print(a*M)
else:
    if M%(K+1) ==0:
        print(num * (M//(K+1)))
    else:
        print(num * (M//(K+1)) + a*(M%K))
