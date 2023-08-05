import sys

input = sys.stdin.readline

n = int(input())

def stone_game(n):
    return "SK" if n % 2 == 1 else "CY"

print(stone_game(n))
