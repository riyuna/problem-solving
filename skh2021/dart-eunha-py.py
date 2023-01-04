from functools import cmp_to_key
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

L=[]

def cmp(a, b):
    return (a > b) - (a < b) 

def cmp1(tp1, tp2):
    if tp1[1]!=tp2[1]:return cmp(tp1[1],tp2[1])
    return cmp(tp1[0],tp2[0])

def cmp2(tp1, tp2):
    if tp1[1]*tp2[0] != tp1[0]*tp2[1]: return cmp(tp1[1]*tp2[0], tp1[0]*tp2[1])
    if tp1[1]!=tp2[1]: return cmp(tp1[1],tp2[1])
    return cmp(tp1[0],tp2[0])

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

