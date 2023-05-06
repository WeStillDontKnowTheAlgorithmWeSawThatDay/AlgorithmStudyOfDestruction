def solution(participant, completion):
    answer = ''
    dictionary = {person:0 for i, person in enumerate(participant)}
    
    for person in participant:
        dictionary[person] += 1
        
    for person in completion:
        if dictionary[person] == 1:
            del dictionary[person]
        else:
            dictionary[person] -= 1

    return list(dictionary.keys())[0]
