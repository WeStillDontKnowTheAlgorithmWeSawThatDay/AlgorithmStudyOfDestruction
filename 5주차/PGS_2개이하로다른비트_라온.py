def solution(numbers):
    answer = []
    for number in numbers:
        bits = make_bits(number)[::-1]
        flag = False
        for i, bit in enumerate(bits[:len(bits)-1]):
            if bit == 0:
                if i > 0:
                    answer.append(number + 2**i - 2**(i-1))
                else:
                    answer.append(number + 2**i)
                flag = True
                break
        if not flag:
            length = len(bits) - 1
            answer.append(number + 2**length - 2**(length-1))   
    return answer

def make_bits(number):
    i = 1
    while True:
        if 2**i > number:   break
        i += 1

    bits = []
    while i >= 0:
        if 2**i <= number:
            number -= 2**i
            bits.append(1)
        else: 
            bits.append(0)
        i -= 1
    return bits
    
    