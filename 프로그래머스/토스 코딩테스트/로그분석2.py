import math
import sys
sys.stdin = open("a.txt", "rt")

A = "home"
B = "transfer"
C= "account_tab"
D= "enter_account_no"
E= "enter_transfer_amount"
F= "transfer_decision"
G= "enter_password"
H= "transfer_complete"

LogNameList = [A,B,C,D,E,F,G,H]
Adict = {
    A:[], B:[],C:[],D:[],E:[],F:[],G:[],H:[]
}
Idict = {
    A:[], B:[],C:[],D:[],E:[],F:[],G:[],H:[]
}

a= int(input())

logList = []
for i in range(a):
    logList.append(list(input().split(",")))

logList.sort(key=lambda x: x[0])

for log_time, log_id, log_type, log_name, svc_id, user_no, network, os, app_ver  in logList:
    if os == "android":
        if log_name in Adict.keys() : Adict[log_name].append(user_no)

    elif os == "ios":
        if log_name in Idict.keys() : Idict[log_name].append(user_no)

AchangeList = []

IchangeList = []

for i in range(len(Adict)-1):
    allCount = len(set(Adict[LogNameList[i]]))
    visitCount = 0
    for j in Adict[LogNameList[i]]:
        if j in Adict[LogNameList[i+1]]:
            visitCount+=1

    if allCount != 0 :
        AchangeList.append(math.floor((visitCount/allCount)*100))
    else :
        AchangeList.append(0)

for i in range(len(Idict)-1):
    allCount = len(set(Idict[LogNameList[i]]))
    visitCount = 0
    for j in Idict[LogNameList[i]]:
        if j in Idict[LogNameList[i+1]]:
            visitCount+=1

    if allCount != 0 :
        IchangeList.append(math.floor((visitCount/allCount)*100))
    else :
        IchangeList.append(0)


answer = ""

for i in range(len(AchangeList)):
    if AchangeList[i] == min(AchangeList):
        answer +="android,"
        answer += LogNameList[i]
        answer += ","+ LogNameList[i+1]
        answer += ","+ str(AchangeList[i]) +"%\n"
        break

for i in range(len(IchangeList)):
    if IchangeList[i] == min(IchangeList):
        answer +="ios,"
        answer += LogNameList[i]
        answer += ","+LogNameList[i+1]
        answer += ","+str(IchangeList[i])+"%"
        break

print(answer)