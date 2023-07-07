from itertools import combinations

fun = input()

stack = []
left = []
right = []

괄호_리스트 = []

for i in range(len(fun)):
    if fun[i] == '(':
        # left.append(i)
        stack.append(i)
    if fun[i] == ')':
        괄호_리스트.append([stack.pop(), i])

# print(괄호_리스트)

fun_list = []
for i in range(1, len(괄호_리스트) + 1):
    fun_list += combinations([x for x in range(len(괄호_리스트))], i)

# print(fun_list)

ans_list = []

for i in range(len(fun_list)):
    rm_list = []
    # print(i)
    # print(fun_list[i])
    # print(fun_list)
    for j in range(len(fun_list[i])):
        # print(fun_list[i][j])
        # print(j, 괄호_리스트[rm_list[j]])
        l, r = 괄호_리스트[fun_list[i][j]]
        # print(j)
        # print(l, r)
        rm_list.append(l)
        rm_list.append(r)
    # print(rm_list)
    tmp = ""
    for f in range(len(fun)):
        if f not in rm_list:
            tmp += fun[f]
            # print(fun[f], end='')
    if tmp not in ans_list:
        ans_list.append(tmp)
    # print(tmp)
    # print()

ans_list.sort()
for ans in ans_list:
    print(ans)
# print(*ans_list)
