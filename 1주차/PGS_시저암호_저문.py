def solution(s, n):
    answer = ""

    for letter in s:
        if letter == " ":
            answer += letter
            continue
        elif 65 <= ord(letter) <= 90:
            if ord(letter) + n > 90:
                answer += chr(((ord(letter) + n) - 90) + 64)
                continue
        elif 97 <= ord(letter) <= 122:
            if ord(letter) + n > 122:
                answer += chr(((ord(letter) + n) - 122) + 96)
                continue
        answer += chr(ord(letter) + n)

    return answer