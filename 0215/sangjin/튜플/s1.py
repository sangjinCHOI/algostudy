def solution(s):
    s = s[1: -1].replace("},{", "}{")
    answer = []
    tmp = []
    num = ""

    for w in s:
        if w.isdigit():
            num += w
        elif w == ",":
            tmp.append(int(num))
            num = ""
        elif w == "}":
            tmp.append(int(num))
            answer.append(tmp)
            tmp = []
            num = ""
    answer.sort(key=lambda x: len(x))

    if len(answer) > 1:
        for i in range(len(answer) - 1):
            tmp = answer.pop(i + 1)
            for j in range(len(answer[i])):
                tmp.remove(answer[i][j])
            answer.insert(i + 1, answer[i] + tmp)

    return answer[-1]