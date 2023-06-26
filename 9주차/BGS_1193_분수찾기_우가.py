index = int(input())

n = 1

while (n * n + n) / 2 < index:
    n += 1

group = int((n * n + n) / 2) - index
if n % 2 == 0:
    y = group + 1
    x = n - y + 1
elif n % 2 != 0:
    x = group + 1
    y = n - x + 1

print(f'{x}/{y}')
