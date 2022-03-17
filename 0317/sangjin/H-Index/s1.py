def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            answer = len(citations)-i
            return answer
    return 0