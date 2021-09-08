import sys
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

lines = sys.stdin.readlines()
def pon_input():
    line=lines.pop(0)
    return line

while lines:
    n,m = map(int,pon_input().split())
    L=[]
    for i in ' '*m:L.append(list(map(int,pon_input().split())))
    L.append([1, 1])
    M=solve_2SAT(L)
    if M==None:print('no')
    else:print('yes')