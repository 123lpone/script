from pickle import TRUE
from IPy import IP
import socket
import queue
import threading
import time
import sys
ipque=queue.Queue()
addr=input("输入IP地址>>>")
typ="tcp"
typ=typ.lower()
ips=IP(str(addr))
iplist=[]
for ip in ips:
    ipque.put(ip)

#检测tcp    
def scantcp(queue):
    while not queue.empty():
        ip=queue.get()
        s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM) #建立套接字tcp
        for i in range(22,101):
            ipport=(str(ip),i)
            s.settimeout(2)
            exp=s.connect_ex(ipport)
            if exp:
                print("地址{}:端口:{}--close".format(ip,i))
            else:
                print("地址{}:端口:{}--tcp".format(ip,i))


#建立线程
tasklist=[]
for i in range(5):
    if typ=="tcp":
        t=threading.Thread(target=scantcp,args=(ipque,),daemon=TRUE)
        tasklist.append(t)
    elif typ=="udp":
        t=threading.Thread(target=scanudp,args=(ipque,),daemon=TRUE)
        tasklist.append(t)
for i in tasklist:
    i.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(1) 