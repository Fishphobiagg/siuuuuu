# 1 : x +- 2 / y +- 1
# 2 : x +- 1 / y +- 2


def route(list):
    if 6>= list[0] >= 3:
        if 6 >= list[1] >= 3:
            return 8
        elif list[1] == 2 or list[1] == 7 :
            return 6
        elif list[1] == 1 or list[1] == 8:
            return 2
    elif list[0] == 2 or list[0] == 7:
        if 6 >= list[1] >= 3:
            return 6
        elif list[1] == 2 or list[1] == 7 :
            return 4
        elif list[1] == 1 or list[1] == 8:
            return 3
    elif list[0] == 1 or list[0] == 8:
        if 6 >= list[1] >= 3:
            return 4
        elif list[1] == 2 or list[1] == 7 :
            return 3
        elif list[1] == 1 or list[1] == 8:
            return 2
        
        
            
tc = list(input())

y_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

knight_location = [y_dict.get(tc[0]), int(tc[1])]

print(route(knight_location))

