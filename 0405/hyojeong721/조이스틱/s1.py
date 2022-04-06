def solution(name):
    answer = 0
    idx = 0

    while True:
        # 상하 카운트
        answer += min(ord(name[idx])-ord('A'), ord('Z')-ord(name[idx])+1)

        #좌우 카운트
        left, right = 1, 1
        while name[idx-left] == 'A':
            left += 1
        while name[idx+right] == 'A':
            right += 1

        answer += min(left, right)
        idx += -left if left < right else right

    return answer

print(solution("JEROEN"))