def solution(record):
    answer = []
    users = {}
    for line in record:
        words = line.split(" ")
        command, uid = words[0], words[1]
        if command == "Enter" or command == "Leave":
            answer.append([uid, command])
        if command != "Leave":
            users[uid] = words[2]
    for i, line in enumerate(answer):
        uid, command = line
        if command == "Enter": 
            answer[i] = users[uid] + "님이 들어왔습니다."
        if command == "Leave": 
            answer[i] = users[uid] + "님이 나갔습니다."
    return answer
