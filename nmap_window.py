import socket

# def ippattern(i,j):
#     for i in range(0,4):
#         for j in range(0,20): 
#             print("192.168."+str(i)+"."+str(j))

def ippattern(i,j):
    a = "192.168."+str(i)+"."+str(j)
    return a
    # print("192.168."+str(i)+"."+str(j)) 

for i in range(0,4):
    for j in range(0,20):  
        b = ippattern(i,j)
        try:
            print("\n",b)
            c = socket.gethostbyaddr(b)
            print(c[0])
        except:
            print("pass")

# except Exception as ex:
#     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#     message = template.format(type(ex).__name__, ex.args)
#     print(message)

# b = "192.168.0.0"
# a = socket.gethostbyaddr(b)
# print(a[0])

# a = socket.gethostbyaddr("192.168.3.119")
# print(type(a))


