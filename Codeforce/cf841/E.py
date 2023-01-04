import sys
input=sys.stdin.readline

res=0
for i in range(1,4):
	for j in range(1,4):
		for k in range(1,4):
			for l in range(1,4):
				for m in range(1,4):
					for n in range(1,4):
						L=[i,j,k,l,m,n]
						for s in range(6):
							lsl=0
							grr=0
							for t in range(s):
								if L[t]<L[s]:lsl+=1
							for t in range(s+1, 6):
								if L[t]>L[s]:grr+=1
							if lsl<grr:res+=L[s]
print(res)