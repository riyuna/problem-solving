import sys
input=sys.stdin.readline

for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    res=1
    for j in range(n):
        if L[j]:
            if j and L[j-1]:res+=5
            else:res+=1
        else:
            if j and not L[j-1]:
                res=-1
                break
    print(res)