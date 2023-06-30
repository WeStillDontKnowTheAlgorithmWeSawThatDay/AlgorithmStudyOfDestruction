N, M = map(int, input().split())
lecList = list(map(int, input().split()))

le, ri = sum(lecList) // M, sum(lecList)

ansList = []
while le <= ri:
    mid = (le + ri) // 2

    videoCnt = 1
    videoLen = 0
    tri = 0
    # print(mid)
    for lec in lecList:
        if lec > mid:
            tri = 1
            break
        if videoLen + lec > mid:
            videoCnt += 1
            videoLen = lec
        else:
            videoLen += lec
        # print(videoCnt, videoLen)

    if videoCnt <= M and tri != 1:
        ansList.append(mid)
        ri = mid - 1
    else:
        le = mid + 1

print(min(ansList))

#  애초에 강의 중에 mid보다 큰 값이 있으면 불가능하다
