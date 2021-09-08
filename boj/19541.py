import sys
input=sys.stdin.readline
n,m=map(int,input().split())
L=[False]*n
M=[]
for i in ' '*m:
    M.append(list(map(int,input().split()))[1:])
M.reverse()
res=list(map(int,input().split()))
checkL=[None]*n
collect=[]
print(M)
for li in M:
    print(checkL)
    check=True
    for k in li:
        if not res[k-1]:
            check=False
            break
    print(check)
    if check:
        for k in li:
            if checkL[k-1]==None:checkL[k-1]=True
    else:
        for k in li:
            checkL[k-1]=False
M.reverse()
print(checkL)
chkmem=checkL[:]
for li in M:
    check=False
    for i in li:
        if checkL[i-1]:
            check=True
            break
    if check:
        for i in li:
            checkL[i-1]=True
state=True

print(res)
print(checkL)
for i in range(n):
    if res[i] and checkL[i]==False:state=False
    if not res[i] and checkL[i]==True:state=False
if not state:print('NO')
else:
    print('YES')
    for i in range(n):
        if chkmem[i]==True:print(1,end=' ')
        elif chkmem[i]==None:
            if res[i]==True:print(1,end=' ')
            else:print(0,end=' ')
        else:print(0,end=' ')