def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for test in range(int(input())):
    N, M = map(int, input().split())
    parent = list(range(0, N + 1))
    a = list(map(int, input().split()))
    for i in range(M):
        union(a[i * 2], a[i * 2 + 1])
    for i in range(1, N+1):
        parent[i] = find(i)
    print(f'#{test + 1} {len(set(parent)) - 1}')