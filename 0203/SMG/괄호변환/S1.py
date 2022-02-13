def solution(p):
    N = len(p)
    answer = ''
    if not p:
        return answer
    cnt1 = 0
    cnt2 = 0
    for i in range(N-1):
        if p[i] == "(":
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            u = p[:i+1]
            v = p[i+1:]
            break
    else:
        u = p
        v = ''

    stack = []
    for i in u:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop(-1)
            else:
                stack.append(i)
    temp = ''
    if stack:
        for i in u:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        answer = '(' + solution(v) + ')' + temp[1:-1]
    else:
        answer = u + solution(v)

    return answer

print(solution("()))((()"))