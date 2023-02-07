N = int(input())
E = list(map(int, input().split()))
M = int(input())
W = list(map(int, input().split()))

reply = []
for i in W:
    if i in E:
        result = 'yes'
        reply.append(result)
    else:
        result = 'no'
        reply.append(result)

    print(result, end=' ')