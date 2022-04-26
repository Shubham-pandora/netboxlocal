# def create_ip_address( address, **kwargs):
#     """Create a new ip address

#     :param address: IP address
    
#     :param kwargs: Optional arguments
#     :return: netbox object if successful otherwise raise CreateException
#     """
#     required_fields = {"address": address}
#     return (required_fields, **kwargs)

# ipaddress = "192.168.1.121"
# create_ip_address(str(ipaddress))

def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total


print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))