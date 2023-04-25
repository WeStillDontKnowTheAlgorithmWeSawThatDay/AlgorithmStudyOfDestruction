
# 문자 밀기 하면 아스키코드로 바꿔서 미는게 젤 먼저 생각남
#
# 딕셔너리에 넣고 키값 증가하는 식으로 해볼까도 했는데 코드는 그게 더 깔끔할지도?

def solution(s, n):
    answer = ''

    # print(ord('A'), ord('Z'))
    # print(ord('a'), ord('z'))
    for ss in s:
        sNum = ord(ss)
        print(sNum)
        if 65 <= sNum <= 90:
            sNum += n
            if sNum > 90:
                sNum -= 26
            answer += chr(sNum)

        elif 97 <= sNum <= 122:
            sNum += n
            if sNum > 122:
                sNum -= 26
            answer += chr(sNum)
        else:
            answer += ss

    return answer