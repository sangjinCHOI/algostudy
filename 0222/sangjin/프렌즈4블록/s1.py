def down(board):
    status = 0
    for i in range(len(board) - 1, 0, -1):
        for j in range(len(board[0])):
            if board[i][j] == "-" and board[i - 1][j] != "-":
                board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                status += 1
    return status, board


def solution(m, n, board):
    cnt = 0
    tmp = 1
    while tmp:
        board = [list(board[i]) for i in range(m)]
        cord = []
        for i in range(m - 1):
            for j in range(n - 1):
                a, b, c, d = board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1]
                if a == b == c == d and a != "-" and b != "-" and c != "-" and d != "-":
                    if [i, j] not in cord:
                        cord.append([i, j])
                    if [i, j + 1] not in cord:
                        cord.append([i, j + 1])
                    if [i + 1, j] not in cord:
                        cord.append([i + 1, j])
                    if [i + 1, j + 1] not in cord:
                        cord.append([i + 1, j + 1])

        for c in cord:
            board[c[0]][c[1]] = "-"

        status = 1
        while status:
            status, board = down(board)

        tmp = len(cord)
        if tmp:
            cnt += tmp
        else:
            break

    answer = cnt
    return answer