def solution(n):
    return func(n, 1, 2, 3, [])

def func(n, src, mid, dst, path):
    if n == 1:
        path.append([src, dst])
        return path
    func(n-1, src, mid, dst, path)
    path.append([src, dst])
    func(n-1, mid, dst, mid, path)
    return path
