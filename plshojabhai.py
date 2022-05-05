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
    "192.168.0.6":"sparkmaster3",
    "192.168.0.108": "alpha2-209.pandorarndlabs.net",
    "192.168.0.125": "SATEESHK",
    "192.168.0.205": "SESHASAI-QA",
    "192.168.0.212": "JAIPAL",
    "192.168.0.214": "VAMSI-QA",
    "192.168.0.240": "SATISH-CNG",
    "192.168.0.245": "NAVEEN-QA",
    "192.168.1.2": "PANDORANETWORKS",
    "192.168.1.25": "PL-217",
    "192.168.1.47": "47-box",
    "192.168.1.72": "VIVEK",
    "192.168.1.118": "linux7",
    "192.168.1.119": "linux10",
    "192.168.1.155": "QAtesting ",
    "192.168.1.163": "KMAHESH-LAPTOP",
    "192.168.1.171": "MONITORING2",
    "192.168.1.172": "linux",
    "192.168.1.179": "VRAVI",
    "192.168.1.238": "MACBOOKAIR-DE30",
    "192.168.1.245": "BMAHESH-DBA",
    "192.168.1.252": "VARAPRASAD",
    "192.168.2.4": "RPAVAN",
    "192.168.2.26": "GOPIKUMAR-QA",
    "192.168.2.29": "SURESHK-QA",
    "192.168.2.37": "YAGNENDER",
    "192.168.2.41": "SAMEER",
    "192.168.2.45": "SYEDKAZIM-ORANG",
    "192.168.2.56": "SAIGOUD",
    "192.168.2.62": "NARESH-P",
    "192.168.2.65": "OPS-LAPTOP",
    "192.168.2.84": "NARENDRA",
    "192.168.2.89": "BALRAJ",
    "192.168.2.103": "VEERAHANUMANTH",
    "192.168.2.115": "UBUNTUSERVER",
    "192.168.2.127":"lenovoTouch",
    "192.168.2.139":"HARIHARAN",
    "192.168.2.150":"EMAHESH-OPS",
    "192.168.2.151":"MAHESHS-QA",
    "192.168.2.164":"OPSMONITORING",
    "192.168.2.166":"SURESHK-QA",
    "192.168.2.170":"BALAKRISHNA-LAP",
    "192.168.2.178":"SatishRanganathan",
    "192.168.2.180":"SRINIVAS-CEG",
    "192.168.2.192":"netbox.localdomain.com",
    "192.168.2.194":"SURYANEW-LAPTOP",
    "192.168.2.209":"MNARESH",
    "192.168.2.233":"SRINIVASMUDDALA",
    "192.168.3.5":"EPAVAN-QA",
    "192.168.3.6":"CHARY-LAPTOP",
    "192.168.3.7":"PND-OPS",
    "192.168.3.13":"OMKAR-OFFICE",
    "192.168.3.26":"KOTESWAR",
    "192.168.3.29":"QA-AUTOMATION",
    "192.168.3.54":"SOMETHING-PC",
    "192.168.3.98":"BEN",
    "192.168.3.119":"MSI-Build.Panterra.com",
    "192.168.3.149":"BALUNAYAK-ISC",
    "192.168.3.173":"MURALI-IMAC-2",
    "192.168.3.174":"SRINIVAS-CEG",
    "192.168.3.190":"SMAHESH-QA",
    "192.168.0.2":"K8-1",
    "192.168.0.3":"K8-2",
    "192.168.1.3":"Invalid argument",
    "192.168.0.4":"localhost.localdomain",
    "192.168.0.6":"sparkmaster3",
    "192.168.2.17":"VM4",
    "192.168.2.18":"alpha218",
    "192.168.3.20":"sai-nivas",
    "192.168.1.21":"Afzal",
    "192.168.1.22":"Sharan",
    "192.168.1.23":"Dhananjay",
    "192.168.1.28":"Riyaz",
    "192.168.3.31":"Akhil",
    "192.168.1.32":"Pavankumar",
    "192.168.2.32":"CMohan",
    "192.168.3.36":"krishnaveni",
    "192.168.2.46":"localhost.localdomain",
    "192.168.1.47":"47-box",
    "192.168.1.51":"localhost.localdomain",
    "192.168.3.52":"vikas",
    "192.168.1.53":"localhost.localdomain",
    "192.168.1.54":"localhost.localdomain",
    "192.168.1.57":"Nawaj",
    "192.168.1.68":"server1.crazytechgeek.info",
    "192.168.3.76":"Deepika",
    "192.168.1.77":"Venu",
    "192.168.1.83":"Ranjith",
    "192.168.1.84":"localhost.localdomain",
    "192.168.1.85":"Deepika",
    "192.168.1.87":"master1.hadoop.com",
    "192.168.1.92":"myredmine.beta-wspbx.com",
    "192.168.2.92":"Veerender",
    "192.168.1.94":"ganesh",
    "192.168.1.95":"VRavi",
    "192.168.1.96":"localhost.localdomain",
    "192.168.0.100":"alpha2-201.pandorarndlabs.net",
    "192.168.0.101":"alpha2-202.pandorarndlabs.net",
    "192.168.1.101":"SmartBox6",
    "192.168.3.101":"Sushmitha",
    "192.168.1.102":"alpha1-101.pandorarndlabs.net",
    "192.168.0.103":"alpha2-204.pandorarndlab.net",
    "192.168.1.103":"alpha1-102.pandorarndlabs.net",
    "192.168.0.104":"alpha2-205.pandorarndlabs.net",
    "192.168.1.104":"alpha1-103.pandorarndlabs.net",
    "192.168.0.105":"alpha2-206.pandorarndlabs.net",
    "192.168.1.105":"alpha1-104.pandorarndlabs.net",
    "192.168.0.106":"alpha2-207.pandorarndlabs.net",
    "192.168.1.106":"Santosh",
    "192.168.0.107":"alpha2-208.pandorarndlabs.net",
    "192.168.1.107":"Nagoor",
    "192.168.0.108":"alpha2-209.pandorarndlabs.net",
    "192.168.1.108":"alpha1-105.pandorarndlabs.net",
    "192.168.0.109":"alpha2-210.pandorarndlabs.net",
    "192.168.0.110":"alpha2-211.pandorararndlabs.com",
    "192.168.1.110":"alpha1-106.pandorarndlabs.net",
    "192.168.0.111":"alpha2-212.pandorarndlabs.net",
    "192.168.1.111":"alpha1-107.beta-wspbx.com",
    "192.168.0.112":"alpha2-213.pandorarndlabs.net",
    "192.168.1.112":"Alpha1-108.pandorarndlabs.net",
    "192.168.0.113":"alpha2-214.pandorarndlabs.net",
    "192.168.1.114":"alpha1-110.pandorarndlabs.net",
    "192.168.1.115":"alpha1-111.pandorarndlabs.net",
    "192.168.1.116":"116-Box",
    "192.168.1.118":"localhost.localdomain",
    "192.168.1.119":"localhost.localdomain",
    "192.168.1.147":"localhost.localdomain",
    "192.168.1.160":"sparkmaster",
    "192.168.1.168":"dastagiri",
    "192.168.1.172":"localhost.localdomain",
    "192.168.2.183":"master2.hadoop.com",
    "192.168.1.189":"localhost.localdomain",
    "192.168.2.204":"2.204",
    "192.168.3.206":"localhost.localdomain",
    "192.168.1.209":"localhost.localdomain",
    "192.168.1.210":"alpha1-110.pandorarndlabs.net",
    "192.168.1.219":"ratnaraju",
    "192.168.1.232":"MShravan",
    "192.168.1.248":"Bhargav"
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
                    netbox.ipam.create_ip_address(str(ipaddress),dns_name="unknown")
                    print("Not---------")
                    
            else:
                print("Faild")
        else:
            print("IP in netbox",ipaddress)

      
