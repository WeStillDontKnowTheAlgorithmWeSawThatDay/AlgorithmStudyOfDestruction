def solution(phone_book):
    answer = True
    # phone_book.sort(key=len) # 이렇게 풀면 안됨!
    phone_book.sort()
    
    for idx_phone, phone in enumerate(phone_book):
        if idx_phone == len(phone_book)-1: return answer
        if phone in phone_book[idx_phone+1]:
            if not phone[0] == phone_book[idx_phone+1][0]: continue # 예외처리 ["88", "988"] 인 경우
            return False
    return answer