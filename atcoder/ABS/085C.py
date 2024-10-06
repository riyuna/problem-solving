import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n,y=linput()
y//=1000
a=-1
b=-1
c=-1
for i in range(int((y-n)//9+1)):
	k=(y-n)-(i*9)
	if k%4:continue
	kk=k//4
	cc=(n-i-kk)
	if cc<0:continue
	if i*10+kk*5+cc*1==y:
		a,b,c=i,kk,cc
		break
print(a,b,c)