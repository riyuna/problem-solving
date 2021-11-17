from math import gcd
def P1(x1,y1,x2,y2,x3,y3):
    X1,X2,X3,Y1,Y2,Y3=abs(x1-x2), abs(x2-x3), abs(x3-x1), abs(y1-y2), abs(y2-y3), abs(y3-y1)
    return gcd(X1,Y1)+gcd(X2,Y2)+gcd(X3,Y3)

############### SUBMIT THE CODE ABOVE ONLY ###############

print(P1(0,0,2,2,3,0)) # 6
