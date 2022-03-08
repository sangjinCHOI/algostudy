def solution(phone_book):  # 효율성3,4에서 걸림
    # hash_book = dict.fromkeys(phone_book, 1)
    for number in phone_book:
        temp = ''
        for t in number:
            temp += t
            if temp in phone_book and temp != number:
                return False
    return True

def solution(phone_book):
    hash_book = dict.fromkeys(phone_book, 1)
    for number in phone_book:
        temp = ''
        for t in number:
            temp += t
            if temp in hash_book and temp != number:
                return False
    return True


pb1 = ["119", "97674223", "1195524421"]
print(solution(pb1))
pb2 = ["123", "456", "789"]
print(solution(pb2))
pb3 = ["12", "123", "1235", "567", "88"]
print(solution(pb3))