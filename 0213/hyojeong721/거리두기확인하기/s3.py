# 패스
def second(place, ex_x, ex_y, x, y):
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < 5 and -1 < ny < 5:
            # 아까 검사했던 자리(맨처음 P였던 자리)는 패스
            if nx == ex_x and ny == ex_y:
                pass
            else:
                if place[nx][ny] == "P":
                    return 0
    return 1

def first(place, x, y):
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < 5 and -1 < ny < 5:
            # 상하좌우에 p있는 경우 아웃
            if place[nx][ny] == "P":
                return 0
            # 상하좌우에 O 잇는 경우 그자리로 가서 재검사
            elif place[nx][ny] == 'O':
                if second(place, x, y, nx, ny) == 0:
                    return 0

    return 1


def check(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                if first(place, x, y) == 0:
                    return 0

    return 1

def solution(places):
    answer = []

    for p in places:
        answer.append(check(p))

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# places=[["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]] # 답 0
result = [1, 0, 1, 1, 1]
print(solution(places))