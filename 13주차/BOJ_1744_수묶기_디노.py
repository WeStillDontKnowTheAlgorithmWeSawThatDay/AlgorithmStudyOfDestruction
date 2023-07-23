N = int(input())

ans = 0

plus, minus = [], []
for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()

# if len(minus) % 2 == 0:
i = 0
while i < len(minus) - 1:
    ans += minus[i] * minus[i + 1]
    i += 2

if len(minus) % 2 == 1:
    ans += minus[len(minus) - 1]

while len(plus) > 0 and plus[len(plus)-1] == 1:
    ans += 1
    plus.pop()

i = 0
while i < len(plus) - 1:
    if plus[i] == 1:
        ans += 1
        i += 1
        continue

    ans += plus[i] * plus[i + 1]
    i += 2

if len(plus) % 2 == 1:
    ans += plus[len(plus) - 1]

print(ans)
