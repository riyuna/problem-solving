from collections import deque
import sys
input=sys.stdin.readline

class Node(dict):
		def __init__(self):
			super().__init__()
			self.final = False
			
			self.out = set()
			self.fail = None
			
		def addout(self,out):
			if type(out) is set:
				self.out = self.out.union(out)
			else :
				self.out.add(out)
		
		def addchild(self,alphabet,node = None):
			self[alphabet] = Node() if node is None else node

class AC():
	   
	def __init__(self,patterns):
		self.patterns = patterns
		self.head = Node()
		
		self.maketrie()
		self.constructfail()
		
	def search(self,sentence):
		dp=[(0,0) for i in range(len(sentence)+1)]
		dp[0]=(1, -1)
		crr = self.head
		for i, c in enumerate(sentence) :
			while crr is not self.head and c not in crr:
				crr = crr.fail
			if c in crr:
				crr = crr[c]
			
			if crr.final:
				for mem in crr.out:
					orig, cnt = d[mem]
					if not dp[i-len(mem)+1][0]:continue
					if dp[i+1][0]<dp[i-len(mem)+1][0]+cnt:
						dp[i+1]=(dp[i-len(mem)+1][0]+cnt, i-len(mem)+1)
		return dp
	
	def maketrie(self):
		for pattern in self.patterns:
			crr = self.head
			for c in pattern :
				if c not in crr:
					crr.addchild(c)
				crr = crr[c]
			crr.final = True
			crr.addout(pattern)
			
	def constructfail(self):
		queue = deque([])
		self.head.fail = self.head
		queue.append(self.head)
		while len(queue):
			crr = queue.popleft()
			for nextc in crr:
				child = crr[nextc]
				
				if crr is self.head:
					child.fail = self.head
				else :
					f = crr.fail
					while f is not self.head and nextc not in f:
						f = f.fail
					if nextc in f:
						f = f[nextc]
					child.fail = f
				
				child.addout(child.fail.out)
				child.final |= child.fail.final
				
				queue.append(child)

d=dict()
def remove_vowel(s):
	res=''
	ct=0
	for i in s:
		if i not in 'AEIOU':res+=i
		else:ct+=1
	return (res, ct)
for i in ' '*int(input()):
	s=input().strip()
	res,ct=remove_vowel(s)
	if res not in d or d[res][1]<ct:
		d[res]=(s, ct)

s=input().strip()
L=list(d.keys())

trie=AC(L)
dplist=trie.search(s)
res=[]
vowel, index=dplist[-1]
res.append(d[s[index:]][0])

while index>0:
	vowel, nextindex=dplist[index]
	res.append(d[s[nextindex:index]][0])
	index=nextindex

for i in res[::-1]:
	print(i,end=' ')