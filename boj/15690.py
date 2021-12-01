from collections import deque
s=input()
L=s.split('. ')
L[-1]=L[-1].strip('.')
for i in range(len(L)):
    L[i]=L[i].split()
mem=dict()
graph=[]
ct=0
for i in L:
    for j in i:
        j=j.strip(',')
        if j not in mem:
            mem[j]=ct
            ct+=1
            graph.append(set())
            graph.append(set())

comma=[False]*len(graph)

for lis in L:
    for j in range(len(lis)-1):
        a,b=lis[j],lis[j+1]
        aa,bb=a.strip(','), b.strip(',')
        inda, indb=mem[aa]*2+1, mem[bb]*2
        graph[inda].add(indb)
        graph[indb].add(inda)
        if a[-1]==',':
            comma[inda]=True
            comma[indb]=True


q=deque([])
for i in range(len(comma)):
    if comma[i]:q.append(i)

while len(q):
    pt=q.popleft()
    for i in graph[pt]:
        if not comma[i]:
            comma[i]=True
            q.append(i)

for lis in L:
    for j in range(len(lis)-1):
        word=lis[j].strip(',').strip('.')
        print(word,end='')
        print(',' if comma[mem[word]*2+1] else '',end=' ')
    print(lis[-1],end='. ')