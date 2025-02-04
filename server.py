import socket # We use socket inorder to communicate with udp

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client: "
bytesToSend   = str.encode(msgFromServer) # encode turns string into bytes

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort)) # implementing the socket

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize) # receive both the address and bufferSize
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client: {}".format(message.decode())
    clientIP  = "Client IP Address: {}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)

# import socket

# local_ip = "127.0.0.1"


# # possibly handle client server com using tcp
# class tcp_handler:
#     def __init__(self):
#         print("lol")


# class udp_handler:
#     def __init__(self, local_ip: str, local_port: int, buffer_size: int):
#         print("lol")


# class data_base_handler():
#     def __init__():
#         print("lol")


# def __main__():
#     print("starting server")
