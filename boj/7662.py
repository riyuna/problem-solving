import sys
from queue import PriorityQueue as pq
input=sys.stdin.readline
for i in ' '*int(input()):
	k=int(input())
	maxque=pq()
	minque=pq()
	d=dict()
	for _ in ' '*k:
		s,n=input().split()
		n=int(n)
		if s=='I':
			maxque.put(-n)
			minque.put(n)
			if n not in d:d[n]=0
			d[n]+=1
		else:
			if n==1:
				if maxque.qsize():res=-maxque.get()
				else:res=10**10
				while not(res in d and d[res]):
					if maxque.qsize()==0:break
					res=-maxque.get()
				if res in d and d[res]: d[res]-=1
			else:
				if minque.qsize():res=minque.get()
				else:res=10**10
				while not(res in d and d[res]):
					if minque.qsize()==0:break
					res=minque.get()
				if res in d and d[res]: d[res]-=1
	ct=0
	for k in d:
		ct+=d[k]
	if ct==0:print('EMPTY')
	else:
		res=-maxque.get()
		while not(res in d and d[res]):
			res=-maxque.get()
		mx=res
		res=minque.get()
		while not(res in d and d[res]):
			res=minque.get()
		mn=res
		print(mx, mn)