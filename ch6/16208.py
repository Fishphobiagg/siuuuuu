n = int(input())
lst = list(map(int, input().split()))
lst.sort()

total = 0
for i in range(n):
    result = lst[i] * sum(lst[i+1:n])
    total += result

print(total)