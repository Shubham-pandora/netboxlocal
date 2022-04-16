from netbox import netbox
netbox = NetBox(host='192.168.0.108',port=8001,use_ssl=False,auth_token='c384a68ab0733a26c11b60ac0221180f10a86d1a')

nb_dev_role = netbox.dcim.get_device_roles()
print(nb_dev_role)