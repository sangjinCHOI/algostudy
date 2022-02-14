from itertools import permutations


def operation(a, b, op):
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    elif op == "*":
        return int(a) * int(b)


def solution(expression):
    answer = []
    num, ops, formula = [], [], []
    tmp = ''
    for word in expression:
        if word.isdigit():
            tmp += word
        else:
            num.append(tmp)
            ops.append(word)
            tmp = ''
    num.append(tmp)
    for i in range(len(ops)):
        formula.append(num[i])
        formula.append(ops[i])
    formula.append(num[-1])
    print(formula)

    for order in permutations(list(set(ops))):
        tmp = list(formula)
        for op in order:
            stack = []
            i = 0
            while i < len(tmp):
                if tmp[i] == op:
                    stack.append(operation(stack.pop(), tmp[i + 1], op))
                    i += 2
                else:
                    stack.append(tmp[i])
                    i += 1
            tmp = list(stack)
        answer.append(abs(int(stack.pop())))

    return max(answer)