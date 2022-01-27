def solution(s):
    results = []
    result = ""

    if len(s) == 1:
        answer = 1
        return answer

    for i in range(1, len(s) // 2 + 1):
        count = 1
        cut = s[:i]
        print(cut)
        for j in range(i, len(s), i):
            print(count)
            if s[j:j + i] == cut:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + cut
                cut = s[j:j + i]
                count = 1
                print(result)

        if count == 1:
            count = ""
        result += str(count) + cut
        print(result)
        results.append(len(result))
        result = ""

    answer = min(results)
    return answer