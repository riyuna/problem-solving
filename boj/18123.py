import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()

ctmem=[]
size=[1]*40
def getsize(k, root, L):
	size[k]=1
	for i in L[k]:
		if i==root:continue
		size[k]+=getsize(i, k, L)
	return size[k]

def centroid(k, root, now, L):
	#check if k is a centroid of tree or not
	for i in L[k]:
		if i==root:continue
		if size[i]>now:return centroid(i, k, now, L)
	return k

#handle when there exist even number of node

def handle(k, root, now, sz, L):
	if sz%2==1:return
	for i in L[k]:
		if i==root:continue
		tot=1
		flag=True
		if size[i]>now+1:continue
		for j in L[i]:
			if j==k:continue
			tot+=size[j]
			if size[j]>now:flag=False
		if flag and sz<=now+tot:ctmem.append(i)
	return

def hashing(k, root, L):
	res=[1,1]
	mem=[]
	for i in L[k]:
		if i==root:continue
		mem.append(hashing(i, k, L))
	mem.sort()
	for i,j in mem:
		res[0]*=2**j
		res[0]+=i
		res[1]+=j
	res[0]*=2
	res[1]+=1
	return res
trees=[]
for i in ' '*n:
	s=iinput()
	L=[[]for i in range(s)]
	for j in ' '*(s-1):
		a,b=linput()
		L[a].append(b)
		L[b].append(a)
	now=getsize(0, -1, L)
	cent=centroid(0, -1, now,L)
	ctmem.append(cent)
	handle(cent, -1, now,s,L)
	h=[0,0]
	for ct in ctmem:
		a,b=hashing(ct, -1,L)
		h[0]=max(h[0], a)
		h[1]=max(h[1], b)
	trees.append(h[0])
print(len(set(trees)))