def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


num_card = int(input())
card_list = list(map(int, input().strip().split()))
num = int(input())
num_list = list(map(int, input().strip().split()))

card_list.sort()

for i in range(len(num_list)):
    if binary_search(num_list[i], card_list) is not None:
        print("1", end=' ')
    else:
        print("0", end=' ')
