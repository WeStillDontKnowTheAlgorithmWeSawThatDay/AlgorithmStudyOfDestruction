X = int(input()) - 1

st, end = 1, 10000000
now_cnt = 0

while st <= end:
    mid = (st + end) // 2
    if mid * (mid + 1) // 2 <= X:
        st = mid + 1
        now_cnt = mid
    else:
        end = mid - 1

now_sum = now_cnt * (now_cnt + 1) // 2
# print("now_cnt = ", now_cnt, "now_sum = ", now_sum)

if now_cnt % 2 == 0:
    le, ri = now_cnt + 1 - (X - now_sum), 1 + (X - now_sum)

else:
    le, ri = 1 + (X - now_sum), now_cnt + 1 - (X - now_sum)

print(le, end="")
print("/", end="")
print(ri, end="")

'''
1 1                 1

1 2 오 1             2
2 1 왼 1 오 -1        3

3 1 왼 1             4
2 2 왼 -1 오 1        5
1 3 왼 -1 오 1        6

1 4 오 1             7
2 3 왼 1 오 -1        8
3 2 왼 1 오 -1        9
4 1 왼 1 오 -1        10

5 1 왼 1             11
4 2 왼 -1 오 1        12
3 3 왼 -1 오 1        13
2 4 왼 -1 오 1        14
1 5 왼 -1 오 1        15
'''

'''
시간 초과 나는 풀이

cnt, now_cnt = 0, 0
tri = 1  # 왼 0 오 1
le, ri = 1, 1

for _ in range(X - 1):
    # print("le = ", le, "ri = ", ri)
    if cnt == now_cnt:
        cnt += 1
        now_cnt = 0
        if tri == 0:
            le += 1
            tri = 1
            continue
        if tri == 1:
            ri += 1
            tri = 0
            continue

    if tri == 0:
        le += 1
        ri -= 1
    elif tri == 1:
        le -= 1
        ri += 1

    now_cnt += 1

print(le, end="")
print("/", end="")
print(ri, end="")
'''
