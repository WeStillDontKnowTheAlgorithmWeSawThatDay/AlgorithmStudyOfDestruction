def solution(participant, completion):
    count = [0 for i in range(len(participant))]
    participantsDict = dict(zip(participant, count))
    
    for part in participant:
        participantsDict[part] += 1;
    
    print(participantsDict)
    
    for comp in completion:
        participantsDict[comp] -= 1;
    
    for partDict in participantsDict:
        if(participantsDict[partDict] != 0):
            return partDict;
    
