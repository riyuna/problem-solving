def list_to_table(L):
    a=len(L)
    b=len(L[0][1])
    table = [[0]*a for i in range(b+1)]
    for i in range(a):
        table[0][i]=i
    for i in range(b):
        for j in range(a):
            table[i+1][j]=L[j][1][i]
    return table

def finding_road_start_x(table,x,y):
    a=len(L)
    b=x
    l=[None]*a
    l[0]=b
    counter=1
    while counter<a:
        i=1
        while l[counter]==None:
            if i>=len(table):
                return "None"
            c=table[i][b]
            if c not in l:
                l[counter]=c
                b=c
                counter=counter+1
                break
            if c in l:
                i=i+1
    return l
            
def finding_road(table,x,y):
    for i in range(x):
        l = finding_road_start_x(table,i,y)
        if not l == "None":
            return l
    return l

n = raw_input("put the number of chapters ")
n = int(n)
#put n
m = raw_input("put the number of referencing different chapters in one chapter ")
m = int(m)
#put m
L = [[i] + [[None]*m] for i in range(n)]
#make L
print L
i = 0
j = 0
for i in range (n):
    for j in range (m):
        print "put the ",i,"th book's ",j+1,"th referencing"
        L[i][1][j] = int(raw_input())
        
print L
#put data

#L=[[0,[0,1]],[1,[2,3]],[2,[0,3]],[3,[0,4]],[4,[4,4]]]
a=len(L)
b=len(L[0][1])
table = list_to_table(L)
print finding_road(table,a,b)
