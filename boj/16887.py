def grundy(n):
	if n<4:return 0
	if n<16:return 1
	if n<82:return 2
	if n<6724:return 0
	if n<50626:return 3
	if n<2562991876:return 1
	return 2

n=int(input())
res=0
for i in list(map(int,input().split())):
	res^=grundy(i)
print('koosaga' if res else 'cubelover')