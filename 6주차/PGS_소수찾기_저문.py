from itertools import product

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    temp = []
    for i in range(1, len(numbers) + 1):
        temp.append(list(product(numbers, repeat=i)))

    # print(temp)

    legend = []
    for i in temp:
        for j in i:
            legend.append(int(''.join(j)))

    legend = list(set(legend))

    for i in legend:
        print(i)
        # t = 0
        for j in range(2, i + 1):
            if i % j == 0 and j != i:
                break
            # t += 1
        if j == i:
            answer += 1

    print(legend)

    return answer