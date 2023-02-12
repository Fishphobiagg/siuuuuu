n = int(input())
arr = list(map(int, input().split()))

d = [arr[0], max(arr[0], arr[1])]
for i in range(2, n):
    d.append(max(d[i-1], d[i-2]+arr[i]))

print(d[n-1])