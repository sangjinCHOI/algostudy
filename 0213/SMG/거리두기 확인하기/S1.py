def solution(places):
    answer = []
    locations = []
    for i in places:
        temp = []
        for y in range(5):
            for x in range(5):
                if i[y][x] == 'P':
                    temp.append((x, y))
        locations.append(temp)
    print(locations)
    for location in range(5):
        check = True
        for i in locations[location]:
            for j in locations[location]:
                if abs(i[0]-j[0]) + abs(i[1]-j[1]) == 1:
                    check = False
                elif abs(i[0]-j[0]) + abs(i[1]-j[1]) == 2:
                    if i[0] < j[0] and i[1] == j[1]:
                        if places[location][i[1]][j[0]-1] == 'O':
                            check = False
                    elif i[1] < j[1] and i[0] == j[0]:
                        if places[location][j[1]-1][i[0]] == 'O':
                            check = False
                    elif i[0] < j[0]:
                        if i[1] < j[1]:
                            if i[1]+1 <= 4 and places[location][i[1]+1][i[0]] == 'O':
                                check = False
                            elif i[0]+1 <= 4 and places[location][i[1]][i[0]+1] == 'O':
                                check = False
                        elif i[1] > j[1]:
                            if i[1]-1 >= 0 and places[location][i[1]-1][i[0]] == 'O':
                                check = False
                            elif i[0]+1 <= 4 and places[location][i[1]][i[0]+1] == 'O':
                                check = False
        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))