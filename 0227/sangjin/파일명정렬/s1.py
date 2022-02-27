def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        check_head = 1
        for i in range(len(file)):
            if check_head and not file[i].isdigit():
                head += file[i]
            elif file[i].isdigit():
                check_head = 0
                number += file[i]
            else:
                tail = file[i:]
                break
        answer.append([head, number, tail])

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(a) for a in answer]
    return answer