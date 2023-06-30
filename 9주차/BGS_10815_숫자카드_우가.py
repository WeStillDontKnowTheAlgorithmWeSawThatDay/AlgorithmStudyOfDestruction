def fff():
    input()
    nlist = set(input().split())
    input()
    mlist = input().split()
    answer = ''
    for m in mlist:
        if m in nlist:
            answer += '1 '
        else:
            answer += '0 '
    print(answer)

fff()
