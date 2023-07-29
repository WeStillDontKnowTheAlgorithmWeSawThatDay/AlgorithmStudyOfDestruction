n = int(input())

neg, zero, pos = [], [], []
for _ in range(n):
    num = int(input())
    if num == 0:
        zero.append(num)
    elif num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)

pos.sort()
neg.sort(reverse=True)

pos_sum, neg_sum = 0, 0
neg_remain = -1001

while pos:
    num1, num2 = 0, 0
    if len(pos) == 1:
        num1 = pos.pop()
        pos_sum += num1
    
    if len(pos) >= 2:
        num1 = pos.pop()
        num2 = pos.pop()
        if num2 == 1:
            pos_sum += (num1 + num2)
        else:
            pos_sum += (num1 * num2)

while neg:
    num1, num2 = 0, 0
    if len(neg) == 1:
        neg_remain = neg.pop()
    
    if len(neg) >= 2:
        neg_sum += (neg.pop() * neg.pop())

if not zero and neg_remain != -1001: # 남은 음수가 있음
    print(pos_sum + neg_sum + neg_remain)
else:
    print(pos_sum + neg_sum)