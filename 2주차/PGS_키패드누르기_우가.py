def solution(numbers, hand):
    points = {
        1 : [-1, 1],
        2 : [0, 1],
        3 : [1, 1],
        4 : [-1, 0],
        5 : [0, 0],
        6 : [1, 0],
        7 : [-1, -1],
        8 : [0, -1],
        9 : [1, -1],
        0 : [0, -2],
        99 : [-1, -2],
        100 : [1, -2]
    }
    left = [1, 4, 7]
    middle = [2, 5, 8, 0]
    right = [3, 6, 9]
    answer = ''
    lefthand = 99
    righthand = 100
    for num in numbers:
        if(num in left):
            lefthand = num
            answer += 'L'
        if(num in right):
            righthand = num
            answer += 'R'
        if(num in middle):
            winner = whoWin(points[num], points[lefthand], points[righthand], hand)
            answer += winner
            if(winner == "R"):
                righthand = num
            else:
                lefthand = num
            
    return answer

def whoWin(middleNum, leftNum, rightNum, hand):
    lefts = calculateDistance(middleNum, leftNum)
    rights = calculateDistance(middleNum, rightNum)
    if(lefts == rights):
        if(hand == "right"):
            return "R"
        else:
            return "L"
    if(lefts > rights):
        return "R"
    else:
        return "L"


def calculateDistance(a, b):
    aa = abs(a[0] - b[0])
    bb = abs(a[1] - b[1])
    return aa + bb

