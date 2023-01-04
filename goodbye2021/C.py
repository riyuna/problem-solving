import sys

input=sys.stdin.readline
L=[]
n,g,k=map(int,input().split())
important=0
for i in ' '*n:
	s,l,o=map(int,input().split())
	if not o:important+=1
	L.append([s,l,o])


def checker(day, L, g, k, important):
	ct=0
	M=[]
	for s,l,o in L:
		kk=s*max(1,day-l)
		M.append((o, kk))
	M.sort()
	for i in range(max(important, len(L)-k)):
		ct+=M[i][1]
		if ct>g:return False
	return True


lo=0
hi=2*10**9+1

while True:
	mid=(lo+hi)//2
	if lo+1==hi or lo==hi:break
	if checker(mid, L, g, k, important):
		lo=mid
	else:
		hi=mid
print(mid)