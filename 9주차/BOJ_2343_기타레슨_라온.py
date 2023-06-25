# 88퍼에서 틀림 ㅠ 이유 모르겠 .. 
N, M = map(int, input().split())
videos = list(map(int, input().split()))

# N, M = 9, 3
# videos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(mid):
    i = M - 1
    sum = 0
    for video in videos:
        if video > mid:
            return True
        if sum + video > mid:
            i -= 1
            sum = 0
        sum += video
        
    if i < 0:
        return False
    if i >= 0 :
        return True
    
left, right = max(videos), sum(videos)
while left <= right:
    mid = (left + right) // 2
    if func(mid) and left == right:
        print(mid)
        break
      
    if func(mid):
        right = mid - 1

    if not func(mid):
        left = mid + 1
        if(left > right):
            print(left)
            break
