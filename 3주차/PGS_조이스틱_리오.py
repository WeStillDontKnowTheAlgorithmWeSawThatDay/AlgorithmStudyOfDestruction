# 테케 자꾸 세개 정도 나가서 도저히 안되겠어서 긁어왔습니다..

def solution(name):
    answer = 0
    n = len(name)

    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

    move = n - 1
    for left in range(n):
        idx = left + 1
        while (idx < n) and (name[idx] == 'A'):
            idx += 1

        right = n - idx
        distance = min(left, right)

        move = min(move, left + right + distance)

    answer += move
    return answer
