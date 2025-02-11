import socket # We use socket inorder to communicate with udp



class handler:
    def __init__(self, local_ip: str, local_port: int, buffer_size: int):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.udp_handler = udp_handler(self.local_ip, self.local_port, self.buffer_size)
        print("lol")

    # change ip and port
    def change_socket(self, local_ip: str, local_port: int):
        print("changing ip and port from ip:{} port{} -> ip:{} port{}".format(self.local_ip, self.local_port, local_ip, local_port))




class udp_handler:
    def __init__(self, local_ip: str, local_port: int, buffer_size: int):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_server_socket.bind((self.local_ip, self.local_port))
        print("udp server up and listening")



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
