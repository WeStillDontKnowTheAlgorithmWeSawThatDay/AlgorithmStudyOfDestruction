N = int(input())

num, sum = 1, 0
while True:
    if sum + num < N:
        sum += num
        num += 1
    
    if sum + num == N:
        if num%2 == 1:
            print(str(1) + "/" + str(num))
        if num%2 == 0:
            print(str(num) + "/" + str(1))
        break

    if sum + num > N:
        diff = N - sum
        if num%2 == 1:
            print(str(num-diff+1) + "/" + str(diff))
        if num%2 == 0:
            print(str(diff) + "/" + str(num-diff+1))
        break