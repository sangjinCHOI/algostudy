def times(expression):
    check = True
    while check:
        for i in range(len(expression)):
            if expression[i] == '*':
                a = ''
                b = ''
                an = 1
                bn = 1
                while expression[i+bn].isdigit():
                    b += expression[i+bn]
                    if i+bn < len(expression)-1:
                        bn += 1
                    else:
                        break
                while expression[i-an].isdigit() and i-an >= 0:
                    a += expression[i-an]
                    an += 1
                a = list(a)
                a.reverse()
                a = ''.join(a)
                expression = expression.replace(a+'*'+b, str(int(a)*int(b)))
                break
        else:
            check = False

    return expression

def minus(expression):
    check = True
    while check:
        for i in range(len(expression)):
            if expression[i] == '-':
                a = ''
                b = ''
                an = 1
                bn = 1
                while expression[i+bn].isdigit():
                    b += expression[i+bn]
                    if i+bn < len(expression)-1:
                        bn += 1
                    else:
                        break
                while expression[i-an].isdigit() and i-an >= 0:
                    a += expression[i-an]
                    an += 1
                a = list(a)
                a.reverse()
                a = ''.join(a)
                expression = expression.replace(a+'-'+b, str(int(a)-int(b)))
                break
        else:
            check = False

    return expression

def plus(expression):
    check = True
    while check:
        for i in range(len(expression)):
            if expression[i] == '+':
                a = ''
                b = ''
                an = 1
                bn = 1
                while expression[i+bn].isdigit():
                    b += expression[i+bn]
                    if i+bn < len(expression)-1:
                        bn += 1
                    else:
                        break
                while expression[i-an].isdigit() and i-an >= 0:
                    a += expression[i-an]
                    an += 1
                a = list(a)
                a.reverse()
                a = ''.join(a)
                expression = expression.replace(a+'+'+b, str(int(a)+int(b)))
                break
        else:
            check = False

    return expression

def solution(expression):
    answer = 0
    answers = []
    answers.append(str(abs(int(plus(minus(times(expression)))))))
    answers.append(str(abs(int(plus(times(minus(expression)))))))
    answers.append(str(abs(int(times(plus(minus(expression)))))))
    answers.append(str(abs(int(times(minus(plus(expression)))))))
    answers.append(str(abs(int(minus(plus(times(expression)))))))
    answers.append(str(abs(int(minus(times(plus(expression)))))))
    answer = max(answers)

    return answer

print(solution("100-200*300-500+20"))