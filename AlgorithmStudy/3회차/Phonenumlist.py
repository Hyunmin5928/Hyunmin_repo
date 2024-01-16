def solution(phone_book):
    phone_hash = {}
    
    for phone_num in phone_book:
        phone_hash[phone_num] = 1

    for phone_num in phone_book:
        tmp = ""
        for num in phone_num[:-1]:
            tmp += num
            if tmp in phone_hash:
                return False
    return True
