#coding=utf-8
from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
bindAddr = ('',7788)
udpSocket.bind(bindAddr)

recvData = udpSocket.recvfrom(1024)
print(recvData)

udpSocket.close()