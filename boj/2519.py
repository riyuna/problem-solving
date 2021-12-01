import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

##########################################
def reverse_edges(adj):
    adj_rev = dict()
    for u in adj:
        adj_rev[u] = []
    for u in adj:
        for v in adj[u]:  # (u,v) is an edge
            adj_rev[v].append(u)
    return adj_rev

##########################################
def DFS_forward(adj, u, visited, node_stack):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            DFS_forward(adj, v, visited, node_stack)
    node_stack.append(u)

def DFS_backward(adj_rev, u, visited, scc):
    visited.append(u)
    for v in adj_rev[u]:
        if v not in visited:
            DFS_backward(adj_rev, v, visited, scc)
    scc.append(u)

##########################################
def find_SCC(adj):
    visited_forward = []
    node_stack = []
    for u in adj:
        if u not in visited_forward:
            DFS_forward(adj, u, visited_forward, node_stack)

    adj_rev = reverse_edges(adj)
    visited_backward = []
    sccs = []  # list of SCCs
    for i in range(len(adj)):
        u = node_stack.pop()
        if u not in visited_backward:
            scc = []
            DFS_backward(adj_rev, u, visited_backward, scc)
            sccs.append(scc)

    return sccs

def build_implication_graph(P):
    k = len(P)  # number of clauses
    n = 1  # number of variables
    for j in range(k):  n = max(n, abs(P[j][0]), abs(P[j][1]))

    adj = dict()
    for i in range(1,n+1):  adj[i], adj[-i] = [], []
    
    for j in range(k):
        u, v = P[j]
        adj[-u].append(v)
        adj[-v].append(u)

    return adj, n

##################################################
def solve_2SAT(P):
    adj, n = build_implication_graph(P)
    sccs = find_SCC(adj)
    sccID = dict()  # sccID[u]: scc id of node u
    for h in range(len(sccs)):
        scc = sccs[h]
        for u in scc: sccID[u] = h
    
    # satisfiable <=> \forall i, x_i and \overline{x_i} belong to different scc
    for i in range(1,n+1):
        if sccID[i] == sccID[-i]:
            return None  # not satisfiable

    truth_assignment = [None] * n
    for i in range(n):
        truth_assignment[i] = sccID[i+1] > sccID[-(i+1)]
    
    return truth_assignment
        
#################################################################
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

n=int(input())
L=[]
for i in range(n):
    L.append([-(i*3+1), -(i*3+2)])
    L.append([-(i*3+1), -(i*3+3)])
    L.append([-(i*3+2), -(i*3+1)])
    L.append([-(i*3+2), -(i*3+3)])
    L.append([-(i*3+3), -(i*3+1)])
    L.append([-(i*3+3), -(i*3+2)])

ptL=[]
for i in ' '*n*3:
    a,b,c,d=map(int,input().split())
    ptL.append([a,b,c,d])
for i in range(n*3):
    for j in range(i):
        a,b,c,d=ptL[i]
        e,f,g,h=ptL[j]
        if cross(a,b,c,d,e,f,g,h):
            L.append([i+1, j+1])
            L.append([j+1, i+1])

M=solve_2SAT(L)
if M==None:print(-1)
else:
    res=[]
    for i in range(n*3):
        if M[i]:res.append(i+1)
    print(len(res))
    for i in res:print(i,end=' ')