# **

N = int(input())
values = list(map(int, input().split()))

left, right = 0, N - 1
answer = abs(values[left] + values[right])
ptr1, ptr2 = left, right

while left < right:
    sum = values[left] + values[right]
    
    if abs(sum) < answer:
        answer = abs(sum)
        ptr1, ptr2 = left, right
        if answer == 0:
            break
    
    if sum < 0:
        left += 1
    else:
        right -= 1

print(values[ptr1], values[ptr2])
