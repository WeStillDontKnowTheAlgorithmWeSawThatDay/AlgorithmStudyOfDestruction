N = int(input())

ansList = []
for i in range(N, 0, -1):
    ansList.append(" " * (N - i) + "*" * (2 * i - 1))

for a in ansList:
    print(a)
for i in range(len(ansList) - 2, -1, -1):
    print(ansList[i])
