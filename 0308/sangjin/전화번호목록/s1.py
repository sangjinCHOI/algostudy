def solution(phone_book):
    phone_book.sort(key=lambda x: (x, len(x)))

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break
    else:
        answer = True

    return answer