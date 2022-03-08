def solution(phone_book):  ## 효율성 3,4 걸림
    phone_book = sorted(phone_book, key=lambda x: len(x))  # 문자길이순 정렬
    answer = True
    for i, phone1 in enumerate(phone_book):
        hash_map = {}
        for phone2 in phone_book[i+1:]:  # 비교대상을 제외한 나머지들
            hash_map[phone2[:len(phone1)]] = phone2  # key= 비교 대상 길이만큼 잘라넣기
        if phone1 in hash_map:
            answer = False
            break
    return answer

def solution(phone_book): # 효율성 3, 4 걸림
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False

    return True


phone_book = ["12","567", "123","1235","88"]
print(solution(phone_book))


pb1 = ["119", "97674223", "1195524421"]
print(solution(pb1))
pb2 = ["123","456","789"]
print(solution(pb2))
pb3 = ["12","123","1235","567","88"]
print(solution(pb3))