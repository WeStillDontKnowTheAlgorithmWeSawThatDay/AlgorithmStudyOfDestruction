# pypy에서 통과
# 내 로직 안틀렸어
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])

ans = 0
chk = [i for i in range(V + 1)]

for a, b, c in graph:
    if chk[a] != chk[b]:
        parent = chk[b]
        ans += c
        for i in range(len(chk)):
            if chk[i] == parent:
                chk[i] = chk[a]

print(ans)

# import sys
#
#
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
#
# graph = [list(map(int, input().split())) for _ in range(E)]
#
# ans = 0
#
# graph.sort(key=lambda x: x[2])
#
# chk = [i for i in range(V + 1)]
#
# for a, b, c in graph:
#
#     # if a == 2 and b == 3:
#     #     print(chk)
#     # print(a, b, chk[a], chk[b])
#     if chk[a] != chk[b]:
#         parent = chk[b]
#         ans += c
#         # print("chk[4] = ", chk[4])
#         # print("len(chk)", len(chk))
#         # print("chk[b]", chk[b])
#         for i in range(len(chk)):
#             # print("i = ", i, "chk[i]", chk[i], "chk[b]= ", chk[b])
#             if chk[i] == parent:
#                 # print(i, "chk[i] = ", chk[i])
#                 chk[i] = chk[a]
#     # if a == 2 and b == 3:
#     #     print(chk)
#     # print()
#
# print(ans)
