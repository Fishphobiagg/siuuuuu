N = int(input())
score = []
for _ in range(N):
    data = input().split()
    score.append((data[0], int(data[1])))

array = dict(score)
print(*sorted(list(array.keys())))
