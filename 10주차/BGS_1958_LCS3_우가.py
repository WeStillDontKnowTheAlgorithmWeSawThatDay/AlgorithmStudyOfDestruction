arr = []
for i in range(3):
    arr.append(input())

arr = sorted(arr, key=lambda x : len(x))

answer = []
temp = ''
for te in arr[0]:
    temp += te
    if temp in arr[1] and temp in arr[2]:
        answer.append(temp)
for i in range(1, len(arr[0])):
    temp += arr[0][i]
    if temp in arr[1] and temp in arr[2]:
        answer.append(temp)

print(answer[len(answer)-1])