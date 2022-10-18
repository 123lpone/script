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
    for i in range(10,101):
        ipque.put((str(ip),i))

#检测tcp    
def scantcp(queue):
    while not queue.empty():
        s=socket.socket() #建立套接字tcp
        s.settimeout(2)
        ipp=queue.get()
        exp=s.connect_ex(ipp)
        if exp:
            pass
        else:
            print(ipp)


#建立线程
tasklist=[]
for i in range(5):
    if typ=="tcp":
        t=threading.Thread(target=scantcp,args=(ipque,),daemon=TRUE)
        tasklist.append(t)
for i in tasklist:
    i.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(1) 