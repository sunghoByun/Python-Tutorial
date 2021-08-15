import collections

v = [[1, 4], [3, 4], [3, 10]]

X = dict()
Y = dict()
xx= 0
yy = 0
for x,y in v:
    if x not in X.keys():
        X[x]= 1
    elif x in X.keys():
        X[x] +=1

    if x not in Y.keys():
        Y[y] = 1
    elif y in Y.keys():
        Y[y] +=1

for k,v in X.items():
    if v == 1:
        xx = k
for k,v in Y.items():
    if v == 1:
        yy = k

print(xx,yy)
