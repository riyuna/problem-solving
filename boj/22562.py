import sys
input=sys.stdin.readline
from math import ceil
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
h,a,d,s=linput()
L=[]
mem=[]
dam=0
for i in ' '*n:L.append(linput())
for hi, ai, di, si in L:
	fast=True if s>si else False
	attack_me=max(a-di,0)
	attack_other=max(ai-d,0)
	if attack_me==0:need_turn=10**20
	else:need_turn=ceil(hi/attack_me)-fast

	if need_turn==0:need_turn=1e-10
	mem.append([hi, ai, di, si, need_turn, attack_other])
	dam+=attack_other
mem.sort(key=lambda x:x[5]/x[4])
flag=True
orig_h=h
for monster in mem:
	damage=int(monster[-2])*dam
	if damage>=h:
		flag=False
		break
	else:
		h-=damage
		dam-=monster[-1]
print(orig_h-h if flag else -1)