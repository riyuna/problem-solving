a,b,c=map(float,input().split())
def f(x):
	return 1/(b**2-x**2)**0.5 + 1/(a**2-x**2)**0.5

lo = 0
hi = min(a,b)

while abs(hi-lo)>1e-6:
	mid = (lo+hi)/2
	if f(mid) < 1/c: lo=mid
	else:hi=mid

print((lo+hi)/2)