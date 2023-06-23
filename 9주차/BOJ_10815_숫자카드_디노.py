N = int(input())
numCards = list(map(int, input().split()))
numCards.sort()

M = int(input())
compCards = list(map(int, input().split()))

ansList = []

# -10 2 3 6 10

for i in range(len(compCards)):
    compareNum = compCards[i]
    le, ri = 0, N - 1

    while le <= ri:
        # print(le, ri)
        mid = (le + ri) // 2
        midNum = numCards[mid]

        # print(mid, midNum)

        if compareNum > midNum:
            le = mid + 1
            continue
        if compareNum < midNum:
            ri = mid -1
            continue

        if compareNum == midNum:
            ansList.append(1)
            # print(midNum)
            break
    if len(ansList) != i+1:
        ansList.append(0)

print(*ansList)


'''
예전에 풀었던 거 (이분 탐색 안쓴 버전)

import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int,input().split()))
check = {}
for i in cards:
    check[i] = 1 

M = int(input())
numbers = list(map(int,input().split()))

for i in numbers:
    if i in check:
        print(1, end=' ')
    else:
        print(0, end=' ')                
'''
