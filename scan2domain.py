import ipcalc
import networkscan
from netbox import NetBox
import requests
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
        print(address1)
        netbox.ipam.create_ip_address(address1)
        

