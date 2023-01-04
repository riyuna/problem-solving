n = int(input())
L = []
for i in range(n):
	L.append(list(map(int, input().split())))


D = [0] * (n+1)
for i in range(n):
	D[i+1] = D[i] + L[i][1]*4
	temp = 0
	if i== 0:
		continue
	temp += L[i-1][0]
	if temp >= 120:
		continue
	D[i+1] = min(D[i+1], D[i-1] + L[i-1][1]*4 + L[i][1]*2)
	if i == 1:
		continue
	temp += L[i-2][0]
	if temp >= 120:
		continue
	D[i+1] = min(D[i+1], D[i-2] + L[i-2][1]*4 + L[i-1][1]*2 + L[i][1])
	if i == 2:
		continue
	temp += L[i-3][0]
	if temp >= 120:
		continue
	D[i+1] = min(D[i+1], D[i-3] + L[i-3][1]*4 + L[i-2][1]*2 + L[i-1][1] + L[i][1])
	if i == 3:
		continue
	temp += L[i-4][0]
	if temp >= 120:
		continue
	D[i+1] = min(D[i+1], D[i-4] + L[i-4][1]*4 + L[i-3][1]*2 + L[i-2][1] + L[i-1][1] + L[i][1])
	if i == 4:
		continue
	temp += L[i-5][0]
	if temp >= 120:
		continue
	D[i+1] = min(D[i+1], D[i-5] + L[i-5][1]*4 + L[i-4][1]*2 + L[i-3][1] + L[i-2][1] + L[i-1][1] + L[i][1])
print(str(D[-1]//4) + '.' + ['00', '25', '50', '75'][D[-1]%4])
