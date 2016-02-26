import base64
import json
import requests
import simplejson
from collections import OrderedDict
import sys
import os

data = '[{"pk":[-1],"t":5,"parents":{"p1":{"pk":[-2]},"p2":{"pn":1,"pk":[-1,2]}},"ip":"134.88.54.224","user":"stevenf12"},{"pk":[],"t":20,"parents":{"p1":{"pn":0,"pk":[1]},"p2":{"pk":[-1]}},"ip":"134.88.54.224","user":"stef12"}]'
#data = '[{"pn":12,"pk":[-6],"t":14,"parents":{"p1":{"pn":11,"pk":[5]},"p2":{"pn":3,"pk":[-5,-6]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":13,"pk":[-2],"t":26,"parents":{"p1":{"pn":12,"pk":[-6]},"p2":{"pn":7,"pk":[-2,6]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":14,"pk":[-1],"t":42,"parents":{"p1":{"pn":13,"pk":[-2]},"p2":{"pn":0,"pk":[-1,2]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":15,"pk":[-7],"t":48,"parents":{"p1":{"pn":14,"pk":[-1]},"p2":{"pn":4,"pk":[-7,1]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":16,"pk":[-10],"t":57,"parents":{"p1":{"pn":15,"pk":[-7]},"p2":{"pn":8,"pk":[-10,7]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":17,"pk":[4],"t":66,"parents":{"p1":{"pn":16,"pk":[-10]},"p2":{"pn":5,"pk":[10,4]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":18,"pk":[3],"t":84,"parents":{"p1":{"pn":17,"pk":[4]},"p2":{"pn":2,"pk":[-4,3]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":19,"pk":[-9],"t":94,"parents":{"p1":{"pn":18,"pk":[3]},"p2":{"pn":9,"pk":[-3,-9]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":20,"pk":[-8],"t":100,"parents":{"p1":{"pn":19,"pk":[-9]},"p2":{"pn":6,"pk":[-8,9]}},"ip":"134.88.255.66","user":"mcoughlin3"},{"pn":21,"pk":[],"t":112,"parents":{"p1":{"pn":20,"pk":[-8]},"p2":{"pn":10,"pk":[8]}},"ip":"134.88.255.66","user":"mcoughlin3"}]'

datas = "{"+'"'+"root"+'"'+":"+data+"}"
JSdata = json.loads(datas)
#type(data)
#type(JSdata)
#print JSdata
#print JSdata

parent = JSdata["root"]
#print parent
#print data[1]
for item in parent:
    print item["user"]
    for x in range(1,3):
        p = "p"+str(x) #since 2 pieces make a single piece 
        if 'pn' in item["parents"][p]: #checking if key pn exists 
            print "number =>", item["parents"][p]["pn"]
        print "pieces = >" ,item["parents"][p]["pk"]
    #print item[]
    
    #print item.get()
#for item in parent:
#    print item["pn"]


