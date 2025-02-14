import socket
from database import database_handler
# possibly handle client server com using tcp disscus with team


class tcp_handler:
    def __init__(self):
        print("lol")


# you should do all main functions of the back end through this class
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

    def add_player(self, player_name: str, player_id: int, equipment_id: int):
        database_handler.add_player([player_id, player_name])
        self.udp_handler.send_message(equipment_id, [self.local_ip, self.local_port])
        database_handler.print_table()


# this class shouldn't be called directly rather use the functions that do the sending functions automatically
class udp_handler:
    def __init__(self, local_ip: str, local_port: int, buffer_size: int):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_server_socket.bind((self.local_ip, self.local_port))
        print("udp server up and listening")

    # idea make it async
    # this function waits for a response from the listening port and then returns a tuple with [ip,port]
    def recive_message(self) -> tuple[str, tuple[str, str]]:
        bytes_address_pair = self.udp_server_socket.recvfrom(self.buffer_size)
        message = bytes_address_pair[0]
        address = bytes_address_pair[1]
        client_msg = "message from client:{}".format(message)
        client_ip = "client ip:{}".format(address)
        print(client_msg)
        print(client_ip)
        return bytes_address_pair

    # this function takes -> (message, tuple:[ip, port])
    def send_message(self, send_message: str, address: tuple[str, str]):
        try:
            bytes_to_send = str.encode(send_message)
            self.udp_server_socket.sendto(bytes_to_send, address)
        except:
            print("error occured sending")


# test class for debugging purposes
def __main__():
    print("starting test")


__main__()
