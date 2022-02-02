def solution(s):
    answer = []
    N = len(s)//2
    for i in range(1, N+2):
        temp = ''
        cnt = 1
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+(2*i)]:
               cnt += 1
            elif cnt < 2:
                temp += s[j:j+i]
            else:
                temp += (str(cnt) + s[j:j+i])
                cnt = 1
        answer.append(len(temp))
    return min(answer)

print(solution('d'))