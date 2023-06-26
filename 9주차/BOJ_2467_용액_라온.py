N = int(input())
values = list(map(int, input().split()))

left, right = 0, len(values) - 1
while left < right:
    mid = (left + right) // 2

    sum = values[left] + values[right]
    
    if sum 
