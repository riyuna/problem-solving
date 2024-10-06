import sys
input=sys.stdin.readline

class Point:
	def __init__(self, x, y):
		self.x=x
		self.y=y

n=int(input())

pts=[]
for i in ' '*int(input()):
	x,y=map(int,input().split())
	pts.append(Point(x,y))

