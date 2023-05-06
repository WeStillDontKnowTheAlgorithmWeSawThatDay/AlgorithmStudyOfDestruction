def solution(n):
    store = []
    for i in range(n+1):
        if i == 0:
            store.append(0)
        elif i == 1:
            store.append(1)
        else:
            store.append(store[i-1]+store[i-2])            
    return (store[n-2] + store[n-1]) % 1234567