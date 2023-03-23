import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    start, end = 0, 10000
    while start < end:
        mid = (start+end)//2
        if mid*(mid+1)*K>=2*N:
            end = mid
        else:
            start = mid+1
    total = start*(start+1)//2
    if start%2:
        print(K*(start//2+1)+(N-1)-total*K, 'R')
    else:
        print(-K*(start//2)-((N-1)-total*K), 'L')
