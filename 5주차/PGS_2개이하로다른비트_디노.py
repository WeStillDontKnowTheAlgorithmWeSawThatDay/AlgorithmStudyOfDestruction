# def solution(numbers):
#     answer = []
#     for x in numbers:
#         if x % 2 == 0:
#             answer.append(x + 1)
#         else:
#             binary = '0' + bin(x)[2:]
#             last_zero = binary.rfind('0')
#             flipped_binary = binary[:last_zero] + '10' + binary[last_zero + 2:]
#             answer.append(int(flipped_binary, 2))
#     return answer

def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
            continue
        # print(bin(n))
        # print(len(bin(n)))
        bn = bin(n)

        for i in range(len(bin(n)) - 1, 1, -1):
            # print(i)
            # print(bn[i-1], bn[i])
            if bn[i - 1] == '0' and bn[i] == '1':
                nbn = ''

                for j in range(len(bn)):
                    if j == i - 1:
                        nbn += '1'
                    elif j == i:
                        nbn += '0'
                    else:
                        nbn += bn[j]
                answer.append(int(nbn, 2))
                break
            if i == 2:
                nbn = '0b10' + bn[3:]
                # print(nbn)
                answer.append(int(nbn, 2))

    return answer

# def solution(numbers):
#     answer = []
#     dic = {}
#     for num in numbers:
#         if num in dic:
#             answer.append(dic[num])
#             continue
#         t_num = num
#         while True:
#             if num % 2 == 0:
#                 dic[num] = num + 1
#                 answer.append(num + 1)
#                 break
#             t_num += 1
#             cmp = bin(num ^ t_num)
#             cnt = 0
#             for c in cmp:
#                 if c == '1':
#                     cnt += 1
#             if cnt <= 2:
#                 dic[num] = t_num
#                 answer.append(t_num)
#                 break

#     return answer