import sys
input=sys.stdin.readline
def palace(x,y):
    return (x+y)%3+((x//3)^(y//3))*3

res=0
for i in ' '*int(input()):
    x,y=map(int,input().split())
    res^=palace(x,y)

print('koosaga' if res else 'cubelover')