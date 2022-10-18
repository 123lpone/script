import requests
import exrex
import threading
with open("dict.text","r") as f:
    url=input("输入网站")
    def dirsearch():
        for i in f:
            r1=requests.get("http://"+url+i)    
            if r1.status_code<400:
                print(url+i)
t1=[]
for i in range(3):
    t1.append(threading.Thread(target=dirsearch))
for t in t1:
    t.start()
for t in t1:
    t.join()