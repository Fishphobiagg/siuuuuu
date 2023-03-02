# 감시 피하기
from itertools import combinations
'''
학생은 1
선생은 2
장애물은 3
'''
N = int(input())
school = [[1 if i == 'S' else 2 if i == 'T' else 0 for i in input().split()] for _ in range(N)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def run(x, y):
    obstacle = [1] * 4
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        while True:
            if nx<0 or ny <0 or ny==N or nx ==N:
                break
            if school[nx][ny] == 1 or school[nx][ny] == 3:
               break
            elif school[nx][ny] == 2:
               obstacle[i] = 0
               break
            nx += move[i][0]
            ny += move[i][1]
    if sum(obstacle)<4:
        return False
    else:
        return True

empty = []
student = []
# 학생, 장애물 놓을 좌표
for i in range(N):
    for j in range(N):
        if school[i][j] == 1:
            student.append((i, j))
        elif school[i][j] == 0:
            empty.append((i, j))

for a, b, c in list(combinations(empty, 3)):
    school[a[0]][a[1]], school[b[0]][b[1]], school[c[0]][c[1]] = 3, 3, 3
    cnt = 0
    for x, y in student:
        if run(x, y):
            cnt += 1
    if cnt == len(student):
        print('YES')
        exit()
    school[a[0]][a[1]], school[b[0]][b[1]], school[c[0]][c[1]] = 0, 0, 0

print('NO')
