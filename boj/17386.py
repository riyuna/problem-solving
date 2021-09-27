x1, y1, x2, y2=map(int,input().split())
x3, y3, x4, y4=map(int,input().split())
def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    return ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<0

print([0,1][cross(x1,y1,x2,y2,x3,y3,x4,y4)])