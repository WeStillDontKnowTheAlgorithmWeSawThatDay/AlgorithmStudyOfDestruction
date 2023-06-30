# 1,1

# 1,2 안하고 더하고
# 2,1 더하고 빼고

# 3,1 더하고 안하고
# 2,2 빼고 더하고
# 1,3 빼고 더하고

# 1,4 안하고 더하고
# 2,3 더하고 빼고
# 3,2 더하고 빼고
# 4,1 더하고 빼고

# 1, 2, 3, 4...

num = int(input())

seq = 1
while num > seq:
    num -= seq
    seq += 1

if seq % 2 == 0:
    up = num
    down = seq-num+1
else:
    up = seq-num+1
    down = num

print(up, "/", down, sep="")
