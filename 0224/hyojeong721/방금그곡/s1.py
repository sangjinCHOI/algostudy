# 20, 21, 27, 28 실패
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
def code_change(music_):
    # music_ = music_.replace('E#', 'e')
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')
    return music_

def solution(m, musicinfos):
    listen = code_change(m)
    answer = {}
    for music in musicinfos:
        play = music.split(",")
        time = 60*(int(play[1][:2]) - int(play[0][:2])) + int(play[1][3:]) - int(play[0][3:])
        code = code_change(play[3])
        temp = ""
        # 재생코드만들기
        i = 0
        while len(temp) < time:
            temp += code[i]
            if i == len(code)-1:
                i = 0
            else:
                i += 1
        if listen in temp:
            answer[play[2]] = (temp, code, time)
    res = ""
    if len(answer) > 1:
        for k, v in answer.items():
            if res == "":
                res = k
            else:
                if answer[res][2] < answer[k][2]:
                    res = k
    elif len(answer) == 1:
        res = list(answer.keys())[0]
    else:
        res = "(None)"
    return res

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))