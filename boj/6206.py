mod=10**9+7
p1=998244353
p2=2281707377
def check(s, k, ct):
	if len(s)<k:return False
	hash1=0
	hash2=0
	mem1=dict()
	mem2=dict()
	for i in range(k):
		hash1*=p1
		hash2*=p2
		hash1+=s[i]
		hash2+=s[i]
		hash1%=mod
		hash2%=mod
	mem1[hash1]=1
	mem2[hash2]=1
	a=pow(p1, k, mod)
	b=pow(p2, k, mod)
	for i in range(k, len(s)):
		hash1*=p1
		hash2*=p2
		hash1-=a*s[i-k]
		hash2-=b*s[i-k]
		hash1+=s[i]
		hash2+=s[i]
		hash1%=mod
		hash2%=mod
		if hash1 in mem1 and hash2 in mem2:
			mem1[hash1]+=1
			mem2[hash2]+=1
			if mem1[hash1]>=ct and mem2[hash2]>=ct:return True
		else:
			mem1[hash1]=1
			mem2[hash2]=1
	return False
n,k=map(int,input().split())
L=[]
for i in ' '*n:L.append(int(input()))
start=0
end=n
ct=40
while(ct):
	ct-=1
	mid=start+end
	mid//=2
	if check(L, mid, k):
		start=mid
	else:
		end=mid
print(mid)