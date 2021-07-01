import sys
sys.stdin = open("input.txt","rt")

N,K = map(int,input().split())
_list = list(map(int,input().split()))
_list_out=set()
for i in range(0,len(_list)-2):
    for j in range(i+1,len(_list)-1):
        for k in range(j+1,len(_list)):
            tmp = _list[i]+_list[j]+_list[k]
            _list_out.add(tmp)

_list_out=list(_list_out)
_list_out.sort(reverse=True)


print(_list_out[K-1])