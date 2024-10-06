import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,k=linput()
L=linput()
def solve(L):
	if len(L)<2:return 0
	d=dict()
	mx=0
	for i in L:
		if i not in d:d[i]=0
		d[i]+=1
		mx=max(d[i],mx)

	result=[[]for i in range(mx)]
	L.sort(reverse=True)
	pt=0
	for i in range(len(L)):
		if i>0 and L[i-1]==L[i]:
			pt+=1
		else:pt=0
		result[pt].append(L[i])
	# start=[]
	# end=[]
	# for i in result:
	# 	start.append(i[0])
	# 	end.append(i[-1])
	# start.sort()
	# end.sort()
	# ss=start[0]
	# ee=end[-1]
	# flag=True
	# for i in result:
	# 	if i[0]==ss and i[-1]==ee:flag=False
	# t = ee-ss
	# if mx>1 and not flag:
	# 	t=max(end[-2]-ss, ee-start[1])
	mem=[]
	for i in d:
		if d[i]==mx:
			mem.append(i)
	mem.sort()
	t=mem[0]-mem[-1]
	return (len(L)-mx)*k+t
res1=solve(L)
L.sort()
res2=solve(L[1:n-1])+L[-1]-L[0]
print(max(res1, res2))