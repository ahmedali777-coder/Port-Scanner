import socket

host=str(input("Enter Your Target IP or Domain : "))
ports=[80,20,21,22,23,25,110,119,143,123,67,68,137,138,139,445,990,989,53,443,8080,48080]

for port in ports :
    connection=socket.socket()
    connection.settimeout(1)
    try :
    
        connection.connect((host,port))
       
        service=socket.getservbyport(port)
        print(f"port {port} is open " + " "+"Service : "+service)
        

    except:
        print(f"port {port} is close")
    connection.close()

