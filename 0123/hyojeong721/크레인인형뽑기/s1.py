def solution(board, moves):
    answer = 0
    basket = []
    # 인형뽑기
    while moves:
        pos = moves.pop(0) - 1
        for i in range(len(board)):
            if board[i][pos] != 0:
                basket.append(board[i][pos])
                board[i][pos] = 0
                break
    print('basket', basket)

    # 중복인형 터뜨리기
    i = 0
    while i < len(basket):
        if i+1 < len(basket) and basket[i] == basket[i+1]:
            del basket[i:i+2]
            answer += 2
            i -= 1
        else:
            i += 1
    print(basket)

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# 크레인 작동 위치 배열
moves = [1,5,3,5,1,2,1,4]
# result = 4
print(solution(board, moves))

