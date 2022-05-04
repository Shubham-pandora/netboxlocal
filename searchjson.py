# Import json module
import json

# Define json data
customerData ="""{
    "192.168.0.2": "shubham",
    "192.168.0.3": "Veeru"
}"""
print(customerData)
# Input the key value that you want to search
keyVal = "192.168.0.2"
# keyVal = input("Enter a key value: \n")
print(type(keyVal))
# load the json data
customer = json.loads(customerData)
# Search the key value using 'in' operator
print(keyVal,customer)
if keyVal in customer:
    # Print the success message and the value of the key
    print("%s is found in JSON data" %keyVal)
    print("The value of", keyVal,"is", customer[keyVal])
else:
    # Print the message if the value does not exist
    print("%s is not found in JSON data" %keyVal)