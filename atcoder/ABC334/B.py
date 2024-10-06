import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
#print('なんでや!阪神関係ないやろ!')

a,m,l,r=linput()
k=a%m
l-=k
r-=k
ct=0
if l%m==0:ct+=1
l//=m
r//=m
print(ct+r-l)