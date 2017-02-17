import requests, json, threading
#from time import sleep, strftime
from time import *
from tkinter import *


def getjson(url):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        return json.loads(res.text)
    except(Exception ):
        return json.loads('{"list":[0]}')


def getdata(url):
    ret = list()
    data = getjson(url)
    totalc = 0
    for n in data['list']:
        totalc += int(n)

    ret.append("\n   %s   " % url)
    ret.append("\n   totalCount : %s   " % "{:,}".format(totalc))
    for n in range(len(data['list'])):
        ret.append("   %-10s | %3s/400"% ("Server"+str(n), str( data['list'][n])))

    return ret

def updatevalue():
        text = ""
        for l in getdata():
                text = text + l + "\n"
        lb.config(text=text, justify="left", font = ('굴림체', 10))

def monitor(url):

    root=Tk()
    lb = Label(root);
    lb.pack(anchor = "w")
    #data = getdata(url)

    while(1):
        text = ""
        for l in getdata(url):
            text = text + l + "\n"
        lb.config(text=text, justify="left", font = ('굴림체', 10))

        root.update()

        
day = time()
"""while(1):
    if time() - day > 1:
        for n in getdata():
            print(n)
        day = time()
    else:
        pass

"""
#l = ['http://kkutu.co.kr/servers','http://kkutu.kr/servers','http://kkutu.io/servers']
l = ['http://kkutu.co.kr/servers', 'http://kkutu.io/servers']
for url in l:
    threading.Thread(target=monitor, args=[url]).start()

