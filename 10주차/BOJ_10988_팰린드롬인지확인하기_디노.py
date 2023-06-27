l = input()
for i in range(len(l)):
    if l[i] != l[len(l) - 1 - i]:
        print(0)
        exit()

print(1)
기