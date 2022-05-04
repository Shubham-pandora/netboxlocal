import socket

def ippattern(i,j):
    a = "192.168."+str(i)+"."+str(j)
    return a  

for i in range(0,4):
    for j in range(0,256):  
        b = ippattern(i,j)
        try:
            # print(b)
            c = socket.gethostbyaddr(b)      
            print('"',b,'":','"',c[0],'"')
            # print(b,c[0])
        except:
            pass
            # print(" ")
