location = input()  # a1
col = location[0]  # a
row = location[1]  # 1
best = 8
# row 
if row == '1' or row == '8':  # 만약 가장 끝줄에 있다면, 4가지 경우가 줄어든다
    best -= 4
elif row =='2' or row == '7':  # 만약 끝줄에서 두번째에 있다면, 2가지 경우가 줄어든다
    best -= 2


if col == 'a' or col == 'h':  # 만약 가장 끝줄에 있다면, 4가지 경우가 줄어든다
    best -= 4
elif col == 'b' or col == 'g':  # 만약 끝줄에서 두번째에 있다면, 2가지 경우가 줄어든다
    best -= 2

if best == 0:  # 가장 구석에 있을 경우, row와 col에서 두번 중복되므로 +2
    best = 2
elif best == 2: # row와 col중 하나가 끝줄이 아니고 두번째 줄일 경우, row와 col에서 한번 중복되므로 +1
    best = 3
print(best)