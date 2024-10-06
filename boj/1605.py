mod=10**9+7
p1=998244353
p2=2281707377
def check(s, k):
	if len(s)<k:return False
	hash1=0
	hash2=0
	mem1=dict()
	mem2=dict()
	for i in range(k):
		hash1*=p1
		hash2*=p2
		hash1+=ord(s[i])
		hash2+=ord(s[i])
		hash1%=mod
		hash2%=mod
	mem1[hash1]=True
	mem2[hash2]=True
	a=pow(p1, k, mod)
	b=pow(p2, k, mod)
	for i in range(k, len(s)):
		hash1*=p1
		hash2*=p2
		hash1-=a*ord(s[i-k])
		hash2-=b*ord(s[i-k])
		hash1+=ord(s[i])
		hash2+=ord(s[i])
		hash1%=mod
		hash2%=mod
		if hash1 in mem1 and hash2 in mem2:return True
		mem1[hash1]=True
		mem2[hash2]=True
	return False
n=int(input())
s=input()
start=0
end=n
k=40
while(k):
	k-=1
	mid=start+end
	mid//=2
	if check(s, mid):
		start=mid
	else:
		end=mid
print(mid)