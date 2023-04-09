# 누누와 윌럼프
'''
1.  던지기 : 1칸 다음칸 만큼 눈덩이 커짐
시작크기 : 1


'''


N ,M = map(int, input().split())
length = list(map(int, input().split()))
willump = 1
if N == 1:
    print(length[0]+1)
    exit()
def nunu(x,snow=1, time=0):
    global willump
    willump = max(willump, snow)
    if time == M:
        willump = max(willump, snow)
        return
    if x+1 <= N-1:
        nunu(x+1, snow+length[x+1], time+1)
    if x+2 <= N-1:
        nunu(x+2,snow//2+length[x+2],time+1)

nunu(-1)
print(willump)