from re import I
import ipcalc
import networkscan
from netbox import NetBox
import requests
import socket
import json
InstanceData ="""{
    "192.168.0.100/32": "shubham",
    "192.168.0.101": "Veeru"
}"""
Ins = json.loads(InstanceData)
headers = {
    'content-type': "application/json",
    'authorization': "Token c384a68ab0733a26c11b60ac0221180f10a86d1a",
    'cache-control': "no-cache",
    'postman-token': "356fdcce-4d66-a618-1d36-f44f4588d057"
    }
NB_URL = "http://192.168.0.108"
netbox = NetBox(host='192.168.0.108',port=8001, use_ssl=False,auth_token='c384a68ab0733a26c11b60ac0221180f10a86d1a')

if __name__ == '__main__':

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
        # print(netboxip)
        print(netboxip['count'])    
        # if not in netbox
        if netboxip['count'] == 0:
            # check if in network exists and not exists in netbox
            if ipaddress in found_ip_in_network:
                if ipaddress in Ins:
                    print("%s is found in JSON data" %ipaddress)
                    print("The value of", ipaddress,"is", Ins[ipaddress])                     
                    # Adding in IP netbox            
                    netbox.ipam.create_ip_address(str(ipaddress),dns_name=hostnamepass)
                    # netbox.ipam.create_ip_address(str(ipaddress),dns_name="shubham")
                else:
                    netbox.ipam.create_ip_address(str(ipaddress),dns_name="success")
                    
            else:
                pass
        else:
            # if not exits in netbox and network
            if ipaddress in found_ip_in_network:
                pass
            else:
                # if not exists in network but exists in netbox then delete from netbox
                netbox.ipam.delete_ip_address(str(ipaddress))