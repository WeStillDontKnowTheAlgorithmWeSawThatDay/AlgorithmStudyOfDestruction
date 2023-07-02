x = input()

if "0" not in x:
    print(-1)
else:
    sum = 0
    for x_i in x:
        sum += int(x_i)
    if(sum % 3 != 0):
        print(-1)
    else:
        x_sorted = sorted(x, reverse=True)
        print("".join(x_sorted))
    
