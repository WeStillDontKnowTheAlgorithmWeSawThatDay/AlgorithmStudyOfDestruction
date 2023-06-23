# 책 풀이
# def solution(phone_book):
#     headers = {}

#     for phone_number in phone_book:
#         headers[phone_number] = 1

#     for phone_number in phone_book:
#         header = ''
#         for number in phone_number:
#             header += number
#             if header in headers and header != phone_number:
#                 return False

#     return True

# 함수 이용한 풀이
def solution(phone_book):
    phone_book.sort()
    # print(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1): return False

    return True

# def compare(long, short):
#     for i in range(len(long)- len(short)):
#         for j in range(len(short)):
#             if short[j] != long[i+j]:
#                 break
#             if j == len(short)-1:
#                 return False
#     return True

# def solution(phone_book):
#     answer = True
#     phone_book.sort()

#     # print(phone_book)
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if compare(phone_book[j], phone_book[i]) == False:
#                 return False

#     return answer