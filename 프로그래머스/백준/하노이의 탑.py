n = int(input())
cnt = 0
strResult = ""
def hanoi(n, fromPos, toPos, auxPos):
    global cnt
    cnt+=1
    global strResult

    if n==1 :
        strResult += str(fromPos) + str(" ") + str(toPos) + str("\n")
        # print(fromPos, toPos)
        return
    else:
        hanoi(n-1, fromPos, auxPos, toPos)
        # print(fromPos, toPos)
        strResult += str(fromPos) + str(" ") +str(toPos)+ str("\n")
        hanoi(n-1, auxPos, toPos, fromPos)
        return


hanoi(n,1,3,2)
print(cnt)
print(strResult)

n = int(input())
def hanoi2(n,frmPos,toPos,ansPos):
    if n>1:
        hanoi2(n-1,frmPos,ansPos,toPos)

    print(frmPos,toPos)

    if n>1:
        hanoi2(n-1, ansPos,toPos,frmPos)

print(2**n-1)
hanoi2(n,1,3,2)