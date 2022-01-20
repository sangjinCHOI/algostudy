def solution(new_id):
    new_id = new_id.lower()
    check = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    new_id2 = ''
    for i in new_id:
        if i in check:
            new_id2 += i
    new_id3 = ''
    for i in range(len(new_id2)):
        if new_id2[i] == '.':
            if new_id2[i-1] == '.':
                continue
        new_id3 += new_id2[i]

    if new_id3 and new_id3[0] == '.':
        new_id3 = new_id3[1:]
    if new_id3 and new_id3[-1] == '.':
        new_id3 = new_id3[:-1]
    if not new_id3:
        new_id3 = 'a'
    if len(new_id3) >= 16:
        new_id3 = new_id3[:15]
    if len(new_id3) <= 2:
        while len(new_id3) <= 2:
            new_id3 += new_id3[-1]
    if new_id3 and new_id3[0] == '.':
        new_id3 = new_id3[1:]
    if new_id3 and new_id3[-1] == '.':
        new_id3 = new_id3[:-1]
    answer = new_id3
    return answer

print(solution("abcdefghijklmn.p"))