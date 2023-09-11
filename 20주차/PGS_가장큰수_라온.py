# **

def solution(numbers):
    num_str = list(map(str, numbers)) #numbers의 인덱스들이 int이기 때문에 비교를 위해 문자열로 바꿔준다. -> map 함수 사용해도 좋을 것 같습니당
    num_str.sort(key = lambda x: (x*3),reverse=True)    #숫자를 문자형태로 비교하면 첫째자리수만 ascii코드로 바뀌어 자동 비교되기때문에 자리수를 맞춰준 다음 lambda로 비교를 해준다.
    return str(int(''.join(num_str))) # 모든 원소가 0이면 0이 이어져서 나올 수 있기 때문에 이럴때를 대비하여 0을 return하게 해준다.
