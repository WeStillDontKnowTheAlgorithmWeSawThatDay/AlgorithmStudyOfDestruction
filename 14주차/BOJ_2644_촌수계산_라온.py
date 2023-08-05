n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
relations = [list(map(int, input().split())) for _ in range(m)]

parents = dict()
for parent, child in relations:
    parents[child] = parent

def find_parent(x1, parents_list):
    if x1 == None:
        return parents_list
    parents_list.append(x1)
    return find_parent(parents.get(x1), parents_list)

t1_parents = find_parent(t1, [])
t2_parents = find_parent(t2, [])

answer, flag = -1, False
for i, parent1 in enumerate(t1_parents):
    for j, parent2 in enumerate(t2_parents):
        if parent1 == parent2:
            answer = i + j
            flag = True
            break
    if flag:    break
print(answer)
