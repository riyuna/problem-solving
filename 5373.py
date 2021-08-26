class Cube():
    def __init__(self):
        self.u=[['w']*3 for i in range(3)]
        self.f=[['r']*3 for i in range(3)]
        self.d=[['y']*3 for i in range(3)]
        self.b=[['o']*3 for i in range(3)]
        self.l=[['g']*3 for i in range(3)]
        self.r=[['b']*3 for i in range(3)]
    
    def rotate(self, param):
        if param=='L':
            self.u[0][0], self.u[1][0], self.u[2][0], self.f[0][0], self.f[1][0], self.f[2][0], self.d[0][0], self.d[1][0], self.d[2][0], self.b[0][0], self.b[1][0], self.b[2][0] = self.b[0][0], self.b[1][0], self.b[2][0], self.u[0][0], self.u[1][0], self.u[2][0], self.f[0][0], self.f[1][0], self.f[2][0], self.d[0][0], self.d[1][0], self.d[2][0]
            self.l[0][0], self.l[0][1], self.l[0][2], self.l[1][0], self.l[1][2], self.l[2][0], self.l[2][1], self.l[2][2] = self.l[2][0], self.l[1][0], self.l[0][0], self.l[2][1], self.l[0][1], self.l[2][2], self.l[1][2], self.l[0][2]

        if param=='R':
            self.u[0][2], self.u[1][2], self.u[2][2], self.f[0][2], self.f[1][2], self.f[2][2], self.d[0][2], self.d[1][2], self.d[2][2], self.b[0][2], self.b[1][2], self.b[2][2] = self.f[0][2], self.f[1][2], self.f[2][2], self.d[0][2], self.d[1][2], self.d[2][2], self.b[0][2], self.b[1][2], self.b[2][2], self.u[0][2], self.u[1][2], self.u[2][2]
            self.r[0][0], self.r[0][1], self.r[0][2], self.r[1][0], self.r[1][2], self.r[2][0], self.r[2][1], self.r[2][2] = self.r[2][0], self.r[1][0], self.r[0][0], self.r[2][1], self.r[0][1], self.r[2][2], self.r[1][2], self.r[0][2]
        if param=='U':
            self.f[0][0], self.f[0][1], self.f[0][2], self.r[0][0], self.r[0][1], self.r[0][2], self.b[2][2], self.b[2][1], self.b[2][0], self.l[0][0], self.l[0][1], self.l[0][2] = self.r[0][0], self.r[0][1], self.r[0][2], self.b[2][2], self.b[2][1], self.b[2][0], self.l[0][0], self.l[0][1], self.l[0][2], self.f[0][0], self.f[0][1], self.f[0][2]
            self.u[0][0], self.u[0][1], self.u[0][2], self.u[1][0], self.u[1][2], self.u[2][0], self.u[2][1], self.u[2][2] = self.u[2][0], self.u[1][0], self.u[0][0], self.u[2][1], self.u[0][1], self.u[2][2], self.u[1][2], self.u[0][2]
        if param=='D':
            self.f[2][0], self.f[2][1], self.f[2][2], self.r[2][0], self.r[2][1], self.r[2][2], self.b[0][2], self.b[0][1], self.b[0][0], self.l[2][0], self.l[2][1], self.l[2][2] = self.l[2][0], self.l[2][1], self.l[2][2], self.f[2][0], self.f[2][1], self.f[2][2], self.r[2][0], self.r[2][1], self.r[2][2], self.b[0][2], self.b[0][1], self.b[0][0]
            self.d[0][0], self.d[0][1], self.d[0][2], self.d[1][0], self.d[1][2], self.d[2][0], self.d[2][1], self.d[2][2] = self.d[2][0], self.d[1][0], self.d[0][0], self.d[2][1], self.d[0][1], self.d[2][2], self.d[1][2], self.d[0][2]
        if param=='F':
            self.u[2][0], self.u[2][1], self.u[2][2], self.r[0][0], self.r[1][0], self.r[2][0], self.d[0][2], self.d[0][1], self.d[0][0], self.l[2][2], self.l[1][2], self.l[0][2] = self.l[2][2], self.l[1][2], self.l[0][2], self.u[2][0], self.u[2][1], self.u[2][2], self.r[0][0], self.r[1][0], self.r[2][0], self.d[0][2], self.d[0][1], self.d[0][0]
            self.f[0][0], self.f[0][1], self.f[0][2], self.f[1][0], self.f[1][2], self.f[2][0], self.f[2][1], self.f[2][2] = self.f[2][0], self.f[1][0], self.f[0][0], self.f[2][1], self.f[0][1], self.f[2][2], self.f[1][2], self.f[0][2]
        if param=='B':
            self.u[0][0], self.u[0][1], self.u[0][2], self.r[0][2], self.r[1][2], self.r[2][2], self.d[2][2], self.d[2][1], self.d[2][0], self.l[2][0], self.l[1][0], self.l[0][0] = self.r[0][2], self.r[1][2], self.r[2][2], self.d[2][2], self.d[2][1], self.d[2][0], self.l[2][0], self.l[1][0], self.l[0][0], self.u[0][0], self.u[0][1], self.u[0][2]
            self.b[0][0], self.b[0][1], self.b[0][2], self.b[1][0], self.b[1][2], self.b[2][0], self.b[2][1], self.b[2][2] = self.b[2][0], self.b[1][0], self.b[0][0], self.b[2][1], self.b[0][1], self.b[2][2], self.b[1][2], self.b[0][2]
    def job(self, s):  # pylint: disable=E0202
        if s[1]=='+':
            self.rotate(s[0])
        else:
            self.rotate(s[0])
            self.rotate(s[0])
            self.rotate(s[0])

for i in ' '*int(input()):
    n=int(input())
    cube=Cube()
    for j in input().split():
        cube.job(j)
    L=cube.u
    print(L[0][0]+L[0][1]+L[0][2])
    print(L[1][0]+L[1][1]+L[1][2])
    print(L[2][0]+L[2][1]+L[2][2])