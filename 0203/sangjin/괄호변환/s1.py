def correct(arr):
    stack = []
    for a in arr:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if not stack:
                return 0
            stack.pop()
    return 1


def rev(arr):
    result = ''
    for a in arr:
        if a == '(':
            result += ')'
        else:
            result += '('
    return result


answer = ''
def solution(p):
    global answer
    stack = []
    u, v = "", ""

    if not p:
        return ""
    else:
        if correct(p):
            return p
        else:
            for i in range(2, len(p) + 1):
                if p[:i].count('(') == p[:i].count(')'):
                    u = p[:i]
                    v = p[i:]
                    break
            if correct(u):
                answer += u + solution(v)
            else:
                answer += '(' + solution(v) + ')' + rev(u[1:len(u) - 1])

    return answer