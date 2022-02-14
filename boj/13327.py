import sys
import heapq
INP=iter(sys.stdin.read().split())
input = lambda: next(INP)


class Wood:
	def __init__(self, is_hori, st_pos, length):
		self.is_hori = is_hori
		self.is_verti = not is_hori
		self.st_pos = st_pos
		self.length = length


def distance(wood1, wood2):
	if wood1.is_verti:
		if wood2.is_verti:
			ys1 = wood1.st_pos[1]
			ye1 = ys1 + wood1.length
			
			ys2 = wood2.st_pos[1]
			ye2 = ys2 + wood2.length
			
			dx = abs(wood1.st_pos[0] - wood2.st_pos[0])
			
			if ys1 <= ys2 <= ye1 or ys1 <= ye2 <= ye1:
				return dx**2
			elif ys2 <= ys1 <= ye2 or ys2 <= ye1 <= ye2:
				return dx**2
			elif ye2 < ys1:
				return dx**2 + (ys1 - ye2)**2
			return dx**2 + (ys2 - ye1)**2
		
		return distance(wood2, wood1)
	
	if wood2.is_hori:
		xs1 = wood1.st_pos[0]
		xe1 = xs1 + wood1.length
		
		xs2 = wood2.st_pos[0]
		xe2 = xs2 + wood2.length
		
		dy = abs(wood1.st_pos[1] - wood2.st_pos[1])
		
		if xs1 <= xs2 <= xe1 or xs1 <= xe2 <= xe1:
			return dy**2
		elif xs2 <= xs1 <= xe2 or xs2 <= xe1 <= xe2:
			return dy**2
		elif xe2 < xs1:
			return dy**2 + (xs1 - xe2)**2
		return dy**2 + (xs2 - xe1)**2
	
	xs1 = wood1.st_pos[0]
	xe1 = xs1 + wood1.length
	
	x2 = wood2.st_pos[0]
	
	y1 = wood1.st_pos[1]
	
	ys2 = wood2.st_pos[1]
	ye2 = ys2 + wood2.length
	
	if xs1 <= x2 <= xe1:
		dx = 0
	elif xe1 < x2:
		dx = x2 - xe1
	else:
		dx = xs1 - x2
	
	if ys2 <= y1 <= ye2:
		dy = 0
	elif ye2 < y1:
		dy = y1 - ye2
	else:
		dy = ys2 - y1
	
	return dx**2 + dy**2


def build_graph():
	global adj_list, n, m, w, l
	
	adj_list = [[] for _ in range(w+2)]
	
	for i in range(w):
		min_dist = n**2 + m**2 + 1
		
		for st_wood in start:
			min_dist = min(min_dist, distance(wood[i], st_wood))
		
		if min_dist <= l:
			adj_list[0].append((i+1, min_dist))
	
	for i in range(w):
		for j in range(i+1, w):
			dist = distance(wood[i], wood[j])
			
			if dist <= l:
				adj_list[i+1].append((j+1, dist))
				adj_list[j+1].append((i+1, dist))
	
	for i in range(w):
		min_dist = n**2 + m**2 + 1
		
		for ed_wood in end:
			min_dist = min(min_dist, distance(wood[i], ed_wood))
		
		if min_dist <= l:
			adj_list[i+1].append((w+1, min_dist))
	
	min_dist = n**2 + m**2 + 1
	for st_wood in start:
		for ed_wood in end:
			min_dist = min(min_dist, distance(st_wood, ed_wood))
	
	if min_dist <= l:
		adj_list[0].append((w+1, min_dist))


if __name__ == "__main__":
	n=int(input())
	m=int(input())
	u=int(input())
	v=int(input())
	w=int(input())
	l=int(input())

	
	start = []
	wood = []
	end = []
	
	xb=int(input())
	yb=int(input())
	for _ in range(u-1):
		xf=int(input())
		yf=int(input())
		
		if xf == xb:
			start.append(Wood(False, (xf, min(yf, yb)), abs(yf - yb)))
		else:
			start.append(Wood(True, (min(xf, xb), yf), abs(xf - xb)))
		
		xb, yb = xf, yf
	
	xb=int(input())
	yb=int(input())
	for _ in range(v-1):
		xf=int(input())
		yf=int(input())
		
		if xf == xb:
			end.append(Wood(False, (xf, min(yf, yb)), abs(yf - yb)))
		else:
			end.append(Wood(True, (min(xf, xb), yf), abs(xf - xb)))
		
		xb, yb = xf, yf
	
	for _ in range(w):
		x1=int(input())
		y1=int(input())
		x2=int(input())
		y2=int(input())
		
		if x1 == x2:
			wood.append(Wood(False, (x1, min(y1, y2)), abs(y2 - y1)))
		else:
			wood.append(Wood(True, (min(x1, x2), y1), abs(x2 - x1)))
	
	adj_list = []
	build_graph()
	
	heap = []
	dist = [-1 for _ in range(w+2)]

	heapq.heappush(heap, (0, 0))

	while heap:
		d, p = heapq.heappop(heap)

		if dist[p] != -1:
			continue

		dist[p] = d

		for nx, dd in adj_list[p]:
			if dist[nx] != -1:
				continue

			heapq.heappush(heap, (d+dd, nx))

	print(dist[w+1])
