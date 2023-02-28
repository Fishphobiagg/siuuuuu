# 감시 피하기

'''
선생님은 각자의 위치에서 델타 탐색하며 감시를 한다.
장애물에 막히기전까지의 범위는 모두 커버 가능
S = 학생
T = 선생
O = 장애물

3개의 장애물 설치하여 모든 학생이 감시로부터 피할 수 있게
-> 학생의 상하좌우를 깔끔하게 만들어줘야 한다.

학생과 선생이 붙어있는 경우에는 무조건 NO
열을 순회해서, 학생 다음 바로 선생이나 선생 다음 바로 장애물이 나오면 컷컷컷컷
스택에 넣어놓고 그 다음 S,T,O의 경우에 따라 검사
run 함수에는 학생 좌표 넣기
'''
move = [(0,1), (1,0), (-1,0), (0,-1)]
def run(x, y, direction): # 학생좌표 기준으로 사방에 선생이 없거나, 다음에 만나는 오브젝트가 장애물일 경우 통과
    nx = x+move[i][direction]
    ny = y+move[i][direction]
    if school[nx][ny] == 'T':
        return False
    elif school[nx][ny] == 'O':
        return True
    elif nx == N or ny == N or nx < 0 or ny < 0:
        return True
    else:
        run(nx,ny,direction)
def obstacle(): # 장애물 경우의 수 생성 후 run 함수 실행
    # 순열 생성 및 해당 좌표 장애물 처리
        
ans = 'YES'
N = int(input())
school = [input().split() for _ in range(N)]
student = []
empty = []
# 학생, 장애물 후보지 좌표 몰색
for i in range(N):
    for idx, object in enumerate(school):
        if object == 'S':
            student.append((i, idx))
        elif object=='X':
            empty.append((i, idx))
            
if obstacle():
    print('YES')
    exit()