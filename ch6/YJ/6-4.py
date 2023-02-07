#두 배열의 원소 교체
# import sys
# sys.stdin = open("input.txt", "r", encoding= 'UTF8')

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#a는 오름차순, b는 내림차순
a = sorted(a)
b = sorted(b, reverse = True)

print(a)
print(b)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))
