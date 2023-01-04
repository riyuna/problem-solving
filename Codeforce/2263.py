import sys
sys.setrecursionlimit(100100)
n=int(input())
L1 =list(map(int,input().split()))
L2 = list(map(int,input().split()))

mem=dict()
for i in range(n):
	mem[L1[i]]=i

def solve(start1, end1, start2, end2):
	if start1>end1:return
	if start2>end2:return

	root = mem[L2[end2]]
	print(L1[root],end=' ')

	solve(start1, root-1, start2, start2+root-start1-1)
	solve(root+1, end1, start2+root-start1, end2-1)

solve(0,n-1,0,n-1)