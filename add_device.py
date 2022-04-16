from lib2to3.pgen2 import token
from tkinter import ACTIVE
from unittest import result
import pynetbox
import time
dev = "R1"
def adddev(dev):
    nb = pynetbox.api(url='http://192.168.0.108:8001',token='c384a68ab0733a26c11b60ac0221180f10a86d1a')

    result = nb.dcim.devices.create(
        name='shubham',
        device_type=1,
        device_role=2,                       
        site=5,            
    )
    print(result)

adddev(dev)