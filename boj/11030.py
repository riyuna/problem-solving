import sys
sys.setrecursionlimit(10**5)
a,b=map(int,input().split())

def tet(a,b):
    if b==1:return (a, False)
    k,big=tet(a,b-1)
    res=pow(a, k, 10**8)
    if res==0:
        res=10**8
        big=True
    if a==1:big=False
    elif big==False:
        c=a
        ct=0
        while ct<k:
            c*=a
            ct+=1
            if c>=10**8:
                big=True
                break

    return res, big

k,big=tet(a,b)
k%=10**8
s=str(k)
print('0'*(8-len(s))+s if big else s)