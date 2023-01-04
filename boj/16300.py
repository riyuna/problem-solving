import sys


input = sys.stdin.readline


if __name__ == "__main__":
	molecule, n = input().split()
	n = int(n)
	s = input().strip()
	molecule = molecule  + ' '
	s = s + ' '
	L = [0] * 26
	temp = 0
	for i in range(1, len(molecule)):
		if ord(molecule[i])>64 or molecule[i] == ' ':
			if temp == i-1:
				L[ord(molecule[temp])-65] += 1
			else:
				L[ord(molecule[temp])-65] += int(molecule[temp+1:i])
			temp = i

	temp = 0
	D = [0] * 26
	for i in range(1, len(s)):
		if ord(s[i])>64 or s[i] == ' ':
			if temp == i-1:
				D[ord(s[temp])-65] += 1
			else:
				D[ord(s[temp])-65] += int(s[temp+1:i])
			temp = i
	
	ans = 10000000000000
	for i in range(26):
		if D[i] != 0:
			ans = min(ans, L[i]*n//D[i])
	print(ans)
