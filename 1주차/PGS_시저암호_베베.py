def solution(s: str, n: int):
    input_chrs = list(s)

    new_chrs = list()
    for i in input_chrs:
        if i == " ":
            new_chrs.append(" ")
        elif i.isupper():
            new_chr = chr((ord(i) - 65 + n) % 26 + 65)
            new_chrs.append(new_chr)
        elif i.islower():
            new_chr = chr((ord(i) - 97 + n) % 26 + 97)
            new_chrs.append(new_chr)
        else:
            new_chrs.append(i)

    return "".join(new_chrs)