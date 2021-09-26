def pibo(n):
    if n== 0 or n==1 : return n
    else : return pibo(n-1)+ pibo(n-2)

n = int(input())

print(pibo(n))