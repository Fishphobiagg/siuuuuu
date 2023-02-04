#왕실의 나이트
coordinate = input()


r = int(coordinate[1])
#아스키코드 a가 97이므로 1부터
c = ord(coordinate[0])- 96 


cases = [(-2,-1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

cnt = 0 #경우의 수를 담아줄 변수

for i in range(len(cases)):
    row = r + cases[i][0]
    col = c + cases[i][1]
#구간에서 벗어나지 않으면 카운트 +1
    if (row > 0) and (row <= 8) and (col > 0) and (col <= 8):
        cnt += 1

print(cnt)

