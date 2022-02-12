# 13 실패 -> s1에서 cross만 고침
def coltest(place, x, y):
    if x == 3:
        if place[x+1][y] == 'P':
            return 0
        else:
            return 1

    if x == 4:
        return 1

    if place[x+ 1][y] == 'P':
        return 0
    if place[x+2][y] == 'P':
        if place[x+1][y] != 'X':
            return 0
    return 1

def rowtest(place, x, y):
    if y == 3:
        if place[x][y+1] == 'P':
            return 0
        else:
            return 1
    if y == 4:
        return 1

    if place[x][y+1] == 'P':
        return 0
    if place[x][y+2] == 'P':
        if place[x][y+1] != 'X':
            return 0
    return 1

def crosstest(place, x, y):
    if x+1 >= 5 or y+1 >= 5:
        return 1

    if place[x+1][y+1] == 'P':
        if place[x+1][y] == 'X' and place[x][y+1] == 'X':
            return 1
        else:
            return 0
    else:
        return 1


def check(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                if rowtest(place, x, y) != 1 or coltest(place, x, y) != 1:
                    print(x, y,'행열검사아웃')
                    return 0
                if crosstest(place, x, y) == 0:
                    print(x, y,'대각선검사아웃')
                    return 0
    return 1

def solution(places):
    answer = []

    for p in places:
        answer.append(check(p))

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1, 0, 1, 1, 1]
print(solution(places))