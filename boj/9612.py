d=dict()
n=int(input())
rem=''
mxm=0
for i in ' '*n:
	s=input()
	if s not in d:d[s]=0
	d[s]+=1
	if d[s]>mxm or d[s]==mxm and s>rem:
		mxm=d[s]
		rem=s

print(rem,mxm)