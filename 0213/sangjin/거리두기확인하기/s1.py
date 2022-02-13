##### XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

dx1 = [-1, 0, 1, 0]
dy1 = [0, 1, 0, -1]
dx2 = [-2, -1, 0, 1, 2, 1, 0, -1]
dy2 = [0, -1, -2, -1, 0, 1, 2, 1, ]


def dist_1(i, j, place):
    for k in range(4):
        ni = i + dx1[k]
        nj = j + dy1[k]
        if ni in range(5) and nj in range(5) and place[ni][nj] == "P":
            return 0
    return 1


def dist_2(i, j, place):
    for k in range(8):
        ni = i + dx2[k]
        nj = j + dy2[k]
        if ni in range(5) and nj in range(5) and place[ni][nj] == "P":
            if k % 2:
                if i + dx1[(k // 2) % 4] in range(5) and j + dy1[(k // 2) % 4] in range(5) and \
                        place[i + dx1[(k // 2) % 4]][j + dy1[(k // 2) % 4]] == "O":
                    return 0
                elif i + dx1[(k // 2 + 1) % 4] in range(5) and j + dy1[(k // 2 + 1) % 4] in range(5) and \
                        place[i + dx1[(k // 2 + 1) % 4]][j + dy1[(k // 2 + 1) % 4]] == "O":
                    return 0
            else:
                if place[i + dx1[k // 2]][j + dy1[k // 2]] == "O":
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        for i in range(5):
            for j in range(5):
                # p 찾기
                if place[i][j] == "P":
                    if dist_1(i, j, place) and dist_2(i, j, place):
                        answer.append(1)
                    else:
                        answer.append(0)

    return answer