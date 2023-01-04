class GFG: 
    def __init__(self,graph): 
          
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 
  
    def bpm(self, u, matchR, seen): 
        for v in range(self.jobs): 
            if self.graph[u][v] and seen[v] == False: 
                seen[v] = True 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
        
    def maxBPM(self): 
        matchR = [-1] * self.jobs 
        result = 0 
        for i in range(self.ppl): 
            seen = [False] * self.jobs 
            if self.bpm(i, matchR, seen): 
                result += 1
        return result 
        
n,m=map(int,input().split())
check=[]
ct=0
for i in ' '*n:
	s=input()
	check.append(s)
	for j in s:
		if j=='X':ct+=1

odd = (n*m+1)//2
even = n*m-odd
L=[[0]*even for i in range(odd)]
for i in range(n):
	for j in range(m):
		now = (i*m+j)//2
		if check[i][j]=='X':continue
		if (i+j)%2==0:
			if i>0:
				ii=i-1
				if check[ii][j]!='X':
					k = (ii*m+j)//2
					L[now][k]=1
			if i<n-1:
				ii=i+1
				if check[ii][j]!='X':
					k = (ii*m+j)//2
					L[now][k]=1
			if j>0:
				jj=j-1
				if check[i][jj]!='X':
					k=(i*m+jj)//2
					L[now][k]=1
			if j<m-1:
				jj=j+1
				if check[i][jj]!='X':
					k=(i*m+jj)//2
					L[now][k]=1
	
g=GFG(L)
res=g.maxBPM()
print((n*m-ct-res))