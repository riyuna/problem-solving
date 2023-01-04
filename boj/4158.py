import sys
input=sys.stdin.readline
while True:
	n,m=map(int,input().split())
	if n+m==0:break
	d=dict()
	ct=0
	for i in ' '*(n+m):
		k=int(input())
		if k in d:ct+=1
		d[k]=True
	print(ct)