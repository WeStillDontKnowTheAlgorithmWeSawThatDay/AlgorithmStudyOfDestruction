# 시간초과, lb
def solution(infos, queries):
    answer = []
    
    appliers = []
    conditions = []
    
    lang = {"cpp": set(), "java": set(), "python": set(), "-": set(i for i in range(len(infos)))}
    job = {"backend": set(), "frontend": set(), "-": set(i for i in range(len(infos)))}
    career = {"junior": set(), "senior": set(), "-": set(i for i in range(len(infos)))}
    food = {"chicken": set(), "pizza": set(), "-": set(i for i in range(len(infos)))}
    
    for i, info in enumerate(infos):
        a, b, c, d, e = info.split(" ")
        lang[a].add(i)
        job[b].add(i)
        career[c].add(i)
        food[d].add(i)
        appliers.append(info.split(" "))
    
    for query in queries:
        temp = query.split(" and ")
        temp = temp[0:3] + temp[3].split(" ")
        conditions.append(temp)

    for condition in conditions:
        a, b, c, d, e = condition
        print(condition)
        people = lang[a]
        temp = people.copy()
        for person in people:
            if person not in job[b] or person not in career[c] or person not in food[d]:
                temp.remove(person)
    return answer