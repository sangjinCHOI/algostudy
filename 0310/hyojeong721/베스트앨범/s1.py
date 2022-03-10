def solution(genres, plays):
    answer = []
    total = {}
    music = {}
    for i in range(len(genres)):
        # 총 장르 순서 따지기 위한 total dic만들기
        if genres[i] not in total:
            total[genres[i]] = plays[i]
        else:
            total[genres[i]] += plays[i]
        # 장르별 dic 만들기
        if genres[i] not in music:
            music[genres[i]] = [(i, plays[i])]
        else:
            music[genres[i]] = music[genres[i]] + [(i, plays[i])]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for genre in total:
        if len(music[genre[0]]) == 1:
            answer.append(music[genre[0]][0][0])
        else:
            lst = sorted(music[genre[0]], key=lambda x:x[1], reverse=True)
            answer.append(lst[0][0])
            answer.append(lst[1][0])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [800, 600, 150, 800, 2500]
# [4, 1, 3, 0]
print(solution(genres, plays))