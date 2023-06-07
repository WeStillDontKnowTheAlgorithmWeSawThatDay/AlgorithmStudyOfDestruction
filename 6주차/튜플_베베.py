def solution(s):
    numbers = s[2:-2].split("},{")
    numbers = [number.split(",") for number in numbers]
    numbers.sort(key=lambda x: len(x))

    answer = []
    for number in numbers:
        for n in number:
            if int(n) not in answer:
                answer.append(int(n))
                break

    return answer
