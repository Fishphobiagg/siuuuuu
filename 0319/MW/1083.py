# 소트

'''

'''

N = int(input())
arr = list(map(int, input().split()))
chance = int(input())
start = 0

while chance and start < N - 1 and N > 1:
    bubble = arr[start:] if chance // (N - 1) else arr[start:start + chance + 1]
    chance -= arr.index(max(bubble)) - start
    bubble = [bubble.pop(bubble.index(max(bubble)))] + bubble
    for i in range(start, start + len(bubble)):
        arr[i] = bubble[i - start]
    start += 1

print(*arr)