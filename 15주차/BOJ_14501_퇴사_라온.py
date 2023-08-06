n = int(input())
consults = []
for _ in range(n):
    day, money = map(int, input().split())
    consults.append((day, money))

times = {}
for i, consult in enumerate(consults):
    day, money = consult
    if times.get(i+day+1) == None:
        times[i+day+1] = [(i+1, money)]
    else:
        times[i+day+1].append((i+1, money))

t, start = 1, 1
profit = 0
time_profit = [0]

while t <= n+1:
    days = times.get(t)
    t += 1
    if days == None:
        time_profit.append(profit)
        continue
    max_money = profit
    for day, money in days:
        if day >= start:
            max_money = max(max_money, profit + money)
        if day < start:
            max_money = max(max_money, time_profit[day] + money)
    start = t
    profit = max_money
    time_profit.append(profit)
print(profit)
