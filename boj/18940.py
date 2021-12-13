import sys
input=sys.stdin.readline
def solve(n):
    if n in [0, 14, 34] or n%34 in [4, 8, 20, 24, 28]:return False
    return True

for i in ' '*int(input()):
    print('Yuto' if solve(int(input())) else 'Platina')