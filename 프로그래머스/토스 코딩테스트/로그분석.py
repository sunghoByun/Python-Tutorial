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
Idict2 = {
    A:[], B:[],C:[],D:[],E:[],F:[],G:[],H:[]
}

print(Adict)


Alog_time=[]
Alog_id=[]
Alog_type=[]
Alog_name=[]
Asvc_id=[]
Auser_no=[]
Anetwork=[]
Aos=[]
Aapp_ver=[]

Ilog_time=[]
Ilog_id=[]
Ilog_type=[]
Ilog_name=[]
Isvc_id=[]
Iuser_no=[]
Inetwork=[]
Ios=[]
Iapp_ver=[]

a= int(input())

logList = []
for i in range(10):
    logList.append(list(input().split(",")))

logList.sort(key=lambda x: x[0])


#
# for i in range(10):
#     log_time, log_id, log_type, log_name, svc_id, user_no, network, os, app_ver = input().split(",")
#     if os == "android":
#         if log_name in Adict.keys() : Adict[log_name].append(user_no)
#         Alog_type.append(log_time)
#         Alog_id.append(log_id)
#         Alog_type.append(log_type)
#         Alog_name.append(log_name)
#         Asvc_id.append(svc_id)
#         Auser_no.append(user_no)
#         Anetwork.append(network)
#         Aos.append(os)
#         Aapp_ver.append(app_ver)
#     elif os == "ios":
#         if log_name in Idict.keys() : Idict[log_name].append(user_no)
#         Ilog_time.append(log_time)
#         Ilog_id.append(log_id)
#         Ilog_type.append(log_type)
#         Ilog_name.append(log_name)
#         Isvc_id.append(svc_id)
#         Iuser_no.append(user_no)
#         Inetwork.append(network)
#         Ios.append(os)
#         Iapp_ver.append(app_ver)
#
# for i in range(len(Ilog_time)):
#     print(Ilog_name[i], Iuser_no[i])

