def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    return False

# 절대 외우지마
# 숫자로만인지: isdigit()
# 알파벳만인지: isalpha()
# 숫자 또는 알파벳으로 이루어져 있는지: isalnum()
