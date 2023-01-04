import sys;input=sys.stdin.readline
n,q=map(int,input().split())
# box = [[i+1, 1] for i in range(n)]
where = [i for i in range(n)]

p=[-1]*(n+1)
def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a
tot = n
for i in ' '*q:
	tl = input().split()
	if tl[0]=='1':
		x,y=int(tl[1])-1, int(tl[2])-1
		merge(x, y)
	if tl[0]=='2':
		x=int(tl[1])-1
		p.append(x)
		where.append(x)
	if tl[0]=='3':
		print("=========")
		print(where)
		print(p)
		x=int(tl[1])-1
		print(find(where[x])+1)
		print()

