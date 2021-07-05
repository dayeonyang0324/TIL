def solution(phone_book):
    # answer = True
    # for j in range(len(phone_book)):
    #     start = phone_book[j]
    #     for i in range(j+1, len(phone_book)):
    #         if start == phone_book[i][:len(start)] or phone_book[i] == start[:len(phone_book)]:
    #             answer = False
    #             break
    # return answer
    
    # sort를 하면 앞뒤로 포함관계로 정렬된다. ['123', '12345', '234']
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    return True