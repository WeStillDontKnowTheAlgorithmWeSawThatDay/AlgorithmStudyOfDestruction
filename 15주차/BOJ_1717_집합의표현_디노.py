import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def find(target):
    if target == arr[target]:
        return target

    arr[target] = find(arr[target])
    return arr[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        arr[b] = a
    else:
        arr[a] = b


n, m = map(int, input().split())
arr = [x for x in range(n + 1)]

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)

    if q == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = []
#
# for _ in range(m):
#     q, a, b = map(int, input().split())
#
#     # print("start", q, a, b, "----------------")
#     if q == 0:
#         x, y = [], []
#         for ar in arr:
#             # print("now = ", ar)
#             if a in ar and b not in ar:
#                 # print("??", ar)
#                 # arr.remove(ar)
#                 x = ar
#             if b in ar and a not in ar:
#                 # print("??", ar)
#                 # arr.remove(ar)
#                 y = ar
#
#         if x == [] and y != []:
#             # print("sdads",arr, y)
#             arr.remove(y)
#             y.append(a)
#             arr.append(y)
#         if x != [] and y == []:
#             # print("sdads", arr, x)
#             arr.remove(x)
#             x.append(b)
#             arr.append(x)
#         if x == [] and y == [] and a != b:
#             arr.append([a, b])
#         if x != [] and y != []:
#             arr.remove(x)
#             arr.remove(y)
#             arr.append(x + y)
#
#     if q == 1:
#         tri = 0
#         for ar in arr:
#             if a in ar and b in ar:
#                 print("YES")
#                 tri = 1
#         if tri == 0:
#             print("NO")
# print(" result", arr, "---------------")

# n, m = map(int, input().split())
# arr = [[x] for x in range(n + 1)]
# # print(arr)
# #
# # arr.remove([1])
# # print(arr)
# for _ in range(m):
#     q, a, b = map(int, input().split())
#     if q == 0:
#         for ar in arr:
#             if a in ar:
#                 # print(arr, "sdsad", ar)
#                 x = ar
#                 arr.remove(ar)
#             if a == b:
#                 continue
#             if b in ar:
#                 # print(arr, "dssada",ar)
#                 y = ar
#                 arr.remove(ar)
#         tmp = x + y
#         arr.append(tmp)
#
#     if q == 1:
#         tri = 0
#         for ar in arr:
#             if a in ar and b in ar:
#                 tri = 1
#         if tri == 1:
#             print("YES")
#         else:
#             print("NO")
#     # print(arr)
