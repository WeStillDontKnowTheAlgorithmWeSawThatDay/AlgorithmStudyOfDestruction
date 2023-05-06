# 반복문 한번으로 해결하고픔
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        sec = 0
        for next_price in queue:
            sec += 1
            if price > next_price:
                break
        answer.append(sec)
    return answer