def solution(s):
    answer = []
    s = list(map(str, s[2:-2].split('},{')))
    print(s)
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
    print(s)
    s.sort(key=lambda x: len(x))
    print(s)
    for i in s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{20,111},{111}}"))