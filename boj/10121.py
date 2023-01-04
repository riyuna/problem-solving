n=int(input())
s=input()
#j=apple, p=orange


def solve(s, rev=False):
	if len(s)==0:return 0
	if s == 'j':return 0
	n=len(s)
	pt1=0
	pt2=0
	apple=0
	orange=0
	res=0
	while pt2<n:
		if s[pt2]=='j':
			apple+=1
		else:orange+=1
		if apple>orange or pt2==n-1:
			if pt2==n-1:pt2+=1
			ss=s[pt1:pt2][::-1]
			if not rev:res=max(res, solve(ss, rev=True))
			else:res=max(res, len(ss))
			pt2+=1
			pt1=pt2
			apple=0
			orange=0
		else:
			pt2+=1
	return res




print(solve(s))