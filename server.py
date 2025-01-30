import socket


# possibly handle client server com using tcp disscus with team

class tcp_handler:
    def __init__(self):
        print("lol")


class udp_handler:
    def __init__(self, local_ip: str, local_port: int, buffer_size: int):
        self.local_ip
        self.local_port
        self.buffer_size
        self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_server_socket.bind(local_ip, local_port)
        print("udp server up and listening")

    # idea make it async
    def recive_message(self):
        bytes_address_pair = self.udp_server_socket.recv(self.buffer_size)
        message = bytes_address_pair[0]
        address = bytes_address_pair[1]
        client_msg = "message from client:{}".format(message)
        client_ip = "client ip:{}".format(address)
        print(client_msg)
        print(client_ip)

    def send_message(self, send_message):
        bytes_to_send = str.encode(send_message)




class data_base_handler():
    def __init__():
        print("lol")


def __main__():
    print("starting server")
