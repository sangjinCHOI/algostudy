def solution(dartResult):
    score_lst = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i+1] == 'S':
                score_lst.append(int(dartResult[i]))
                i += 1
            elif dartResult[i+1] == 'D':
                score_lst.append(int(dartResult[i])**2)
                i += 1
            elif dartResult[i+1] == 'T':
                score_lst.append(int(dartResult[i])**3)
                i += 1
            else:
                if dartResult[i + 2] == 'S':
                    score_lst.append(10)
                elif dartResult[i + 2] == 'D':
                    score_lst.append(10 ** 2)
                elif dartResult[i + 2] == 'T':
                    score_lst.append(10 ** 3)
                i += 2
        elif dartResult[i] == '*':
            score_lst[-1] *= 2
            if len(score_lst) > 1:
                score_lst[-2] *= 2
        elif dartResult[i] == '#':
            score_lst[-1] -= score_lst[-1]*2
    answer = sum(score_lst)
    return answer

print(solution('10S*2T*3S'))