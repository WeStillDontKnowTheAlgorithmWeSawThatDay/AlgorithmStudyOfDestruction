# 아뉘 3의 배수 판별법을 내가 어떻게 알아요!

nums = list(input())
nums.sort(reverse=True)
big_number = -1

sum = 0
for num in nums:
    sum += int(num)

if '0' in nums and sum % 3 == 0:
    nums.remove('0')
    big_number = ''.join(nums) + '0'
print(big_number)