import sys
input=sys.stdin.readline
def bishop(x,y):
    return min(x,y)

def king(x,y):
    if x%2 and y%2:return 2
    if x%2==0 and y%2==0:return 0
    if (min(x,y)%2):return 3
    return 1

def knight(x,y):
    if min(x,y)%3==0:return 0
    if min(x,y)%3==1 and x==y:return 0
    if min(x,y)%3==2 and (x-y)**2>1:return 2
    return 1

def rook(x,y):
    return x^y

def palace(x,y):
    return (x+y)%3+((x//3)^(y//3))*3

res=0
for i in ' '*int(input()):
    x,y,c=input().strip().split()
    x=int(x)
    y=int(y)
    if c=='B':res^=bishop(x,y)
    if c=='N':res^=knight(x,y)
    if c=='K':res^=king(x,y)
    if c=='R':res^=rook(x,y)
    if c=='P':res^=palace(x,y)

print('koosaga' if res else 'cubelover')