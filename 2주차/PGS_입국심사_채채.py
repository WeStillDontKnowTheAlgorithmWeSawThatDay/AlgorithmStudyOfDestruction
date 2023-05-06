def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    while(start<=end):
        mid = (start + end) // 2
        people = calculate(times,mid)
        if(people >= n):
            answer = mid
            end = mid -1
        else:
            start = mid +1
    return answer
        
def calculate(times,targetTime):
    sum = 0
    for time in times:
        sum += targetTime//time
    print(sum)
    return sum

