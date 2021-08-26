import sys
sys.setrecursionlimit(10**6)
m=int(input())
L=list(map(int,input().split()))
k=int(input())
d=dict()
def comb(n, k):
    if n<k:return 0
    if n==k:return 1
    if k==0:return 1
    if (n,k) in d:return d[(n,k)]
    res = comb(n-1,k)+comb(n-1,k-1)
    d[(n,k)]=res
    return res
ct=0
for i in L:
    ct+=comb(i,k)
print(ct/comb(sum(L),k))