# -*- coding:utf-8 -*-
import sys
import socket
import json

#   1.与Juder服务器建立连接
def connect_TO_Juder_server(ip, port, token):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    return s

#   2.从服务器接收数据
def recv_data(_socket):
    nRet = -1
    Message = _socket.recv(1024 * 1024 * 4)
    print(Message)
    len_json = int(Message[:8])
    str_json = Message[8:].decode()
    if len(str_json) == len_json:
        nRet = 0
    Dict = json.loads(str_json)
    return nRet, Dict

#   3.发送数据到服务器
def send_data(socket,dict):
    str_json = json.dumps(dict)
    len_json = str(len(str_json)).zfill(8)
    str_all = len_json + str_json
    print(str_all)
    ret = socket.sendall(str_all.encode())
    if ret == None:
        ret = 0
    print('sendall', ret)
    return ret