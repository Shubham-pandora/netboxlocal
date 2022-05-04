from re import I
from turtle import pensize
import ipcalc
import networkscan
from netbox import NetBox
import requests
import socket
import json

headers = {
    'content-type': "application/json",
    'authorization': "Token c384a68ab0733a26c11b60ac0221180f10a86d1a",
    'cache-control': "no-cache",
    'postman-token': "356fdcce-4d66-a618-1d36-f44f4588d057"
    }
NB_URL = "http://192.168.0.108"
netbox = NetBox(host='192.168.0.108',port=8001, use_ssl=False,auth_token='c384a68ab0733a26c11b60ac0221180f10a86d1a')

if __name__ == '__main__':
        
    InstanceData ="""{   
    "192.168.2.92": "Veeru",
    "192.168.1.23": "Dhananjay",
    "192.168.1.32": "Pavankumar",
    "192.168.1.77": "Venu",
    "192.168.1.85": "Deepika",
    "192.168.1.94": "ganesh",
    "192.168.1.101": "SmartBox6",
    "192.168.1.102": "alpha1-101.pandorarndlabs.net",
    "192.168.1.103": "alpha1-102.pandorarndlabs.net",
    "192.168.1.104": "alpha1-102.pandorarndlabs.net",
    "192.168.1.114": "alpha1-103.pandorarndlabs.net",
    "192.168.1.115": "alpha1-110.pandorarndlabs.net",
    "192.168.1.118": "localhost.localdomain",
    "192.168.1.119": "localhost.localdomain",
    "192.168.1.147": "localhost.localdomain",
    "192.168.1.172": "localhost.localdomain",
    "192.168.1.23":"Bhargav"
    }"""
    print(InstanceData)
    # load the json data
    Ins = json.loads(InstanceData)
    print(Ins)
    #define the network to scan
    my_network = "192.168.0.0/22"
    #create the object
    my_scan = networkscan.Networkscan(my_network)
    # Run the scan of hosts using pings
    my_scan.run()
    # Here we define exits IP address  in our N/W and write it to list
    found_ip_in_network = []
    for address1 in my_scan.list_of_hosts_found:
        found_ip_in_network.append(str(address1)) 

    print(found_ip_in_network)   

    # Get all IP from prefix
    for ipaddress in ipcalc.Network(my_network):
        # Doing get request to netbox
        request_url = f"{NB_URL}/api/ipam/ip-addresses/?q={ipaddress}/"
        ipaddress1 = requests.get(request_url,headers=headers)
        netboxip = ipaddress1.json()
        print(ipaddress)
        # print(type(ipaddress))   type of ipaddress is -> <class 'ipcalc.IP'>
        # print(netboxip)
        print(netboxip['count'])    
        # if not in netbox
        if netboxip['count'] == 0:
            print("IP not in netbox",ipaddress)           
            # check if in network exists and not exists in netbox
            if ipaddress in found_ip_in_network:
                print("IPaddress found in  is - network :", ipaddress)
                print("--------------------------")
                print(ipaddress , Ins)             
                if str(ipaddress) in Ins:
                    print("Found")
                    print("%s is found in JSON data" %ipaddress)
                    print("The value of", str(ipaddress),"is", Ins[str(ipaddress)])                     
                    # Adding in IP netbox            
                    print("------------------------")
                    netbox.ipam.create_ip_address(str(ipaddress),dns_name=Ins[str(ipaddress)])
                else:
                    netbox.ipam.create_ip_address(str(ipaddress),dns_name="Unknown")
                    print("Not---------")
                    
            else:
                print("Faild")
        else:
            print("IP in netbox",ipaddress)

      
