def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    tmp = ""
    for id in new_id:
        if id.isalpha() or id.isdigit() or id == "-" or id == "_" or id == ".":
            tmp += id
    new_id = tmp

    tmp = " "
    for id in new_id:
        if id == "." and tmp[-1] == ".":
            continue
        tmp += id
    tmp = tmp[1:]
    new_id = tmp

    if new_id[0] == ".":
        new_id = new_id[1:]

    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:len(new_id) - 1]

    if len(new_id) == 0:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]

    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:len(new_id) - 1]

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    print(new_id)

    return new_id
