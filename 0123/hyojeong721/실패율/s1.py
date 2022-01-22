def solution(N, stages):
    temp = {}
    answer = []
    participant = len(stages)
    for i in range(1, N+1):
        #스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        inguser = stages.count(i)
        # 스테이지 : 실패율
        if inguser == 0:
            temp[i] = 0
        else:
            temp[i] = inguser/participant
        participant = participant - inguser
    print(temp)
    sortedtemp = sorted(temp.items(), key=lambda x: x[1], reverse=True)

    for item in sortedtemp:
        answer.append(item[0])
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))