import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
a=iinput()
b=iinput()
c=iinput()
x=iinput()
ct=0
for i in range(a+1):
	for j in range(b+1):
		for k in range(c+1):
			if i*500+j*100+k*50==x:ct+=1
print(ct)