# ADD Devices using text file
from lib2to3.pgen2 import token
from tkinter import ACTIVE
from unittest import result
import pynetbox
import time
dev = "R1"
def adddev(dev):
    nb = pynetbox.api(url='http://192.168.0.108:8001',token='c384a68ab0733a26c11b60ac0221180f10a86d1a')

    result = nb.dcim.devices.create(
        name=dev,
        device_type=1,
        device_role=2,                       
        site=5,            
    )
    print(result)

file1 = open('C:\\shubhamnet\\hosts.txt','r')
lines = file1.readlines()
# print(lines)
count = 0
#strips the newline character
for line in lines:
    count += 1
    # time.sleep(0.4)
    dev = line
    # print(dev)
    adddev(dev)