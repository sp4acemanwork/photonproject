import socket
from database import database_handler


# you should do all main functions of the back end through this class
class handler:
    def __init__(self, target_ip: str, local_port_listen: int, local_port_send: int, buffer_size: int):
        self.target_ip = target_ip
        self.local_port_listen = local_port_listen
        self.local_port_send = local_port_send
        self.buffer_size = buffer_size
        # bind to listen for incoming traffic
        self.udp_handler = udp_handler("127.0.0.1", self.local_port_send, self.local_port_listen, self.buffer_size)
        self.database_handler = database_handler()
    def start_game(self):
        print("printing values")
        self.udp_handler.send_message("202", [self.target_ip, self.local_port_send])
    

    # change ip and port
    def change_socket(self, new_target_ip: str, new_local_port: int):
        print("changing ip and port from ip:{} port:{} -> ip:{} port:{}".format(self.target_ip, self.local_port_send, new_target_ip, new_local_port))

        # close original socket and set up new socket
        self.udp_handler.udp_client_socket.close()
        self.udp_handler.udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_handler.udp_client_socket.bind((new_target_ip,new_local_port))

        self.udp_handler.send_ip = new_target_ip
        self.udp_handler.send_port = new_local_port


    # call thing with address to send?
    # this function will call the add player to database then transit the equipment codes for player?

    def add_player(self, player_name: str, player_id: int, equipment_id: int):
        player_tuple = (player_id, player_name)
        self.database_handler.add_player(player_tuple)
        test = (self.target_ip, self.local_port_send)
        self.udp_handler.send_message(str(equipment_id), test)
        #  add check for if user is in the table already
        
        self.database_handler.print_table()

    def recive_message(self) -> tuple[str, str]:
        return self.udp_handler.recive_message()


# this class shouldn't be called directly rather use the functions that do the sending functions automatically
class udp_handler:
    def __init__(self, target_ip: str, listen_port: int,send_port: int, buffer_size: int):
        self.send_ip = target_ip
        self.listen_ip = target_ip
        # self.target_ip = target_ip
        self.listen_port = listen_port
        self.send_port = send_port
        self.buffer_size = buffer_size

        # create socket for listening 
        self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_server_socket.bind((self.listen_ip, self.listen_port))
        print("udp server up and listening")

        # create socket for sending 
        self.udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_client_socket.bind((self.send_ip, self.send_port))
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

        message_from_server = "Message Received"
        bytes_to_send = str.encode(message_from_server)

        self.udp_server_socket.sendto(bytes_to_send,address)
        return bytes_address_pair

    # this function takes -> (message, tuple:[ip, port])
    def send_message(self, send_message: str, address: tuple[str, str]):
        try:
            bytes_to_send = str.encode(send_message)
            self.udp_client_socket.sendto(bytes_to_send, address)

            self.recive_message()

            msgFromServer = self.udp_client_socket.recvfrom(self.buffer_size)
            msg = "Message from server: {}".format(msgFromServer)
            print(msg)
        except Exception as e:
            print("error occured sending {}".format(e))


