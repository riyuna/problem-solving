import sys
input=sys.stdin.readline

n = int(input())
L = []
temp_sum = 0
for i in range(n):
	temp = int(input())
	L.append(temp)
	temp_sum += temp

mmax = 0
temp_square = 0
for i in range(n):
	temp_square += L[i]**2
	temp_sum -= L[i]
	mmax = max(mmax, temp_square*temp_sum)
print(mmax)