words = list(input())
alphabets = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])

stack, answer = [], 0
for word in words:
    stack.append(word)
    for alphabet in alphabets:
        if alphabet in ''.join(stack):
            answer += 1
            for _ in range(len(alphabet)):
                stack.pop()
            answer += len(stack)
            stack = []
answer += len(stack)
print(answer)
