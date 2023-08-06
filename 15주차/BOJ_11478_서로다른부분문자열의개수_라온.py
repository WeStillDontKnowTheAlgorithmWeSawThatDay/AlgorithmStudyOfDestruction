s = list(input())
strings = set()
for n in range(len(s)):
    for i in range(len(s)-n):
        strings.add(''.join(s[i:i+n+1]))
print(len(strings))