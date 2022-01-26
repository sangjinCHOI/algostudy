def solution(s):
    answer = []
    # 문자열1개짜리는 바로 리턴
    if len(s) == 1:
        return 1

    i = 1
    # 문자열 길이의 2등분한 길이들만 보면 됌!
    while i <= len(s)//2:
        cut_str = []
        # i 단위로 문자 자르기
        for k in range(0, len(s), i):
            if k+i <= len(s):
                cut_str.append(s[k:k+i])
            else:
                cut_str.append(s[k:])

        # 밑에 while문에서 자른 문자열의 결과까지 넣기 위해 임의의 값 추가
        cut_str.append('temp')
        # res에 반복숫자+반복되는문자 저장
        res = ''
        cnt = 1
        temp1 = cut_str.pop(0)

        while cut_str:
            temp2 = cut_str.pop(0)
            # 앞에있는 문자(temp1)랑 현재 문자(temp2)랑 비교 -> 같으면 cnt만 올리고 다음으로
            if temp1 == temp2:
                cnt += 1
            else:
                # 같지 않을때 cnt 1인경우는 1생략 문자만 추가 / 그 이상인 경우에 cnt+문자 같이 추가
                if cnt > 1:
                    res += (str(cnt) + temp1)
                else:
                    res += temp1
                temp1 = temp2
                cnt = 1
        answer.append(len(res))
        i += 1

    return min(answer)

s = "xa"
print('답', solution(s))

