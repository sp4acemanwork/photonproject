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


<<<<<<< HEAD
# # possibly handle client server com using tcp
# class tcp_handler:
#     def __init__(self):
#         print("lol")


# class udp_handler:
#     def __init__(self, local_ip: str, local_port: int, buffer_size: int):
#         print("lol")
=======
# possibly handle client server com using tcp disscus with team

class tcp_handler:
    def __init__(self):
        print("lol")


class udp_handler:
    def __init__(self, local_ip: str, local_port: int, buffer_size: int):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_server_socket.bind((self.local_ip, self.local_port))
        print("udp server up and listening")

    # idea make it async
    def recive_message(self) -> tuple[str, tuple[str, str]]:
        bytes_address_pair = self.udp_server_socket.recvfrom(self.buffer_size)
        message = bytes_address_pair[0]
        address = bytes_address_pair[1]
        client_msg = "message from client:{}".format(message)
        client_ip = "client ip:{}".format(address)
        print(client_msg)
        print(client_ip)
        return bytes_address_pair

    def send_message(self, send_message: str, address: tuple[str, str]):
        bytes_to_send = str.encode(send_message)
        self.udp_server_socket.sendto(bytes_to_send, address)
>>>>>>> f6d43037a174b940cc41093731474be5f61d6d49


# class data_base_handler():
#     def __init__():
#         print("lol")


<<<<<<< HEAD
# def __main__():
#     print("starting server")
=======
def __main__():
    print("starting server")
    # create udp handler with udp_handler(ip, port, buffer size)
    udpexample = udp_handler("127.0.0.1", 7501, 1024)
    print("listening on 127.0.0.1 port 7501")
    while (True):
        # message and address gets returned as a tuple
        addandmes = udpexample.recive_message()
        # there's a tuple in a tuple with the format [address, port] that this function takes for the address
        # call this function with the format send_message("message", tuple[address:str, port:str])
        udpexample.send_message("test", addandmes[1])


__main__()
>>>>>>> f6d43037a174b940cc41093731474be5f61d6d49
