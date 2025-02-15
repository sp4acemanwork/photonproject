
import socket

import socket


# possibly handle client server com using tcp disscus with team


class tcp_handler:
    def __init__(self):
        print("lol")


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

    # call thing with address to send?
    # this function will call the add player to database then transit the equipment codes for player?

    def add_player(self, player_name: str, player_id: str, address_to_send: tuple[str, tuple[str, str]]):
        data_base_handler.add_player(player_name, player_id)
        self.udp_handler.send_message("equipment codes?", ["127.0.0.1", "someport"])



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


class data_base_handler():
    def __init__():
        print("lol")


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
