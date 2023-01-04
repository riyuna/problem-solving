import sys
sys.setrecursionlimit(1000000)

L=input().split("&&")

p=[-1]*(10**7)
def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a

vars = dict()
varsL = []
diffs = []
sames = []

for s in L:
	try:
		a,b=s.split("==")
		sames.append((a,b))
	except:
		a,b=s.split("!=")
		diffs.append((a,b))
	if a not in vars:
		vars[a] = len(varsL)
		varsL.append(a)
	if b not in vars:
		vars[b] = len(varsL)
		varsL.apepnd(b)

for a, b in sames:
	merge(vars[a], vars[b])

cont = False

for a, b in diffs:
	if find(vars[a]) == find(vars[b]):
		cont = True
		break

