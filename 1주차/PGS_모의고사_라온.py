def solution(answers):
    result = []
    people = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    
    i = 0
    correct = [0, 0, 0]
    for answer in answers:
        for person in people: 
            numbers = people[person]
            if numbers[i%len(numbers)] == answer:
                correct[person-1] += 1
        i += 1
        
    for i in range(len(correct)):
        if correct[i] == max(correct):
            result.append(i+1)
    return result