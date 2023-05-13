def solution(name):
    answer = 0
    
    a = ""
    for n in range(2):
        a += name

    count, countA, countB = 0, 0, 0
    length = len(name)
    for i in range(length):
        if a[i + length] != "A":
            현재마이너스에이 = ord(a[i + length]) - ord("A")
            제트마이너스현재 = ord("Z") - ord(a[i + length]) + 1
            count += min(현재마이너스에이, 제트마이너스현재)
            countA = max(countA, i)

            
    abc = ""
    for i in range(1, len(name)):
        abc+=name[i]
    
    k = "".join(reversed(abc))
    for i in range(len(k)):
        if a[i] != "A":
            countB = max(countB, i + 1)

    #48.1점 3일박음
    return count + min(countA, countB)
