def search(num, n):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        # print(l, r, mid)
        if num == note1[mid]:
            return 1
        
        if l == r and num != note1[mid]:
            return 0

        if num > note1[mid]:
            l = mid + 1
        
        elif num < note1[mid]:
            r = mid
    return 0

t = int(input())
for i in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    # print(note1, note2)

    for i in range(m):
        # print("target: ", note2[i])
        # print("----answer: ", search(note2[i], n), "----")
        print(search(note2[i], n))
