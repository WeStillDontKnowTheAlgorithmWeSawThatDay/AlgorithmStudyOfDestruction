word = input()

idx = 0
cnt = 0

while idx < len(word):
    # print("idx = ", idx, "w =", word[idx])
    if word[idx] == "c":
        if idx + 1 <= len(word) - 1 and (word[idx + 1] == "=" or word[idx + 1] == "-"):
            cnt += 1
            idx += 2
            continue
    if word[idx] == "d":
        if idx + 1 <= len(word) - 1 and word[idx + 1] == "-":
            cnt += 1
            idx += 2
            continue
        if idx + 2 <= len(word) - 1 and word[idx + 1] == "z" and word[idx + 2] == "=":
            cnt += 1
            idx += 3
            # print("Dsa")
            continue
    if word[idx] == "l":
        if idx + 1 <= len(word) - 1 and word[idx + 1] == "j":
            cnt += 1
            idx += 2
            continue
    if word[idx] == "n":
        if idx + 1 <= len(word) - 1 and word[idx + 1] == "j":
            cnt += 1
            idx += 2
            continue
    if word[idx] == "s":
        if idx + 1 <= len(word) - 1 and word[idx + 1] == "=":
            cnt += 1
            idx += 2
            continue
    if word[idx] == "z":
        if idx + 1 <= len(word) - 1 and word[idx + 1] == "=":
            cnt += 1
            idx += 2
            # print("zzz")
            continue
    idx += 1
    cnt += 1

print(cnt)
