from functools import cmp_to_key
temp_list=[0]*61
n,k=map(int,input().split())
for i in ' '*n:
    t,w=map(int,input().split())
    temp_list[t-40]=max(temp_list[t-40], w)

L=[]
for i in range(61):
    if temp_list[i]:L.append((i+40, temp_list[i]))

def solve(L, k):
    if len(L)==0:return 0
    L.sort()
    t=L[0][0]
    def time_cmp(a, b):
        return 1 if (a[0]-t)*(a[1])<=(b[0]-t)*(b[1]) else -1
    L=sorted(L, key=cmp_to_key(time_cmp))
    mi=(L[0][0]-t)*L[0][1]+30
    if k==1:return mi
    val=0
    for i in range(len(L)-1):
        last=L.pop(-1)
        val=max(val,(last[0]-t)*last[1]+30)
        mi=min(mi, solve(L[:], k-1)+val)
    return mi

print(solve(L, k))