stack = []
result = []
def func(array, num):
    id_list = array[num] # banned_id 하나에 해당하는 user_id 리스트
    for i in range(len(id_list)):
        if id_list[i] == 1 and i not in stack:
            stack.append(i)
            if num+1 == len(array):
                # print(">>> stack is full:", stack)

                # temp: 정렬 후 중복 제거 위해 , list -> string 하고 result에 append
                temp = stack.copy() 
                temp.sort()
                result.append(''.join(map(str, temp)))
                stack.pop()
                return ;
                # if i == len(id_list)-1: return ; # i가 다 돌았을 때만 return 
                # else: continue # i가 아직 다 돌지 않은 경우

            func(array, num+1)
            stack.pop()


def solution(user_id, banned_id):
    answer = 0
    # banned_id를 행으로 가지고 user_id를 열로 가지는 2차원 리스트
    array = [[0]*len(user_id) for i in range(len(banned_id))]
    
    # banned_id에 해당할 수 있는 user_id 추출과정
    for ban_idx, ban in enumerate(banned_id):
        for user_idx, user in enumerate(user_id):
            temp_ban, temp_user = ban, user  # 저장용도
            if len(ban) == len(user): # 1) 길이로 같은 문자열인지 판단
                while "*" in ban: # 2) banned_id 에서 "*" 문자를 모두 제거하였을 때의 문자열과 같은지 비교 (fr*d* frodo => frd frd)
                    idx = ban.index("*")
                    ban = list(ban)
                    user = list(user)
                    del ban[idx]
                    del user[idx]
                if ban == user: # 3) 같으면 array 2차원 리스트 (ban_idx, user_idx) = 1
                    array[ban_idx][user_idx] = 1
            ban = temp_ban # 저장용 템프

    func(array, 0)
    answer = len(list(set(result)))
    return answer
