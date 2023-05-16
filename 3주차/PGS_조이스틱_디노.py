def find(words, cursor, name, cnt):
    name[cursor + 1]

def solution(name):
    answer = 0
    min_move = len(name) - 1

    for i, w in enumerate(name):
        answer += min(ord(w) - ord('A'), ord('Z') - ord(w) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    answer += min_move
    return answer

# #     alphabet = [chr(ord('A')+i) for i in range(len(name))]
# #     words = ['A' for _ in range(len(name))]
# #     cursor = 0
# #     answer = 0

# #     return answer

#     li = [5, 6, 7, 8, 9]

#     li2 = list(combinations(li), 3)

#     ds = {1,2,3}
#     print(sum(ds))

