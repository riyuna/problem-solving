n=int(input())

L=[1]
ct=2
while True:
	L.append(L[-1]+ct)
	ct+=1
	if L[-1]>10**9:break

def solve(n):
	for i in range(len(L)):
		if L[i]>=n:return i+1

k=solve(n)
r=k*(k+1)//2-n
print(')'*(k-r)+'('+')'*r+'('*(k-1))