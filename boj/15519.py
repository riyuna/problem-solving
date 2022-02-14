from collections import deque
s=input()
L=[]
ct=0
for i in s:
	if i in 'abcdefghijklmnopqrstuvwxyz':ct+=1
d=dict()
tot=0
for i in ' '*ct:
	a,b=input().split()
	d[a]=int(b)
	tot+=int(b)

def solve(s, d):
	ct=10
	while True:
		dq=deque([])
		ct-=1
		if not ct:break
		mem=len(s)
		for i in s:
			state=False
			if i==']' and dq[-1] in d and dq[-3] in d:
				a1=dq[-1]
				a2=dq[-3]
				if d[a1] and d[a2]:return False
				if d[a1]+d[a2]==0:return False
				dq.pop()
				dq.pop()
				dq.pop()
				dq.pop()
				dq.append(a1 if d[a1] else a2)
				if d[a1]:d[a1]-=1
				else:d[a2]-=1
				state=True
			if not state:dq.append(i)
		ss=''.join(dq)
		if len(ss)==mem:break
		s=ss
	return True

if tot!=s.count('-'):print('No')
else:print(['No', 'Yes'][solve(s,d)])