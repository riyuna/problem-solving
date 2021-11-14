import sys
input=sys.stdin.readline
def solve(a,b):
    if a>b:a,b=b,a
    if b%a==0:return True
    if b-a<a:
        return not solve(b-a, a)
    return True
while True:
    a,b=map(int,input().split())
    if a==b==0:break
    print(f"{'BA'[solve(a,b)]} wins")