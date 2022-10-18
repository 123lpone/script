import hashlib
import queue
from string import hexdigits
import sys
import threading
import requests
import time
url=input("请输入网站>>>")
num=int(input("请输入线程个数>>>"))
dictlist=[]
listque=queue.Queue()
with open("C:\\Users\\10979\\Desktop\\script\\cms.txt","r",encoding="utf8") as f:
    for i in f:
        listque.put(i.strip())

#扫描字典
def work(queue,url):
    while not queue.empty():
        i=queue.get()
        dictlist=i.split("|")
        header={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
        }
        try:
            r=requests.get("http://"+url+dictlist[0],timeout=1,headers=header)
            
            if r.status_code<400:
                hash=hashlib.md5(r.content)
                if hash.hexdigest()==dictlist[2]:
                    print("{}，采用{}".format(url,dictlist[1]))
                    return
                else:
                    continue
        except Exception as e:
            pass
    print("未找到cms")
#准备线程
def thread(num):
    taskslist=[]
    for i in range(num):
        t=threading.Thread(target=work,args=(listque,url),daemon=True)
        taskslist.append(t)
    for i in taskslist:
        i.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(1)

thread(num)