def test(p):
    s = []
    for i in p:
        if i == '(':
            s.append(i)

        if i == ')':
            if s and s[-1] == '(':
                s.pop()

    if len(s) == 0:
        return True
    else:
        return False

def sep(p):
    if len(p) < 1:
        return p
    else:
        u = ''
        i = 0
        while i < len(p):
            u += p[i]
            if u.count('(') == u.count(')'):
                break
            i += 1
        v = p[i+1:]

        return u, v

def solution(p):
    res = ''
    # 1번
    if p == '':
        return p
    # 올바른 괄호 문자열인지
    if test(p):
        return p

    u, v = sep(p)

    # 3번
    if test(u):
        return u + solution(v)
    else:
        res += '('
        res += solution(v)
        res += ')'

        u = u[1:-1]
        reversed_u = ''
        for i in u:
            if i == "(":
                reversed_u += ')'
            else:
                reversed_u += '('

    return res + reversed_u

print(solution("()))((()"))