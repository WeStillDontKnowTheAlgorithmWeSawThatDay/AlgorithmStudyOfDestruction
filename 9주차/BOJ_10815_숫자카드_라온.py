N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
user_cards = list(map(int, input().split()))

answer = []

for target in user_cards:
    left, right = 0, len(cards)
    flag = 0
    while left <= right:

        if left >= len(cards):
            break

        mid = (left + right) // 2
        if target == cards[mid]:
            flag = 1
            break

        if target > cards[mid]:
            left = mid + 1
        
        if target < cards[mid]:
            right = mid - 1
    answer.append(flag)
print(*answer)