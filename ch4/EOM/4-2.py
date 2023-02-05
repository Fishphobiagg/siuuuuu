def knight_route(location):
    location = [ord(location[0])-96, ord(location[1])-48]
    # print(location)
    commends = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    count = 0
    for index in commends:
        new_lo = [location[0] + index[0], location[1] + index[1]]
        # print(new_lo)
        if 1 <= new_lo[0] <= 8 and 1 <= new_lo[1] <= 8:
            count += 1

    return count

location = input()
print(knight_route(location))

