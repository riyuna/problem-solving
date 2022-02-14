n=int(input())
L=list(map(int,input().split()))
def check(n):
	s=str(n)
	for i in range(len(s)-1):
		if int(s[i])+1!=int(s[i+1]):return False
	return True
res=-1
for i in range(n):
	for j in range(i):
		if check(L[i]*L[j]) and res<L[i]*L[j]:res=L[i]*L[j]
print(res)