num = 6;
def solution(num):
    change = num

    count = 0;
    if(num == 1):
        return 0
    else:
        while change != 1:
            if(count == 500):
                break
            if(change % 2 == 0):
                change = change / 2
                count += 1
            else:
                change = (change * 3) + 1
                count += 1

    if(count >= 500):
        return -1;
    return count

print(solution(6))