n=int(input())
lo=0
hi=2**32
ct=50
while True:
	mid=(lo+hi)//2
	if mid**2>=n:
		hi=mid
	else:lo=mid+1
	ct-=1
	if not ct:break
print(mid)