import sys
sys.stdin = open("input.txt","rt")
N,K = map(int,input().split())

rtList = [i for i in range(1,N+1) if N%i==0]

if K<=len(rtList):
    print(rtList[K-1])
else :
    print(-1)