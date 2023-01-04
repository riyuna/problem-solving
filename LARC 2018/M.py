n = int(input())
L = list(map(int, input().split()))

L.reverse()

temp = L[0]
ans = 1

for i in range(1, n):
	if L[i] >= temp:
		pass
	else:
		ans += 1
	temp = L[i]
print(ans)