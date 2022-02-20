from itertools import permutations
def solution(expression):
    symbol = ['+', '-', '*']
    answer = []
    for per in permutations(symbol):
        f, s = per[0], per[1]
        lst = []
        for e in expression.split(f):
            temp = [f"({i})" for i in e.split(s)]
            lst.append(f'({s.join(temp)})')
        answer.append(abs(eval(f.join(lst))))
    return max(answer)