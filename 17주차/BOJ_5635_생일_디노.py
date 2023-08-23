n = int(input())
arr = []
for _ in range(n):
    name, day, month, year = map(str, input().split())
    arr.append([name, int(day), int(month), int(year)])

arr.sort(key=lambda x: (x[3], x[2], x[1]))
print(arr[-1][0])
print(arr[0][0])
