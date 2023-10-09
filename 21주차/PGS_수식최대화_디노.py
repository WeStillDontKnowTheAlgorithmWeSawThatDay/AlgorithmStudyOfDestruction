from itertools import permutations


def solution(expression):
    answer = 0
    tmpp = []

    num = 0
    for i in range(len(expression)):
        if expression[i].isdigit():
            num = num * 10 + int(expression[i])
        else:
            tmpp.append(num)
            tmpp.append(expression[i])
            num = 0

    tmpp.append(num)
    # print(tmp)

    li = list(permutations(["-", "+", "*"], 3))

    for l in li:
        tmp = tmpp
        for i in range(3):
            j = 0

            while j < len(tmp):
                # print(l[i], tmp[j])
                if tmp[j] == l[i]:
                    if l[i] == "*":

                        tmp = tmp[:j - 1] + [(tmp[j - 1] * tmp[j + 1])] + tmp[j + 2:]
                        j = 0
                        # break
                        continue
                    if l[i] == "-":
                        # print(tmp[j-1], tmp[j+1])
                        tmp = tmp[:j - 1] + [(tmp[j - 1] - tmp[j + 1])] + tmp[j + 2:]
                        j = 0
                        # break
                        continue
                    if l[i] == "+":
                        # print(tmp[j-1], tmp[j+1])
                        tmp = tmp[:j - 1] + [(tmp[j - 1] + tmp[j + 1])] + tmp[j + 2:]
                        j = 0
                        # break
                        continue
                j += 1
        # print(tmp)

        answer = max(answer, abs(tmp[0]))

    # print(li)

    return answer
