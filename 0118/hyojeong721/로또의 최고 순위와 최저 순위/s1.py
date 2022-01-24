def solution(lottos, win_nums):
    answer = [0, 0]
    # 0갯수 세기
    zero_cnt = 0
    # 현재 맞은 번호 갯수알기 = 최저순위
    now_cnt = 0
    for i in range(6):
        if lottos[i] == 0:
            zero_cnt += 1
        elif lottos[i] in win_nums:
            now_cnt += 1
    answer[0] = zero_cnt + now_cnt
    answer[1] = now_cnt
    print('answer', answer)


    # 갯수를 순위로 바꾸기
    for idx, num in enumerate(answer):
        if num == 6:
            answer[idx] = 1
        elif num == 5:
            answer[idx] = 2
        elif num == 4:
            answer[idx] = 3
        elif num == 3:
            answer[idx] = 4
        elif num == 2:
            answer[idx] = 5
        else:
            answer[idx] = 6

    return answer


lottos = [45, 4, 35, 20, 3, 9]
win_nums = 	[20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))