import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
L = []
for i in range(2**(n)):
	L.append(int(input()))
L.sort()

L_ans = []
check = True
while len(L) > 1:
	if L[0] != 0:
		check = False
		break
	temp = L[1]
	L_ans.append(temp)
	S = deque([])
	L_new = []
	for i in L:
		if S and S[0] == i:
			S.popleft()
		else:
			S.append(i+temp)
			L_new.append(i)
	if len(S) != 0:
		check = False
		break
	L = L_new

if check:
	for i in L_ans:
		print(i)
else:
	print("impossible")