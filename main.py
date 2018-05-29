# -*- coding:utf-8 -*-
import sys
import socket
import json
import Juder
#用户自定义函数, 返回字典FlyPlane, 需要包括 "UAV_info", "purchase_UAV" 两个key.
def AlgorithmCalculationFun(a, b, c):
    FlyPlane = c["astUav"]
    
    return FlyPlane




#################################################################################
#               主函数     cbc8a7aa42312233672871941d7f728022b5d426
def main(szIp, nPort, szToken):
    print("server ip %s, prot %d, token %s\n", szIp, nPort, szToken)

    #   1.开始连接服务器
    hSocket =Juder.connect_TO_Juder_server(szIp,nPort,szToken)

    #   2.链接裁判服务器#b'00000052{"notice":"token","msg":"hello, what\'s your token?"}'
    nRet, _ = Juder.recv_data(hSocket)
    if (nRet != 0):
        return nRet
    #   3.选手向裁判服务器表明身份(Player -> Judger)
    my_token = {}
    my_token["token"] = szToken
    my_token["action"] = "sendtoken"
    nRet = Juder.send_data(hSocket,my_token)
    if(nRet != 0):
        return nRet
    #   4.获取身份验证结果
    nRet,Message = Juder.recv_data(hSocket)
    if (nRet != 0):
        return nRet
    print("Message:"+Message)
    return 0

if __name__ == "__main__":
    if len(sys.argv) == 4:
        print("Server Host: " + sys.argv[1])
        print("Server Port: " + sys.argv[2])
        print("Auth Token: " + sys.argv[3])
        main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    else:
        print("need 3 arguments")