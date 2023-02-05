x_move = [2, 2, 1, 1, -2, -2, -1, -1]
y_move = [1, -1, 2, -1, 1, -1, 2, -2]
night = str.maketrans('abcdefgh', '12345678')

location = input()
location.translate(night)

count = 0

for i in range(8):
    x_location = int(location[0]) + x_move[i]
    y_location = int(location[1]) + y_move[i]
    if x_location > 0 and x_location < 9 and y_location > 0 and y_location < 9:
        count+=1
    
print(count)