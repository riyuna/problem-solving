import sys
import math
import random
from copy import deepcopy


input = sys.stdin.readline
err = 1e-5


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y) 
    
    def __pow__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __abs__(self):
        return self ** self
    
    def dist(self, other):
        res = self-other
        return abs(res)**0.5


class Circle:
    __slots__ = ('ctr', 'rad', 'active')
    
    def __init__(self, ctr: Point, rad):
        self.ctr = ctr
        self.rad = rad
        self.active = [(0, 2 * math.pi)]
    
    def __str__(self):
        return f"{self.ctr}, {self.rad}"
    
    def deactivate(self, st, ed):
        if st > ed:
            self.deactivate(st, 2 * math.pi)
            self.deactivate(0, ed)
            return
        
        new_active = []
        
        for ist, ied in self.active:
            if ied <= st or ed <= ist:
                new_active.append((ist, ied))
            else:
                if st - ist > err:
                    new_active.append((ist, st))
                if ied - ed > err:
                    new_active.append((ed, ied))
        
        self.active = new_active
def adjust_angle(angle):
    while angle < 0:
        angle += 2 * math.pi
    while angle > 2 * math.pi:
        angle -= 2 * math.pi
    return angle
def circle_intersect(c1: Circle, c2: Circle):
    ctr_dist = c1.ctr.dist(c2.ctr)
    
    if ctr_dist > c1.rad + c2.rad:
        return
    
    if c1.rad + ctr_dist <= c2.rad:
        c1.active = []
        return
    
    if c2.rad + ctr_dist <= c1.rad:
        c2.active = []
        return
    
    angle1 = math.acos((-c2.rad**2 + c1.rad**2 + ctr_dist**2)/(2 * c1.rad * ctr_dist))
    angle2 = math.acos((-c1.rad**2 + c2.rad**2 + ctr_dist**2)/(2 * c2.rad * ctr_dist))
    
    dvec = c2.ctr - c1.ctr
    angle = math.atan(dvec.y / dvec.x) if dvec.x != 0 else (math.pi / 2 if dvec.y > 0 else 3 * math.pi / 2)
    if dvec.x < 0:
        angle += math.pi
    
    angle1_st = adjust_angle(angle - angle1)
    angle1_ed = adjust_angle(angle + angle1)
    
    angle2_st = adjust_angle(math.pi + angle - angle2)
    angle2_ed = adjust_angle(math.pi + angle + angle2)
    
    c1.deactivate(angle1_st, angle1_ed)
    c2.deactivate(angle2_st, angle2_ed)


def find_composition(circles):
    for i in range(len(circles)):
        for j in range(i+1, len(circles)):
            circle_intersect(circles[i], circles[j])


def check_circle_in_circle(circles):
    real = []

    for i in range(len(circles)):
        c1 = circles[i]
        is_real = True
        for j in range(len(circles)):
            if i == j:
                continue
            c2 = circles[j]

            ctr_dist = c1.ctr.dist(c2.ctr)

            if abs(c1.rad + ctr_dist - c2.rad) < err:
                is_real = False
                break
        
        if is_real:
            real.append(c1)
    
    return real


def solve(n, circles):
    circles = check_circle_in_circle(circles)
    cnt = n - len(circles)
    n = len(circles)
    
    total = deepcopy(circles)
    find_composition(total)
    
    for i in range(n):
        if total[i].active:
            continue
        
        target = circles[i]
        circles.pop(i)
        find_composition(circles)
        nonactive = True
        
        for j in range(n-1):
            k = j if j < i else j+1
            
            if total[k].active != circles[j].active:
                nonactive = False
        
        if nonactive:
            cnt += 1
        
        for circle in circles:
            circle.active = [(0, 2 * math.pi)]
        circles.insert(i, target)
    
    return cnt

def area(circles):
    res=0
    for circle in circles:
        for start, end in circle.active:
            res+=(0.5*circle.rad*(circle.ctr.x*math.sin(end)-circle.ctr.y*math.cos(end)+circle.rad*end))
            res-=(0.5*circle.rad*(circle.ctr.x*math.sin(start)-circle.ctr.y*math.cos(start)+circle.rad*start))
    return res

def area_t(circles, time):
    new_circles = []
    for circle in circles:
        new_circles.append(deepcopy(circle))
        new_circles[-1].rad+=time
        if new_circles[-1].rad<0:new_circles[-1].rad=0
    find_composition(new_circles)
    return area(new_circles)

def main():
    n=int(input())
    circles = []

    for _ in range(n):
        x, y, r1, r2 = map(float, input().split())
        circles.append(Circle(Point(x, y), -r1))
    st = 0
    ed = 10**9
    while ed-st>1e-7:
        mid = (st+ed)/2
        res = area_t(circles,mid)
        if res>a:
            ed = mid
        else:
            st = mid
    return mid

for i in range(int(input())):
	res = main()
	print (f"Case {i+1}: {res}")

