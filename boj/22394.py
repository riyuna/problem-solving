import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
from math import ceil
mod=998244353
dp=[]
P=[[0]*(i*6+2)for i in range(21)]
PE=[[0]*(i*6+2)for i in range(21)]
for i in range(1, 21):
	PE[i][1]=(7/2)*i
	PE[i][0]=PE[i][1]
for i in range(1, 8):
	P[1][i]=(i-1)/6
	if i>1:
		PE[1][i]=(PE[1][i-1]-(P[1][i]-P[1][i-1])*(i-1))


for i in range(2, 21):
	for j in range(1, i*6+2):
			tot=0
			for k in range(max(0, j-6), j):
				try:
					tot+=P[i-1][k]
				except:tot+=1
			P[i][j]=tot/6
			if j>=2:
				PE[i][j]=PE[i][j-1]-(P[i][j]-P[i][j-1])*(j-1)
def f(n,ai,k):
	ii=ceil(ai)
	return PE[n][ii]*((1-P[n][ii]**k)/(1-P[n][ii]))+P[n][ii]**ai
while True:
	n,m=linput()
	if n==m==0:break
	res=[0]
	for i in range(m):
		res.append(PE[n][ceil(res[-1])]+P[n][ceil(res[-1])]*res[-1])
	print(res[-1])