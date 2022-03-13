def solution(answers):
    student_1 = list('12345' * 2000)
    student_2 = list('21232425' * 1250)
    student_3 = list('3311224455' * 1000)
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count = []

    for i in range(len(answers)):
        if answers[i] == int(student_1[i]):
            count_1 += 1
        if answers[i] == int(student_2[i]):
            count_2 += 1
        if answers[i] == int(student_3[i]):
            count_3 += 1

    best = max([count_1, count_2, count_3])

    answer = []
    if best == count_1:
        answer.append(1)
    if best == count_2:
        answer.append(2)
    if best == count_3:
        answer.append(3)

    return answer