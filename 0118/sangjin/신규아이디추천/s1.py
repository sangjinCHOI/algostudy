def solution(new_id):
    # 1
    step1 = ''
    for letter in new_id:
        if 65 <= ord(letter) <= 90:
            letter = chr(ord(letter) + 32)
        step1 += letter
    # 2
    step2 = ''
    for letter in step1:
        if letter.isalpha() or letter.isdigit() or letter in ('-', '_', '.'):
            step2 += letter

    # 3
    step3 = ''
    for idx in range(len(step2) - 1):
        if step2[idx] == '.' and step2[idx + 1] == '.':
            pass
        else:
            step3 += step2[idx]
    step3 += step2[-1]

    # 4
    step4 = ''
    if step3 and step3[0] == '.':
        step4 = step3[1:]
    else:
        step4 = step3

    if step4 and step4[-1] == '.':
        step4 = step4[:-1]

    # 5
    step5 = step4
    if len(step5) == 0:
        step5 += 'a'

    # 6
    if len(step5) >= 16:
        step6 = step5[0:15]
    else:
        step6 = step5

    if step6[-1] == '.':
        step6 = step6[:-1]

    # 7
    step7 = step6
    while len(step7) <= 2:
        step7 += step7[-1]

    answer = step7
    return answer