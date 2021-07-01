import sys
sys.stdin = open("input.txt","rt")


N=int(input())
_list = list(map(int,input().split()))

avg = sum(_list)/N

_stdList=[]

for s in _list:
    _stdList