def isCap(s):
	return s in 'ABCD'

class Board:
	def __init__(self):
		self.pieces = dict()
		for i in 'ABCDabcd':self.pieces[i]=-1

	def play(self, yut, piece):
		ct=yut.count('F')
		if ct==0:ct=5
		
		#to check combined piece
		combined = []
		opposite = []
		for i in 'ABCDabcd':
			if self.pieces[i] == self.pieces[piece] and self.pieces[piece]!=-1 and isCap(piece)==isCap(i):
				combined.append(i)
			elif i == piece : combined.append(i)
			if isCap(piece) != isCap(i): opposite.append(i)
		
		now = self.pieces[piece]
		res = -1
		if now<20 and now not in (4, 9):
			res = now+ct
			if res > 19: res = 100
		elif now == 4: res = 19+ct
		elif now == 9:
			res = 24 + ct
			if res==27: res = 22
			if res>27: res-=1
		elif now in (20, 21, 23, 24):
			res = now + ct
			if res>24: res -= 11
		elif now == 22:
			res = now+ct+4
			if res==29:res = 19
			if res > 29:res = 100
		elif now in (25, 26):
			res = now+ct
			if res == 27: res = 22
			if res > 27: res -= 1
			if res == 29: res = 19
			if res > 29: res = 100
		elif now in (27, 28):
			res = now+ct
			if res == 29: res = 19
			if res > 29: res = 100
		else:
			raise ValueError("something wrong")
		
		for i in combined:
			self.pieces[i] = res
		
		for j in opposite:
			if self.pieces[j] == res and res!=100: self.pieces[j] = -1
		
	def __str__(self):
		L = [
			'..----..----..----..----..----..',
			'..    ..    ..    ..    ..    ..',
			'| \                          / |',
			'|  \                        /  |',
			'|   \                      /   |',
			'|    ..                  ..    |', 
			'..   ..                  ..   ..',
			'..     \                /     ..',
			'|       \              /       |',
			'|        \            /        |',
			'|         ..        ..         |',
			'|         ..        ..         |',
			'..          \      /          ..',
			'..           \    /           ..',
			'|             \  /             |',
			'|              ..              |',
			'|              ..              |',
			'|             /  \             |',
			'..           /    \           ..',
			'..          /      \          ..',
			'|         ..        ..         |',
			'|         ..        ..         |',
			'|        /            \        |',
			'|       /              \       |',
			'..     /                \     ..',
			'..   ..                  ..   ..',
			'|    ..                  ..    |',
			'|   /                      \   |',
			'|  /                        \  |',
			'| /                          \ |',
			'..    ..    ..    ..    ..    ..',
			'..----..----..----..----..----..']
		base = []
		for i in L:base.append(list(i))

		coord = dict()
		#coordinate of A/a
		coord[0] = (24, 30)
		coord[1] = (18, 30)
		coord[2] = (12, 30)
		coord[3] = (6, 30)
		coord[4] = (0, 30)
		coord[5] = (0, 24)
		coord[6] = (0, 18)
		coord[7] = (0, 12)
		coord[8] = (0, 6)
		coord[9] = (0, 0)
		coord[10] = (6, 0)
		coord[11] = (12, 0)
		coord[12] = (18, 0)
		coord[13] = (24, 0)
		coord[14] = (30, 0)
		coord[15] = (30, 6)
		coord[16] = (30, 12)
		coord[17] = (30, 18)
		coord[18] = (30, 24)
		coord[19] = (30, 30)
		coord[20] = (5, 25)
		coord[21] = (10, 20)
		coord[22] = (15, 15)
		coord[23] = (20, 10)
		coord[24] = (25, 5)
		coord[25] = (5, 5)
		coord[26] = (10, 10)
		coord[27] = (20, 20)
		coord[28] = (25, 25)

		for i in 'ABCDabcd':
			now = self.pieces[i]
			if now == -1 or now == 100:continue
			x, y = coord[now]
			if i in 'Bb': y+=1
			elif i in 'Cc': x+=1
			elif i in 'Dd': x, y = x+1, y+1
			base[x][y] = i
		
		result = []
		for i in base:
			result.append(''.join(i))
		return '\n'.join(result)


board = Board()
for i in ' '*int(input()):
	piece, yut = input().split()
	board.play(yut, piece)
print(board)

