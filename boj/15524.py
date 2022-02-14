import sys
from fractions import Fraction
from itertools import combinations


input = sys.stdin.readline


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __pow__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __floordiv__(self, other):
        return self.x * other.y - self.y * other.x


class Line:
    def __init__(self, u, v):
        self.u = u
        self.v = v
    
    def dist(self, vec):
        return Fraction(abs((self.u - vec) // self.v)**2, self.v ** self.v)
    
    def finaldist(self, vec):
        d = Vector(self.v.y, -self.v.x)
        left = (self.u - vec) // d
        right = (self.u + self.v - vec) // d
        
        if left < 0:
            p = (self.u - vec)
            return p ** p
        
        if right > 0:
            p = (self.u + self.v - vec)
            return p ** p
        
        return self.dist(vec)


if __name__ == "__main__":
    n = int(input())
    
    coin_info = []
    
    for _ in range(n):
        r, sxi, syi, txi, tyi = map(int, input().split())
        coin_info.append([r, Vector(sxi, syi), Vector(txi, tyi)])
    
    movable = [[[None, None] for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                movable[i][j] = [True, True]
            
            radius, start, end = coin_info[i]
            line = Line(start, end-start)
            
            dist1 = line.finaldist(coin_info[j][1])
            dist2 = line.finaldist(coin_info[j][2])
            
            pos1 = True
            pos2 = True
            if dist1 < (radius + coin_info[j][0])**2:
                pos1 = False
            if dist2 < (radius + coin_info[j][0])**2:
                pos2 = False
            
            movable[i][j] = [pos1, pos2]
    
    # print(movable)

    bitdp=[0]*(2**n)
    bitdp[0]=1
    bitlist=[i for i in range(n)]
    answer=0
    for i in range(1, n+1):
        comb=list(combinations(bitlist, i))
        for tup in comb:
            res=0
            for k in tup:
                res^=2**k
            for k in tup:
                before=res^2**k
                if bitdp[before]:
                    state=True
                    for j in range(n):
                        if j==k:continue
                        if j in tup:
                            if not movable[k][j][1]:
                                state=False
                                break
                        else:
                            if not movable[k][j][0]:
                                state=False
                                break
                    if state:
                        answer=max(answer,i)
                        bitdp[res]=1
    
print(answer)