def solution(new_id):
    answer = ''
    # 소문자 치환
    new_id = new_id.lower()
    # 제한 ㅜ문자이외의 모든 문자 제거
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 마침표 두개 이상이면 하나로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 처음이나 끝에 위치한 마침표 제거
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 빈문자열이면 'a' 대입
    if answer == '':
        answer = 'a'
    # 16자 이상이면 15개로 마침표잇으면 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 2자 이하면 마지막문자 추가해서 3될때까지
    while len(answer) < 3:
        answer += answer[-1]
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "123_.def"
print(solution(new_id))
