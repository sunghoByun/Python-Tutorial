N = int(input())

def pac(n):
    n = int(n)
    if n==1 or n == 0 : return 1
    return n * pac(n-1)

print(pac(N))