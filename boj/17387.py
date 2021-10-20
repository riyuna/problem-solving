x1, y1, x2, y2=map(int,input().split())
x3, y3, x4, y4=map(int,input().split())
def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1=ccw(x1,y1,x2,y2,x3,y3)
    ccw2=ccw(x1,y1,x2,y2,x4,y4)
    ccw3=ccw(x3,y3,x4,y4,x1,y1)
    ccw4=ccw(x3,y3,x4,y4,x2,y2)
    if ccw1*ccw2==ccw3*ccw4==0:
        if x1==x2==x3==x4:
            return not(min(y3,y4)>max(y1,y2) or min(y1,y2)>max(y3,y4))
        return not(min(x3,x4)>max(x1,x2) or min(x1,x2)>max(x3,x4))
    return ccw1*ccw2<=0 and ccw3*ccw4<=0

print([0,1][cross(x1,y1,x2,y2,x3,y3,x4,y4)])