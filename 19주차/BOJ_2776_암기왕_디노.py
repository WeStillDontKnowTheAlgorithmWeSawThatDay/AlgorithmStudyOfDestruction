# dictionary 사용

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = set(map(int, input().split()))

    M = int(input())
    note2 = list(map(int, input().split()))

    for mm in note2:
        if mm in note1:
            print(1)
        else:
            print(0)



import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))

    M = int(input())
    note2 = list(map(int, input().split()))

    for mm in note2:
        if mm in note1:
            print(1)
        else:
            print(0)

# 이분탐색 사용

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))

    note1.sort()

    M = int(input())
    note2 = list(map(int, input().split()))

    for mm in note2:
        le, ri = 0, len(note1) - 1
        tri = 0
        while le <= ri:
            mid = (le + ri) // 2
            if mm == note1[mid]:
                tri = 1
                break
            if mm < note1[mid]:
                ri = mid - 1
                continue
            if mm > note1[mid]:
                le = mid + 1
        if tri == 1:
            print(1)
        else:
            print(0)
