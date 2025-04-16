import socket
from database import database_handler
import re


class usr:
    def __init__(self, name: str, id:int, team: str):
        self.name = name
        self.score = 0
        self.id = id
        self.base_score = 0
        self.team = team # check to see how players are sorted


# you should do all main functions of the back end through this class
class handler:
    def __init__(self, target_ip: str, port: int, send_port: int, buffer_size: int):
        self.target_ip = target_ip
        self.port = port
        self.buffer_size = buffer_size
        self.udp_handler = udp_handler("127.0.0.1", self.port, self.buffer_size)
        self.database_handler = database_handler()
        self.local_score_keep = {}  # keeps a list of usr obj
        self.messages = []
        self.local_port_send = send_port
    def start_game(self):
        print("printing values")
        self.udp_handler.send_message("202", (self.target_ip, self.local_port_send))

    def end_game(self):
        for i in range(4):
            self.udp_handler.send_message("221", (self.target_ip, self.local_port_send))

    def get_list_of_usrs(self) -> dict:
        return self.local_score_keep
    def get_messages(self):
        return self.messages
    # change ip
    def change_socket(self, new_target_ip: str):
        print("changing ip from ip:{} -> ip:{}".format(self.target_ip, new_target_ip))

        # close original socket and set up new socket
        self.udp_handler.udp_server_socket.close()
        self.udp_handler.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_handler.udp_server_socket.bind((new_target_ip, self.port))
        self.target_ip = new_target_ip

    # call thing with address to send?
    # this function will call the add player to database then transit the equipment codes for player?

    def add_player(self, player_name: str, player_id: int, equipment_id: int, team: str):
        player_tuple = (player_id, player_name)
        self.database_handler.add_player(player_tuple)
        test = (self.target_ip, self.port)
        self.udp_handler.send_message(str(equipment_id), test)
        #  add check for if user is in the table already
        newusr = usr(player_name, player_id, team)
        self.local_score_keep[equipment_id] = newusr
        # self.udp_handler.recive_message()
        # self.database_handler.print_table()

    def player_exists(self, new_id: str):
        return self.database_handler.player_exists(new_id)

    def recive_message(self) -> tuple[str, str]:
        return self.udp_handler.recive_message()

    def get_base_score(self, equipment_id: str) -> tuple[str, int]:
        return (self.local_score_keep[equipment_id].name, self.local_score_keep[equipment_id].scored)

    def get_score(self, equipment_id: str) -> tuple[str, int]:
        return (self.local_score_keep[equipment_id].name, self.local_score_keep[equipment_id].score)

    #                                           [player,  b to their name]
    def recive_event(self) -> tuple[str, bool]:  # figure out what to return
        mesg: tuple = self.udp_handler.recive_message()
        event: str = mesg[0]
        part = re.split(r":", event, maxsplit=1)
        player = self.local_score_keep[part[0]]
        if len(part) == 2:
            if part[1] == "43":
                print(f"user id:{part[0]} scored for RED {player.team}")
                self.messages.append(f"{player.name} scored for {player.team}")
                if player.team == "RED TEAM":
                    player.base_score += 1
                    player.score += 100
                else:
                    player.score -= 10

                self.udp_handler.send_message(str(player.score), (self.target_ip, self.local_port_send))
                return (part[0], True)
            if part[1] == "53":
                print(f"user id:{part[0]} scored for GREEN {player.team}")
                self.messages.append(f"{player.name} scored for {player.team}")
                if player.team == "GREEN TEAM":
                    player.base_score += 1
                    player.score += 100
                else:
                    player.score -= 10

                self.udp_handler.send_message(str(player.score), (self.target_ip, self.local_port_send))
                return (part[0], True)
            else:
                player1 = self.local_score_keep[part[1]]
                print(f"user id:{part[0]} tagged user id:{part[1]}")
                self.messages.append(f"{player.name} tagged {player1.name}")
                if player.team == "GREEN TEAM":
                    player.score += 10
                else:
                    player.score += 10
                self.udp_handler.send_message(part[1], (self.target_ip, self.local_port_send))
                # if player.base_score == 1:
                #     return (part[0], True)
        return (part[0], False)


# this class shouldn't be called directly rather use the functions that do the sending functions automatically
class udp_handler:
    def __init__(self, target_ip: str, local_port: int, buffer_size: int):
        self.target_ip = target_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_server_socket.bind((self.target_ip, self.local_port))
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
        decodedmsg = bytes_address_pair[0].decode('utf-8')
        return (decodedmsg, address)

    # this function takes -> (message, tuple:[ip, port])
    def send_message(self, send_message: str, address: tuple[str, str]):
        try:
            bytes_to_send = str.encode(send_message)
            self.udp_server_socket.sendto(bytes_to_send, address)
        except Exception as e:
            print("error occured sending {}".format(e))


# def __main__():
#     print("starting test")

#     test = handler("127.0.0.1", 7501, 7500, 1024)
#     test.start_game()
#     while (True):

#         user_name = input("enter name: ")
#         user_id = int(input("enter id: "))
#         user_eqid = int(input("enter equipment id: "))
#         test.add_player(user_name, user_id, user_eqid)


# __main__()
