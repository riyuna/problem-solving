import sys


input = sys.stdin.readline


if __name__ == "__main__":
	s = input().strip()
	i = 0
	j = len(s)-1
	pointer1 = 0
	pointer2 = len(s)-1
	ans = 1

	hash1 = 0
	hash2 = 0

	temp = 1
	p = 998244353

	while pointer1<pointer2:
		hash1 *= 2
		hash1 += ord(s[pointer1])-48
		hash1 %= p


		hash2 += temp * (ord(s[pointer2])-48)
		hash2 %= p
		temp *= 2
		temp %= p

		pointer1 += 1
		pointer2 -= 1


		if hash1 == hash2:
			if s[i:pointer1] == s[pointer2+1:j+1]:
				ans += 2
				i = pointer1
				j = pointer2
				temp = 1
				hash1 = 0
				hash2 = 0
	if i > j:
		ans -= 1
	
	print(ans)


