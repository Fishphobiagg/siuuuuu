N = int(input())
arr = [sorted(list(map(int, input().split())), reverse=True) for _ in range(N)]
idx = [0]*N
ans = []
while len(ans) < N:
    max_num = -10000000000
    max_idx = N
    for i in range(N):
        if arr[i][idx[i]] > max_num:
            max_num = arr[i][idx[i]]
            max_idx = i
    ans.append(arr[max_idx][idx[max_idx]])
    idx[max_idx] += 1
print(ans[-1])