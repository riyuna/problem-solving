import sys


input = sys.stdin.readline


def f(temp, temp_acture, new):
	D = [[100000] * 10001 for i in range(temp[0]+1)]
	D[0][0] = 0
	for i in range(1, temp[0]+1):
		for j in range(10001):
			D[i][j] = min(D[i][j], D[i-1][j])
			if j >= temp[i]:
				D[i][j] = min(D[i][j], D[i][j-temp[i]]+temp_acture[i], D[i-1][j-temp[i]]+temp_acture[i])
	ans = [new[0]]
	for i in range(1, new[0]+1):
		temp = new[i]
		while D[-1][temp] > 99999:
			temp += 1
			if temp >= 10000:
				break
		ans.append(D[-1][temp])
	return ans

if __name__ == "__main__":
	B = int(input())
	k = int(input())
	pack = []
	temp = list(map(int, input().split()))
	for i in range(1, len(temp)):
		pack.append([temp[i], temp[i]])
	
	old = temp
	old_actual = temp
	for i in range(1, k):
		new = list(map(int, input().split()))
		new_actual = f(old, old_actual, new)
		for j in range(1, len(new)):
			pack.append([new[j], new_actual[j]])
		old = new
		old_actual = new_actual
	
	pack.sort(key = lambda x:x[1])
	check = True
	for i in pack:
		if i[1]>=B:
			print(i[0])
			check = False
			break
	if check:
		print("impossible")