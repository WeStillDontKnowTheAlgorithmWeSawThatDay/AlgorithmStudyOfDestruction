S = input()
dic = {}

for i in range(len(S)):
    st = ""
    for j in range(i, len(S)):
        st += S[j]
        if st not in dic:
            dic[st] = 1

print(len(dic))