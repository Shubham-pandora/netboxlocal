import socket

def ippattern(i,j):
    a = "192.168."+str(i)+"."+str(j)
    return a  

for i in range(3,4):
    for j in range(0,20):  
        b = ippattern(i,j)
        try:
            # print(b)
            c = socket.gethostbyaddr(b)      
            print('"',b,'":','"',c[0],'"')
            # print(b,c[0])
        except:
            pass
            # print(" ")



# (env) C:\Users\Build\Desktop\itsme>python test.py
# " 192.168.3.5 ": " EPAVAN-QA "
# " 192.168.3.7 ": " PND-OPS "
# " 192.168.3.13 ": " OMKAR-OFFICE "