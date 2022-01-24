def solution(board, moves):
    answer = 0
    N = len(board)
    bowl = []
    for i in moves:
        for j in range(N):
            if board[j][i-1]:
                if bowl and bowl[-1] == board[j][i-1]:
                    answer += 2
                    bowl.pop(-1)
                else:
                    bowl.append(board[j][i-1])
                board[j][i-1] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))