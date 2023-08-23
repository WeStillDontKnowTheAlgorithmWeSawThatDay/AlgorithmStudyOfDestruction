# 메모리 초과는 쫌 .. 

n = int(input())
small = [0, 0, 0]
big = [0, 0, 0]

for _ in range(n):
    line = list(map(int, input().split()))
    small = [line[0] + min(small[:2]), line[1] +  min(small), line[2] + min(small[1:])]
    big = [line[0] + max(big[:2]), line[1] +  max(big), line[2] + max(big[1:])]

print(max(big), min(small))

# lines = [list(map(int, input().split())) for _ in range(n)]
# lines1 =copy.deepcopy(lines)
# lines = lines[::-1]
# lines1 = lines1[::-1]

# # for line in lines:
# #     print(line)
# # print("=========")

# for i, line in enumerate(lines):
#     if i == 0:  continue
#     for j, point in enumerate(line):
#         if j == 0:
#             lines[i][j] = lines[i][j] + max(lines[i-1][j], lines[i-1][j+1])
#             lines1[i][j] = lines1[i][j] + min(lines1[i-1][j], lines1[i-1][j+1])
#         elif j == 1:
#             lines[i][j] = lines[i][j] + max(lines[i-1][j-1], lines[i-1][1], lines[i-1][j+1])
#             lines1[i][j] = lines1[i][j] + min(lines1[i-1][j-1], lines1[i-1][1], lines1[i-1][j+1])
#         elif j == 2:
#             lines[i][j] = lines[i][j] + max(lines[i-1][j-1], lines[i-1][j])
#             lines1[i][j] = lines1[i][j] + min(lines1[i-1][j-1], lines1[i-1][j])

# # print(lines)
# # print(lines1)
# print(max(lines[-1]), min(lines1[-1]))