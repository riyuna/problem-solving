import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
k,g,m=linput()
gg,mm=0,0
for i in range(k):
	if gg==g:gg=0
	elif mm==0:mm=m
	else:
		if(gg+mm>g):gg,mm=g,(gg+mm-g)
		else: gg,mm=gg+mm,0
print(gg,mm)