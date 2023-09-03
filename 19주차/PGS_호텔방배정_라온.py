# **, 어렵눼, 재귀 리미트 해줘야 함

import sys
sys.setrecursionlimit(10000)

def search(number, rooms):
    if rooms.get(number) == None:
        rooms[number] = number + 1
        return number
    
    new_number = search(rooms[number], rooms)
    rooms[number] = new_number + 1
    return new_number


def solution(k, room_number):
    answer = []
    rooms = {}
    for number in room_number:
        room = search(number, rooms)
        answer.append(room)
    return answer

''' 시간 초과
def search(number, rooms):
#     for room in rooms:
#         if room > number:
#             return room

    rooms = list(rooms)
    l, r = 0, len(rooms)

    while l < r:
        mid = (l+r) // 2
        
        if rooms[mid] == number + 1:
            return rooms[mid]
        
        if number > rooms[mid]:
            l = mid + 1
            
        if number < rooms[mid]:
            r = mid
            
    return rooms[l]

def solution(k, room_number):
    answer = []
    queue = [i+1 for i in range(k)]
    rooms = set(queue)
    
    for number in room_number:
        if number in rooms:
            rooms.remove(number)
            answer.append(number)
        else:
            new_number = search(number, rooms)
            rooms.remove(new_number)
            answer.append(new_number)
    return answer
'''